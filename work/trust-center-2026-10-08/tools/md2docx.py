#!/usr/bin/env python3
"""
通用 md 轉 Word。沿用 md2docx_traffic.py 的排版樣式，改成吃參數，不要再為每份文件複製一個腳本。

本檔是 腳本工具/md2docx.py 的副本（2026-10-08 從對話紀錄還原），改了五處：
長文字欄（理由、建議、要修什麼等）給較寬的欄寬；內容全是短字的欄縮窄；
編號清單直接寫出數字，不再用 Word 會跨段接續的 List Number；跳過 <!-- --> 註解行；欄寬同步寫進表格格線。
確認沒問題後可以把這兩處併回 腳本工具/md2docx.py，再刪掉本副本。

用法：
    python3 腳本工具/md2docx.py 來源.md [輸出.docx] [--landscape]

不給輸出路徑就用同名 .docx。表格多或欄位長的文件加 --landscape。
"""
import re, sys, os
from docx import Document
from docx.shared import Pt, Cm, Emu, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ACCENT = RGBColor(0xC0, 0x8A, 0x00)
DARK = RGBColor(0x33, 0x33, 0x33)
GREY = RGBColor(0x66, 0x66, 0x66)
CODEBG = "F4F4F4"


def set_font(run, size=11, bold=False, color=DARK, italic=False, mono=False):
    run.font.name = "Consolas" if mono else "Microsoft YaHei"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "微軟正黑體")
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = color


def add_runs(p, text, size=11, bold=False, color=DARK, italic=False):
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    for i, seg in enumerate(re.split(r"\*\*(.+?)\*\*", text)):
        if not seg:
            continue
        r = p.add_run(seg)
        set_font(r, size=size, bold=bold or (i % 2 == 1), color=color, italic=italic)


def shade_para(p, fill):
    pPr = p._p.get_or_add_pPr()
    sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear")
    sh.set(qn("w:fill"), fill)
    pPr.append(sh)


def shade_cell(tc, fill):
    sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear")
    sh.set(qn("w:fill"), fill)
    tc._tc.get_or_add_tcPr().append(sh)


def build(src, out, landscape=False):
    doc = Document()
    sec = doc.sections[0]
    if landscape:
        sec.orientation = WD_ORIENT.LANDSCAPE
        sec.page_width, sec.page_height = Cm(29.7), Cm(21)
        sec.top_margin = sec.bottom_margin = Cm(1.8)
        sec.left_margin = sec.right_margin = Cm(1.8)
    else:
        sec.page_width, sec.page_height = Cm(21), Cm(29.7)
        sec.top_margin = sec.bottom_margin = Cm(2.2)
        sec.left_margin = sec.right_margin = Cm(2.4)
    usable_emu = int(sec.page_width) - int(sec.left_margin) - int(sec.right_margin)

    footer_p = sec.footer.paragraphs[0]
    footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fld = footer_p.add_run()
    set_font(fld, size=9, color=GREY)
    for tag, attr in [("w:fldChar", {"w:fldCharType": "begin"}),
                      ("w:instrText", None),
                      ("w:fldChar", {"w:fldCharType": "end"})]:
        el = OxmlElement(tag)
        if attr:
            for k, v in attr.items():
                el.set(qn(k), v)
        if tag == "w:instrText":
            el.set(qn("xml:space"), "preserve")
            el.text = "PAGE"
        fld._element.append(el)

    lines = open(src, encoding="utf-8").read().split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        if line.strip().startswith("```"):
            i += 1
            code = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            for cl in code:
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Cm(0.4)
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.1
                shade_para(p, CODEBG)
                r = p.add_run(cl if cl.strip() else " ")
                set_font(r, size=9, color=DARK, mono=True)
            doc.add_paragraph()
            continue

        if line.strip().startswith("<!--"):
            i += 1
            continue

        if not line.strip() or line.strip() == "---":
            i += 1
            continue

        m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$", line.strip())
        if m:
            cap, path = m.group(1), m.group(2)
            if not os.path.isabs(path):
                path = os.path.join(os.path.dirname(os.path.abspath(src)), path)
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            p.add_run().add_picture(path, width=Emu(usable_emu))
            if cap:
                cp = doc.add_paragraph()
                cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                cp.paragraph_format.space_after = Pt(12)
                add_runs(cp, cap, size=9, color=GREY, italic=True)
            i += 1
            continue

        if line.startswith("|"):
            tbl_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl_lines.append(lines[i].strip())
                i += 1
            rows = [[c.strip() for c in tl.strip("|").split("|")] for tl in tbl_lines
                    if not re.match(r"^\|[\s\-:|]+\|$", tl)]
            if not rows:
                continue
            ncol = max(len(r) for r in rows)
            table = doc.add_table(rows=len(rows), cols=ncol)
            table.style = "Table Grid"
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            table.autofit = False

            # 欄寬依表頭語意分配：網址欄給大一點，排名與語系欄縮小
            hdr = rows[0] + [""] * (ncol - len(rows[0]))
            weights = []
            for h in hdr:
                if "網址" in h or "URL" in h.upper():
                    weights.append(3.2)
                elif any(k in h for k in ("內容", "為什麼", "備註", "理由", "建議", "後果",
                                           "要修", "放什麼", "做什麼", "還缺", "要問", "現況", "做法")):
                    weights.append(3.0)
                elif h in ("編號", "順序", "批次"):
                    weights.append(0.9)
                elif "排名" in h or "順位" in h or "語系" in h:
                    weights.append(1.3)
                else:
                    weights.append(1.8)
            # 內容全是短字（例如 ● ◐ ○、家數）的欄縮窄，把寬度讓給文字欄
            for ci in range(ncol):
                body = [r[ci] for r in rows[1:] if ci < len(r)]
                if body and max(len(c) for c in body) <= 4:
                    weights[ci] = min(weights[ci], 0.8)
                elif hdr[ci] in ("項目", "頁面", "題目", "入口", "區塊"):
                    weights[ci] = max(weights[ci], 2.4)
            total = sum(weights)
            widths = [Emu(int(usable_emu * w / total)) for w in weights]
            # 同步寫進表格欄格線，LibreOffice 與部分 Word 版本只看這裡的欄寬
            for gc, wd in zip(table._tbl.tblGrid.findall(qn("w:gridCol")), widths):
                gc.set(qn("w:w"), str(int(wd / 635)))

            for ri, row in enumerate(rows):
                for ci in range(ncol):
                    cell = row[ci] if ci < len(row) else ""
                    tc = table.rows[ri].cells[ci]
                    tc.width = widths[ci]
                    tc.paragraphs[0].text = ""
                    tc.paragraphs[0].paragraph_format.space_after = Pt(2)
                    add_runs(tc.paragraphs[0], cell, size=8.5, bold=(ri == 0))
                    if ri == 0:
                        shade_cell(tc, "F2F2F2")
            doc.add_paragraph()
            continue

        m = re.match(r"^(#{1,4})\s+(.*)", line)
        if m:
            lv, txt = len(m.group(1)), m.group(2)
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(4 if lv == 1 else 14)
            p.paragraph_format.space_after = Pt(8)
            add_runs(p, txt, size={1: 19, 2: 15, 3: 12.5, 4: 11.5}[lv], bold=True,
                     color=DARK if lv == 1 else (ACCENT if lv == 2 else DARK))
            i += 1
            continue

        if line.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip("> ").strip())
                i += 1
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.6)
            p.paragraph_format.space_after = Pt(10)
            add_runs(p, "  ".join(b for b in buf if b), size=10, color=GREY, italic=True)
            continue

        m = re.match(r"^(\d+)\.\s+(.*)", line) or re.match(r"^[-*]\s+(.*)", line)
        if m:
            txt = m.group(2) if m.lastindex == 2 else m.group(1)
            num = re.match(r"^(\d+)\.", line)
            if num:
                # Word 的 List Number 會跨段接續編號，改成直接寫出原本的數字
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Cm(0.63)
                p.paragraph_format.first_line_indent = Cm(-0.63)
                txt = f"{num.group(1)}.  {txt}"
            else:
                p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.space_after = Pt(4)
            add_runs(p, txt, size=10.5)
            i += 1
            continue

        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.line_spacing = 1.35
        add_runs(p, line, size=10.5)
        i += 1

    doc.save(out)
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    landscape = "--landscape" in sys.argv
    if not args:
        sys.exit(__doc__)
    src = args[0]
    out = args[1] if len(args) > 1 else os.path.splitext(src)[0] + ".docx"
    print("saved:", build(src, out, landscape))
