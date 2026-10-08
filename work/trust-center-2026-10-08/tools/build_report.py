#!/usr/bin/env python3
"""把各章 md 組成完整報告，並轉成 docx。

用法（在專案根目錄或任何地方執行皆可）：
    python3 work/trust-center-2026-10-08/tools/build_report.py

產出：
    work/trust-center-2026-10-08/report.md
    outputs/Hotcoin-安全與信任中心規劃-2026-10-08.md
    outputs/Hotcoin-安全與信任中心規劃-2026-10-08.docx
"""
import os, re, sys, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BASE))
sys.path.insert(0, HERE)
import build_matrix  # noqa: E402
from md2docx import build  # noqa: E402

PARTS = ['report-header.md', 'report-part0-basis.md', 'report-part1-gaps.md',
         'report-part2-hub.md', 'report-part4-decisions.md', 'report-appendix.md']
NAME = 'Hotcoin-安全與信任中心規劃-2026-10-08'


def read(name):
    return open(os.path.join(BASE, name), encoding='utf-8').read().strip('\n')


def matrix_table():
    return '\n'.join(l for l in read('matrix.md').splitlines() if l.startswith('|'))


def main():
    build_matrix.main()
    chunks = []
    for part in PARTS:
        text = read(part)
        text = text.replace('<!-- include: report-part3-inventory.md -->', read('report-part3-inventory.md'))
        text = text.replace('<!-- include-table: matrix.md -->', matrix_table())
        chunks.append(text)
    full = '\n\n'.join(chunks) + '\n'
    leftover = re.findall(r'<!--.*?-->', full)
    if leftover:
        sys.exit(f'未替換的 include：{leftover}')
    report = os.path.join(BASE, 'report.md')
    open(report, 'w', encoding='utf-8').write(full)
    out_dir = os.path.join(ROOT, 'outputs')
    os.makedirs(out_dir, exist_ok=True)
    md_out = os.path.join(out_dir, NAME + '.md')
    shutil.copyfile(report, md_out)
    docx_out = build(md_out, os.path.join(out_dir, NAME + '.docx'), landscape=True)
    print('report:', report)
    print('docx:', docx_out)


if __name__ == '__main__':
    main()
