# 安全與信任中心規劃（2026-10-08）

接續 10-08 上午在本機 `SEO顧問-決策副本/work/trust-center-2026-10-08/` 進行、因用量上限中斷的工作。這一輪在雲端環境完成，檔案放在 GitHub `wannn1214/111`，要放回本機專案時，整個資料夾照原路徑複製回去即可。

## 交付物

- `outputs/Hotcoin-安全與信任中心規劃-2026-10-08.docx`：繁中決策版，橫式 20 頁
- `outputs/Hotcoin-安全與信任中心規劃-2026-10-08.md`：同內容 markdown

## 本資料夾

| 檔案 | 內容 | 來源 |
|---|---|---|
| `checklist.md` | 38 項檢查清單 | 上一輪寫的，從對話紀錄還原 |
| `competitors/hotcoin.md` | Hotcoin 38 項實測 | 上一輪寫的，從對話紀錄還原（含 C8 那次修正） |
| `competitors/{11 家}.md` | 競品逐項證據 | 本輪，網頁搜尋讀取 |
| `matrix.md` | 38 項 × 12 家對照矩陣 | `tools/build_matrix.py` 產生，不要手改 |
| `report-header.md` | 開頭結論 | 本輪 |
| `report-part0-basis.md` | 第一章 判斷依據 | 上一輪寫的，本輪改了「對照組」最後一段讀取方式 |
| `report-part1-gaps.md` | 第二章 第一部分：缺口與判斷 | 本輪 |
| `report-part2-hub.md` | 第三章 第二部分：Hub 規劃 | 本輪 |
| `report-part3-inventory.md` | 3.1 內容與資料盤點表 | 上一輪寫的，本輪加了 3 列 |
| `report-part4-decisions.md` | 第四章 需要決定的事 | 本輪 |
| `report-appendix.md` | 附錄 A、B、C | 本輪 |
| `report.md` | 組好的完整報告 | `tools/build_report.py` 產生 |
| `tools/build_report.py` | 重組報告並轉 docx | 本輪 |
| `tools/md2docx.py` | `腳本工具/md2docx.py` 的副本，改了欄寬、編號與註解行 | 本輪 |
| `tools/verify_local.sh` | 本機補驗競品 security.txt 與 Hub 頁 | 本輪，要在你的電腦跑 |
| `tools/shots.sh` | 競品 Hub 截圖清單，呼叫 `腳本工具/shot.py` | 本輪，要在你的電腦跑 |

改任何一章後，跑 `python3 work/trust-center-2026-10-08/tools/build_report.py` 重出 report.md 與 docx。

## 上一輪列的四件待辦，這一輪的狀態

1. 用 checklist.md 查 11 家競品：完成。雲端環境擋掉交易所網域，改用網頁搜尋讀各站網域上的頁面，讀不到的標「未驗證」。
2. 第一部分缺口逐項判斷：完成。25 項中 14 項需要做、8 項有條件再做、3 項暫不做。
3. 第二部分 Hub 架構、區塊、網址、入口、子頁優化、上線順序：完成。
4. 競品 Hub 截圖、轉繁中 docx：docx 完成；截圖這次的環境做不到，清單與腳本在 `tools/shots.sh`。

## 還沒做、要在本機做的

- 跑 `tools/verify_local.sh` 與 `tools/shots.sh`，補競品 security.txt、Hub 原始 HTML 與截圖。
- 依專案 CLAUDE.md 的交付規則，docx 定稿前跑一次 humanizer-zh-tw 潤稿（這次的環境沒有這個 skill）。
- 在 `Hotcoin/00-專案總控/document-manifest.json` 登記這份報告，並在 `SEO記憶/decisions-log.md` 記一筆。
- `tools/md2docx.py` 的修改確認沒問題後，可以併回 `腳本工具/md2docx.py`。
