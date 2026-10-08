# Kraken 安全與信任內容盤點

讀取日期：2026-10-08。方式：WebSearch 限定 kraken.com 網域（含 support.kraken.com、blog.kraken.com、trust.kraken.com、status.kraken.com）取回的搜尋摘要與頁面網址（下稱「搜尋」）。讀取限制：雲端環境網路政策擋掉 kraken.com，無法直接開頁；部分快照年代較舊，SOC 2 類型在不同頁說法不一。

| 編號 | 項目 | 結果 | 證據網址 | 頁上內容 | 讀取方式 |
|---|---|---|---|---|---|
| A1 | 關於我們頁 | 有 | kraken.com/about | 本次未取回內容 | 搜尋 |
| A2 | 法律實體全名與地址 | 有 | kraken.com/legal/disclosures、各地條款 | 各地主體與牌照逐列；客訴信可寄杜拜客訴部 | 搜尋 |
| A3 | 管理團隊具名 | 部分 | kraken.com/press/releases/… | 高管任命以新聞稿發布（CEO Dave Ripley、CFO、CTO 等）；未確認有集中團隊頁 | 搜尋 |
| A4 | 牌照／登記專頁 | 有 | kraken.com/legal/disclosures、/learn/how-kraken-is-regulated、support…/where-is-kraken-licensed-or-regulated | 美國各州 MTL 逐州列牌照號與監管機關；MiCA（愛爾蘭央行）、MiFID（CySEC）、FinCEN MSB、懷俄明 SPDI 銀行執照 | 搜尋 |
| A5 | 服務地區／受限國家 | 有 | 背景知識：kraken.com/legal/restricted-territories | 本次搜尋未直接取回，標背景知識 | 背景知識 |
| A6 | Media Kit／新聞室 | 有 | kraken.com/press/kraken-images、/press/releases | 產品截圖下載、logo 與高管照經媒體信箱索取 | 搜尋 |
| B1 | PoR 常駐頁 | 有 | kraken.com/proof-of-reserves | 常駐頁；最新快照 2025-12-31 | 搜尋 |
| B2 | PoR 第三方審計 | 有 | blog.kraken.com/news/december-2025-proof-of-reserves | The Network Firm 依 AICPA 執行商定程序（早期為 Armanino）；Kraken 自己註明「PoR 審計沒有法定定義」 | 搜尋 |
| B3 | PoR 用戶自驗 | 有 | 同 B1 | 每位用戶發個人 Merkle proof | 搜尋 |
| B4 | PoR 歷史快照 | 有 | blog.kraken.com（2023-11、2024、2025-03、09、12） | 由半年一次改為每季，每次一篇公告 | 搜尋 |
| B5 | 用戶保護基金 | 沒有 | — | 未見 | 搜尋 |
| B6 | 冷錢包比例 | 部分 | kraken.com/features/security | 冷熱錢包並用、機房 24 小時武裝警衛監控；未見比例數字 | 搜尋 |
| B7 | 第三方保險 | 未驗證 | — | 未見 | 搜尋 |
| B8 | 資產隔離聲明 | 有 | 同 B1 | PoR 寫 1:1 以上；美國揭露頁寫「非 FDIC／SIPC 保障」 | 搜尋 |
| C1 | 安全中心 Hub | 有 | kraken.com/features/security、trust.kraken.com | 安全頁＋獨立 Trust Center（文件下載型） | 搜尋 |
| C2 | 帳戶安全功能說明 | 有 | 同 C1 | FIDO2／passkey 2FA、不提供簡訊找回帳戶、API 權限、新提幣地址郵件確認、全域設定時間鎖 | 搜尋 |
| C3 | 第三方安全認證 | 有 | trust.kraken.com | ISO/IEC 27001:2022、SOC 2 Type 1／2、SOC 3、PCI DSS v4.0.1、CCSS | 搜尋 |
| C4 | 滲透測試公開摘要 | 有 | trust.kraken.com | Trust Center 文件區列「pentest report」（需申請下載） | 搜尋 |
| C5 | 漏洞賞金 | 有 | kraken.com/features/security/bug-bounty | 自營計畫，Critical 10 萬–150 萬美元，以 BTC 支付；1 個工作日確認、10 個工作日分級；善意研究不追訴 | 搜尋 |
| C6 | security.txt | 未驗證 | — | 無法直接 GET；安全頁列漏洞揭露政策與 PGP 金鑰 | 搜尋 |
| C7 | 官方渠道驗證工具 | 部分 | support.kraken.com/articles/is-this-email-from-kraken | 〈這封信是 Kraken 寄的嗎〉、驗證來電的功能；官方 App 發行者為 Payward, Inc. | 搜尋 |
| C8 | 反詐騙教育專區 | 有 | support.kraken.com（11 種詐騙）、blog Scam Awareness Week | 說明中心列 11 種詐騙；年度反詐週 | 搜尋 |
| C9 | 安全事件歷史 | 部分 | blog.kraken.com/product/security/kraken-bug-bounty-program-patches-isolated-bug | 公開揭露被研究員利用的入金漏洞事件 | 搜尋 |
| C10 | 系統狀態頁 | 有 | status.kraken.com | 各元件狀態、可訂閱、有 API | 搜尋 |
| D1 | 用戶協議 | 有 | kraken.com/legal/global-terms、/legal/eea-terms | 依地區分版 | 搜尋 |
| D2 | 隱私政策 | 有 | kraken.com/legal/privacy | 另有美國版 | 搜尋 |
| D3 | Cookie 政策 | 有 | kraken.com/legal/cookies | 獨立頁＋頁尾 Cookie Settings | 搜尋 |
| D4 | 風險揭露總則 | 有 | kraken.com/legal/disclosures | Legal Disclosures 併入條款 | 搜尋 |
| D5 | 分產品風險揭露 | 部分 | 衍生品、經紀等各自協議 | 本次未逐一確認 | 搜尋 |
| D6 | AML／KYC 政策頁 | 有 | kraken.com/compliance | Compliance Hub：AML／CFT 主題 | 搜尋 |
| D7 | 執法機關請求入口 | 部分 | support.kraken.com/articles/how-do-i-submit-a-legal-inquiry | 法律查詢入口；本次未找到專用執法入口頁 | 搜尋 |
| D8 | Travel Rule 說明 | 有 | support.kraken.com/articles/updates-to-crypto-transfer-procedures-… | EU／UK／AU／CA 各一篇；超過 1,000 歐元驗證私人錢包、Satoshi test | 搜尋 |
| D9 | 上幣與下架標準 | 有 | kraken.com/get-listed、support…/asset-delistings-* | 上幣五步驟與評估面向；每月下架公告寫明觸發條件與時程 | 搜尋 |
| D10 | 市場監控／公平交易 | 有 | kraken.com/compliance/market-integrity | Compliance Hub 下的 Market Integrity 頁 | 搜尋 |
| E1 | 費率表 | 有 | kraken.com/features/fee-schedule | 08-18 規劃文件已引用為樣板 | 既有調研 |
| E2 | 客服聯絡 | 有 | kraken.com/features/24-7-support | 24/7 客服 | 搜尋 |
| E3 | 正式客訴流程 | 有 | support.kraken.com/articles/complaint-handling-process | 表單／信箱／工單／郵寄；5 個工作日確認、15 個工作日回覆；依地區列外部申訴機構（AFCA、OBSI、FOS、VARA 等） | 搜尋 |
| E4 | 透明度／年度報告 | 有 | blog.kraken.com/compliance/2025-transparency-report | 年度透明度報告（2025 版：7,957 件政府請求、74 國） | 搜尋 |

## F. Hub 結構

Kraken 是本次唯一把「信任」拆成三個 Hub 的交易所：

1. **安全頁** `/features/security`：開場「Protecting your funds and privacy is our number one objective」→ Security Labs → 安全團隊 → Proof of Reserves → 託管安全 → 資訊安全（ISO 27001、SOC 2）→ 安全測試與漏洞賞金 → 帳戶安全功能清單 → 安全資源（帳戶指南、漏洞賞金、揭露政策、PoR 流程、PGP 金鑰）。子頁放在 `/features/security/*`（bug-bounty、kraken-security-labs）。
2. **Trust Center** `trust.kraken.com`：第三方平台型文件中心。概覽→合規標章列（CCSS、GDPR、ISO 27001、PCI DSS、SOC 2/3）→文件下載（報告、證書、應用安全、政策）→主題清單。
3. **Compliance Hub** `/compliance`：AML／CFT、Market Integrity 等合規主題。

## 有特色、Hotcoin 做得到的做法

1. **安全頁最後一個「安全資源」區塊**：把漏洞揭露政策、PGP 金鑰、PoR 流程、帳戶指南列成連結清單。Hotcoin 的 Hub 收尾也可以這樣做，成本只是一組連結。
2. **PoR 公告直說方法限制**（「PoR 沒有法定定義」、商定程序不是審計意見）：Hotcoin 沒有第三方審計，照實寫方法與限制，比寫「100% 安全」更能過評分指南「獨立來源為準」的檢驗。
