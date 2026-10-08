# Coinbase 安全與信任內容盤點

讀取日期：2026-10-08。方式：WebSearch 限定 coinbase.com 網域（含 help.coinbase.com、status.coinbase.com）取回的搜尋摘要與頁面網址（下稱「搜尋」）。讀取限制：雲端環境網路政策擋掉 coinbase.com，無法直接開頁；Coinbase 是美國上市公司，信任證據的重心在 SEC 財報與州牌照，和離岸交易所結構不同。

| 編號 | 項目 | 結果 | 證據網址 | 頁上內容 | 讀取方式 |
|---|---|---|---|---|---|
| A1 | 關於我們頁 | 有 | coinbase.com/about | 公司介紹＋高管與董事名單 | 搜尋 |
| A2 | 法律實體全名與地址 | 有 | coinbase.com/legal/us、各地用戶協議 | 各地用戶協議寫明主體（Coinbase, Inc.、Coinbase Europe 等）；法律頁有郵寄地址 | 搜尋 |
| A3 | 管理團隊具名 | 有 | coinbase.com/about、investor.coinbase.com/governance/management | CEO Brian Armstrong、總裁兼 COO、CFO、法務長等具名；投資人關係另有管理層頁 | 搜尋 |
| A4 | 牌照／登記專頁 | 有 | coinbase.com/legal/licenses | 「Licenses」頁；託管子公司為 NYDFS 特許信託公司 | 搜尋 |
| A5 | 服務地區／受限國家 | 部分 | coinbase.com/legal/prohibited_use | 「Prohibited & Conditional Use Policy」列禁止行為與業務；可用國家清單未在本次確認 | 搜尋 |
| A6 | Media Kit／新聞室 | 有 | coinbase.com/press | press@coinbase.com；品牌素材含 logo、產品圖、高管照、介面截圖與 logo 使用規範 | 搜尋 |
| B1 | PoR 常駐頁 | 沒有（交易所整體） | coinbase.com/blog/how-crypto-companies-can-provide-proof-of-reserves | 以 SEC 審計財報替代 PoR；只有 cbBTC 等包裝資產有 PoR 頁 | 搜尋 |
| B2 | PoR 第三方審計 | 有（財報審計形式） | sec.gov 10-K | 年度財報經外部審計，審計師抽查冷錢包地址所有權 | 搜尋 |
| B3 | PoR 用戶自驗 | 沒有 | — | 無 Merkle 自驗 | 搜尋 |
| B4 | PoR 歷史快照 | 有（10-K／10-Q） | sec.gov | 每季財報揭露客戶託管資金 | 搜尋 |
| B5 | 用戶保護基金 | 沒有 | — | 無 SAFU 類基金 | 搜尋 |
| B6 | 冷錢包比例 | 未驗證 | coinbase.com/blog/how-we-keep-digital-assets-safe | 有寫冷錢包做法，數字本次未取回 | 搜尋 |
| B7 | 第三方保險 | 部分 | coinbase.com/prime/custody | 託管業務宣稱有商業犯罪保險，未列承保機構與額度；另警告「Coinbase 不賣保險產品」 | 搜尋 |
| B8 | 資產隔離聲明 | 有 | coinbase.com/security、10-K | 安全頁寫客戶資產 1:1、未經同意不出借；10-K 寫客戶法幣放在隔離帳戶 | 搜尋 |
| C1 | 安全中心 Hub | 有 | coinbase.com/security | 「Coinbase Security」頁，下有 /security/login-security 等子頁 | 搜尋 |
| C2 | 帳戶安全功能說明 | 有 | 同 C1＋說明中心 | 強制 2FA、安全金鑰／passkey、Vault 多重核准提幣、帳戶鎖定、外洩密碼偵測 | 搜尋 |
| C3 | 第三方安全認證 | 有 | coinbase.com/blog/…soc-1-and-soc-2… | 託管 SOC 1／SOC 2 Type II（Deloitte）、Prime SOC 1／2 Type 2、質押 SOC 2 Type 1；ISO 27001 未見 | 搜尋 |
| C4 | 滲透測試公開摘要 | 未驗證 | — | 搜尋未見 | 搜尋 |
| C5 | 漏洞賞金 | 有 | coinbase.com/whitehat | HackerOne；Critical 最高 1.5 萬、Extreme 最高 100 萬美元；鏈上另在 Cantina 最高 500 萬 | 搜尋 |
| C6 | security.txt | 未驗證 | — | 無法直接 GET；說明中心有〈如何揭露安全漏洞〉 | 搜尋 |
| C7 | 官方渠道驗證工具 | 部分 | help.coinbase.com/…/is-coinbase-present-on-social-media | 列官方社群帳號清單；無互動式查驗工具 | 搜尋 |
| C8 | 反詐騙教育專區 | 有 | help.coinbase.com/en/coinbase/privacy-and-security/avoid-scams | 說明中心「Avoid scams」分類，按詐騙類型逐篇 | 搜尋 |
| C9 | 安全事件歷史 | 有 | coinbase.com/blog/a-postmortem-of-our-may-7-2026-outage | 重大中斷發事後報告（2026-05-07、07-14） | 搜尋 |
| C10 | 系統狀態頁 | 有 | status.coinbase.com | 計畫內與計畫外中斷、可訂閱事件 | 搜尋 |
| D1 | 用戶協議 | 有 | coinbase.com/legal/user_agreement/united_states | 各地區一份 | 搜尋 |
| D2 | 隱私政策 | 有 | coinbase.com/legal/privacy | Global Privacy Policy | 搜尋 |
| D3 | Cookie 政策 | 有 | coinbase.com/legal/cookie | 獨立頁＋第三方 cookie 清單頁 | 搜尋 |
| D4 | 風險揭露總則 | 部分 | coinbase.com/legal/digital-asset-disclosures | Digital Asset Disclosures | 搜尋 |
| D5 | 分產品風險揭露 | 未驗證 | — | 本次未確認 | 搜尋 |
| D6 | AML／KYC 政策頁 | 未驗證 | — | 本次未確認 | 搜尋 |
| D7 | 執法機關請求入口 | 有 | help.coinbase.com/…/who-do-i-contact-for-a-subpoena-request… | Kodex 入口＋subpoenas@coinbase.com；民事文件寄登記代理人 | 搜尋 |
| D8 | Travel Rule 說明 | 未驗證 | — | 本次未確認 | 搜尋 |
| D9 | 上幣與下架標準 | 有 | coinbase.com/exchange/asset-listings、help…/asset-legal-review | 免費申請；法務、合規、技術安全三項核心審查；持續監控並可能下架 | 搜尋 |
| D10 | 市場監控／公平交易 | 未驗證 | — | 本次未確認 | 搜尋 |
| E1 | 費率表 | 有 | help.coinbase.com（費用說明） | 背景知識，本次未取回 | 背景知識 |
| E2 | 客服聯絡 | 有 | help.coinbase.com/…/coinbase-support | 說明中心與客服入口 | 搜尋 |
| E3 | 正式客訴流程 | 有 | help.coinbase.com/en/submit-a-complaint | 免費正式客訴：需客服案件號、45 個工作日內書面決定、可轉紐約 DFS；用戶協議規定仲裁前須先走此流程 | 搜尋 |
| E4 | 透明度／年度報告 | 有 | coinbase.com/blog/transparency-report-2025 | 年度透明度報告第 7 版（2024-10 至 2025-09），政府資料請求統計 | 搜尋 |

## F. Hub 結構

`/security` 是 Hub 雛形：主頁介紹帳戶保護與資產 1:1，子頁走 `/security/{主題}`（如 login-security）。法律文件集中在 `/legal/*`（licenses、prohibited_use、cookie、privacy、digital-asset-disclosures）。反詐內容放在說明中心的 Avoid scams 分類。

## 有特色、Hotcoin 做得到的做法

1. **正式客訴流程頁**：要求附客服案件號、寫明時限與外部申訴機構，並把「先走客訴」寫進用戶協議。Hotcoin 只差把時限與收件方式定下來。
2. **重大中斷的事後報告**：Hotcoin 已有系統狀態頁，可加上事後報告欄位，用事實取代「零事故」說法。
