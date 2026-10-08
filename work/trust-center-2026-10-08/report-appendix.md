## 附錄 A：38 項對照矩陣

● 有　◐ 部分　○ 沒有　? 未驗證（讀不到，不等於沒有）。「頭部」與「同級」兩欄是有或部分的家數，只當參考。每格的證據網址與頁上原文在 `work/trust-center-2026-10-08/competitors/` 各家檔案裡。

<!-- include-table: matrix.md -->

## 附錄 B：Google Ads 與 Google Play 的加密政策

本報告只看自然搜尋（10-08 你的選擇）。這裡說明為什麼 Ads 與 Play 的規定不能直接拿來當自然搜尋標準，以及它們跟 Hotcoin 的關係。

- **自然搜尋**：沒有任何加密貨幣網站認證或牌照要求。Google 用評分指南與實用內容指南定義什麼是可信的結果，第一章已整理。
- **Google Ads**：交易所、軟體錢包要先申請 Google 認證，並在投放國家持有當地牌照或登記。名單上的國家包括美國（FinCEN MSB 登記加各州貨幣傳輸牌照，或銀行執照）、英國（FCA 登記）、歐盟（MiCA CASP 授權）、加拿大、香港、日本、韓國、泰國、阿聯等。2026-05 起改在 Ads 帳戶內申請。
- **Google Play**：交易所與託管型錢包 App 要在 Play Console 的金融功能聲明中逐國申報，名單國家的要求與 Ads 大致相同；沒有對應牌照的國家要從發布範圍拿掉。

**和 Hotcoin 的關係**：Hotcoin 目前能確認的只有澳洲 AUSTRAC 登記，而澳洲不在 Ads 與 Play 的名單上；美國只有 FinCEN MSB（兩筆主體還對不上），沒有州牌照，達不到美國的要求。所以 Ads 這條路目前走不通，這不影響自然搜尋。Play 的發布國家是否合規，建議另外請產品對照 Play Console 的聲明，不在這份報告範圍內。

資料來源：Google Ads 政策說明〈Cryptocurrencies and related products〉與 2025-07、2025-09、2026-08 更新公告；Play Console 說明〈Understanding Google Play's Cryptocurrency Exchanges and Software Wallets Policy〉。2026-10-08 以網頁搜尋讀取 support.google.com，部分表格擷取不完整，引用前以官方頁面為準。

## 附錄 C：資料來源與讀取限制

**Hotcoin**：2026-10-08 以 curl（Googlebot UA）取原始 HTML，只看英文版，JS 載入後的內容未用瀏覽器全量確認。內部資料取自《平台外部信息管理-2.docx》（09-28）、HackenProof 滲透測試報告（07-13）、09-18 信任內容審閱與 09-29 條款查核。

**競品**：2026-10-08 以網頁搜尋限定各站網域讀取。這次的雲端環境擋掉交易所網域，所以：

1. 沒有一家能直接抓原始 HTML，看不到「內容是否直出」「JSON-LD 類型」這兩項，原本規劃的 F 段 Hub 結構只能寫到區塊順序與子頁網址。
2. security.txt（C6）11 家都無法 GET，全部標「未驗證」。
3. 多數搜尋摘要來自 2023 至 2026 年的頁面快照，現況可能已改。
4. 競品 Hub 截圖未能在這次環境產出。

**本機補驗**：`work/trust-center-2026-10-08/tools/verify_local.sh` 在你的電腦上跑，會對 11 家的 security.txt 與 Hub 頁做只讀 GET，輸出狀態碼、title、H1 與 canonical；`tools/shots.sh` 列出要截圖的 12 個競品頁面，沿用 `腳本工具/shot.py`。補完後附錄 A 的「未驗證」會變少，預期第二章的判斷不會因此改變。最值得先補的是：

| 項目 | 為什麼值得補 |
|---|---|
| 各家 security.txt | 確認 C6 是否真的是業界常態，這次 11 家全部讀不到 |
| Coinbase `/security`、Kraken `/features/security`、OKX `/protect`、Toobit `/safety`、BTCC `/btcc-security`、Bybit `/promo/global/user-protection` 的原始 HTML 與截圖 | Hub 區塊設計的直接參考，也是給產品看的截圖 |
| Bitget、Binance 是否有安全 Hub | 這次搜尋都找不到，可能只是沒被搜到 |
| Biconomy 全部項目 | 頁面是 JS 單頁，搜尋幾乎沒收錄 |

**GSC**：連線工具這次沒接上，用 09-10 匯出的 2026-08-10 至 09-06 快照（網頁搜尋、final 資料、查詢×頁面）。

**評分指南**：《搜尋品質評分員指南》2025-09-11 版繁中譯本（專案根目錄 searchqualityevaluatorguidelines-zh-TW.md）；Search Central〈建立實用、可靠、以人為本的內容〉2026-10-05 更新版。
