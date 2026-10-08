# Hotcoin 安全與信任內容盤點

讀取日期：2026-10-08。方式：curl（Googlebot UA）取原始 HTML，搭配內部檔《平台外部信息管理-2.docx》（2026-09-28 提供）與既有調研。讀取限制：只看英文版 en_US；JS 載入後的內容未用瀏覽器全量確認。

| 編號 | 項目 | 結果 | 證據網址 | 頁上內容 | 讀取方式 |
|---|---|---|---|---|---|
| A1 | 關於我們頁 | 有 | /en_US/about/ | 2017 成立、810 萬用戶、120+ 國家地區、產品、安全措施、聯絡信箱 | curl |
| A2 | 法律實體全名與地址 | 部分 | 全站頁尾 | 頁尾版權行寫 Australian Hotcoin Global Exchange Pty Ltd；沒有註冊地址；用戶協議 1.1 寫 HOTCOIN TECHNOLOGY LLC；法律聲明寫塞舌爾法律 | curl＋09-29 條款查核 |
| A3 | 管理團隊具名 | 沒有 | /en_US/about/ | 09-09 決定本版不具名；/support/our-team/ 已 301 到 about | curl＋決策紀錄 |
| A4 | 牌照／登記專頁 | 沒有 | /en_US/legal/licenses/ 302 回首頁 | 關於我們頁有「Legal Entities, Registration Status & Service Regions」文字但沒有連結；Media Kit 寫「AUSTRAC (Australia) · FinCEN MSB (U.S.)」無編號 | curl |
| A5 | 服務地區／受限國家 | 有 | /en_US/support/Service-Regions/ | 09-30 版，列禁止與加強審查兩類國家及分類依據 | curl |
| A6 | Media Kit | 有 | /en_US/media-kit/ | 品牌素材、里程碑、排名、社群帳號；title 是站台通用文案 | curl |
| B1 | PoR 常駐頁 | 部分 | /en_US/reserve-fund/certificate/ | 頁面存在；原始 HTML 儲備率為「No Data」、快照要 JS 載入；無 canonical、hreflang，title 與 description 是站台通用文案 | curl |
| B2 | PoR 第三方審計 | 沒有 | 同上 | 頁上無審計機構；儲備資料經 CoinMarketCap 公布錢包 | curl＋內部檔 |
| B3 | PoR 用戶自驗 | 有 | 同上 | Merkle tree 自驗入口，驗證程式開源於 github.com/hotcoinexchange/proof-of-reserves | curl |
| B4 | PoR 歷史快照 | 未驗證 | 同上 | 有快照下拉選單元件，原始 HTML 無快照日期與數值 | curl |
| B5 | 用戶保護基金 | 部分 | /en_US/insurance-fund/ | 公開 9 個錢包地址（原始 HTML 可見）、涵蓋範圍；無基金總額與申請流程；頁內 H3 寫「Total Value of Reserve Assets Exceeds $137,000,000」混入儲備金數字；title 是站台通用文案 | curl |
| B6 | 冷錢包比例 | 部分 | /en_US/about/ | 寫「The vast majority of user assets are stored in offline cold wallets」與多簽，無比例數字 | curl |
| B7 | 第三方保險 | 沒有 | — | 未見任何保險描述 | curl |
| B8 | 資產隔離聲明 | 未驗證 | — | 用戶協議中文版未見「隔离」 | 09-29 條款文字 |
| C1 | 安全中心 Hub | 沒有 | /en_US/security/ 302 回首頁 | 關於我們頁寫「visit our Security & Trust Center」但沒有連結 | curl |
| C2 | 帳戶安全功能說明 | 部分 | /en_US/support/how-to-strengthen-the-account-security/ | 說明中心文章，5 個 H1；關於我們頁列出 2FA、防釣魚碼、白名單、裝置管理 | curl |
| C3 | 第三方安全認證 | 沒有 | — | 無 ISO 27001、SOC 2、CCSS | 內部檔 |
| C4 | 滲透測試公開摘要 | 沒有 | — | 內部有 HackenProof 2026-07-13 最終報告（含攻擊步驟，不可公開原文） | 內部檔 |
| C5 | 漏洞賞金 | 部分 | hackenproof.com/programs/hotcoin-web-and-mobile | 計畫存在（Critical 上限 $1,000）；hotcoin.com 任何頁面都沒有連到它 | 09-28 查核＋本次 grep |
| C6 | security.txt | 沒有 | /.well-known/security.txt | 回 200 但內容是首頁 HTML | curl |
| C7 | 官方渠道驗證工具 | 有 | /en_US/support/official-channel/ | 驗證工具存在；原始 HTML 無 H1、無官方網域文字清單 | curl |
| C8 | 反詐騙教育專區 | 部分 | /support/notice/hotcoin-official-clarification-... | 零散公告與 insider 子網域文章，沒有集中頁；09-18 審閱的 18 篇反詐與信任文章是否已上線未驗證 | curl＋09-18 審閱 |
| C9 | 安全事件歷史 | 沒有 | — | 社群文案寫「0 安全事故」，無範圍與期間 | 內部檔 |
| C10 | 系統狀態頁 | 有 | /en_US/status/ | title 正常 | curl |
| D1 | 用戶協議 | 有 | /en_US/support/user-agreement/ 與 ?code= 兩個網址 | 兩網址都自指 canonical，頁尾連參數版 | curl |
| D2 | 隱私政策 | 有 | /en_US/support/privacy-policy/ 與 ?code= | 同上 | curl |
| D3 | Cookie 政策 | 沒有 | /en_US/support/cookie-policy/ | 回 200 但是空殼（title 為「/」），屬 /support/ 軟 404 | curl |
| D4 | 風險揭露總則 | 有 | /en_US/support/legal-disclosures/（另有兩個參數網址） | 09-30 上線；自稱即用戶協議所稱《風險提示》；三個網址各自 canonical | curl |
| D5 | 分產品風險揭露 | 有 | 同上 | 現貨、盤前與 Alpha、合約、質押借幣、TradFi、跟單與網格、預測市場、P2P、理財、Web3 錢包、Card 共 11 類 | curl |
| D6 | AML／KYC 政策頁 | 部分 | /en_US/support/hotcoin-statement-on-anti-money-laundering-and-illegal-foreign-exchange-transactions/ | 聲明型公告，不是政策頁 | curl |
| D7 | 執法機關請求入口 | 部分 | 全站頁尾 | 只有信箱 casecn@hotcoin.com（Law Enforcement／Legal Assistance），沒有流程頁 | curl |
| D8 | Travel Rule 說明 | 沒有 | — | 內部檔記 2025-11 加入韓國 CODE VASP 聯盟，站上未見說明頁 | 內部檔 |
| D9 | 上幣與下架標準 | 沒有 | 頁尾 Listing Application 的 href 是 /en_US/ | 由 JS 開外部 Lark 文件 | curl |
| D10 | 市場監控／公平交易 | 部分 | /en_US/about/ | 關於我們頁一句「monitor unusual trading activity... guard against market manipulation」 | curl |
| E1 | 費率表 | 部分 | /en_US/rateStandard/index/ | 原始 HTML 無 H1、無費率數字、無 canonical | curl |
| E2 | 客服聯絡 | 有 | 全站頁尾、關於我們 | service、product、business、casecn、brand 五個信箱；Live Chat 由 JS 開啟 | curl |
| E3 | 正式客訴流程 | 沒有 | /en_US/complaint/ 302 | 用戶協議（英文版）處理時限寫「thirty (20) Business Days」，聯絡方式寫成「Service@ www.hotcoin.com/」（09-18 審閱） | curl＋09-18 審閱 |
| E4 | 年度／透明度報告 | 部分 | /en_US/campaign/annualReport/ | 2024 年報，無 H1、title 為站台通用文案；2026 版修改意見 09-28 已出 | curl |

## 技術面附帶發現

- `/{語言}/support/{任意字串}/` 一律回 200、title 為「/」、canonical 指向自己，是軟 404。隨機網址 `/en_US/support/zzq-random-test-8841/` 實測如此。
- 頁尾「Legal Notice」連 `?code=11675575085043713`；乾淨路徑 `/support/legal-description/` title 仍是「/」；另有 `/support/statement/`（2026）與 `/support/legal-statement/`（2019）兩份不同的法律聲明。
- 風險揭露頁尾文字為「Risk Disclosure」，頁面 H1 為「Hotcoin Legal Disclosures」，正文自稱「Risk Warning」，簡中 title 為「Hotcoin 风险提示」。
