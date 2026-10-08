# OKX 安全與信任內容盤點

讀取日期：2026-10-08。方式：WebSearch 限定 okx.com 網域取回的搜尋摘要與頁面網址（下稱「搜尋」）。讀取限制：本次雲端環境的網路政策擋掉 okx.com，無法直接開頁；OKX 依主體分多套頁面（全球、EEA、US、TR、AU、SG），本檔以全球站 en-us 為主。

| 編號 | 項目 | 結果 | 證據網址 | 頁上內容 | 讀取方式 |
|---|---|---|---|---|---|
| A1 | 關於我們頁 | 有 | okx.com/about（說明中心頁尾 About us） | 本次未開到頁面內容 | 搜尋 |
| A2 | 法律實體全名與地址 | 有 | okx.com/en-us/help/terms-of-service | 條款逐一列出服務主體：Aux Cayes FinTech Co. Ltd（塞舌爾，一般用戶）、OKX Europe Limited（馬爾他）、OKX INC.（美國）、OKX Bahamas、OKX Brazil、OKX Singapore 等，依居住地決定 | 搜尋 |
| A3 | 管理團隊具名 | 有 | okx.com/en-us/learn/bolstering-leadership-…、/okx-global-chief-risk-officer | 創辦人兼 CEO 徐明星；全球合規長、風險長、調查主管、各地 CEO、董事皆具名，以 Learn 文章發布 | 搜尋 |
| A4 | 牌照／登記專頁 | 部分 | okx.com/en-us/help/us-licenses、/learn/our-mica-license | 美國牌照頁（NMLS# 1767779、FinCEN MSB，2026-09-15 更新）；MiCA 由馬爾他 MFSA 核發（2025-01-27）；未見全球單一牌照總表 | 搜尋 |
| A5 | 服務地區／受限國家 | 有 | okx.com/en-us/help/risk-compliance-disclosure | 「Risk & Compliance Disclosure」列受限地區（阿富汗、加拿大、古巴、香港、伊朗、印度、日本、馬來西亞等）；各主體清單不一致 | 搜尋 |
| A6 | Media Kit／新聞室 | 未驗證 | — | 搜尋未找到媒體素材頁 | 搜尋 |
| B1 | PoR 常駐頁 | 有 | okx.com/en-us/proof-of-reserves | 月度報告，第 47 次（2026-09）主要資產 274 億美元，22 種幣 | 搜尋 |
| B2 | PoR 第三方審計 | 有 | okx.com/en-us/learn/okx-proof-of-reserves-27 | 自第 27 次（2025-01）起由 Hacken 驗證，涵蓋 65 萬個錢包地址 | 搜尋 |
| B3 | PoR 用戶自驗 | 有 | 同 B1 | Merkle tree → zk-STARK（2023-04 起），GitHub 開源驗證工具可本機執行 | 搜尋 |
| B4 | PoR 歷史快照 | 有 | okx.com/en-br/proof-of-reserves/download | 下載頁逐月列出 zk-STARK v2 準備金與負債檔；Learn 每月一篇「第 N 次 PoR」 | 搜尋 |
| B5 | 用戶保護基金 | 部分 | okx.com/en-us/learn/is-okx-safe | Learn 文章寫有「Security Fund」，名稱與規模說法不一；OKX Shield 有條款頁 | 搜尋 |
| B6 | 冷錢包比例 | 有 | 同 B5 | 「over 95% of client funds」在冷錢包、多簽多把獨立金鑰 | 搜尋 |
| B7 | 第三方保險 | 未驗證 | — | 搜尋未見承保機構 | 搜尋 |
| B8 | 資產隔離聲明 | 部分 | SG 主體 safeguarding disclosures | 新加坡主體依 MAS 要求有資產保管揭露；全球站未驗證 | 搜尋 |
| C1 | 安全中心 Hub | 部分 | okx.com/en-us/protect、web3.okx.com/security | 「OKX Protect」頁集中介紹安全；錢包另有安全頁 | 搜尋 |
| C2 | 帳戶安全功能說明 | 有 | 說明中心 | 防釣魚碼、官方信箱網域清單、客服只用 App 內語音 | 搜尋 |
| C3 | 第三方安全認證 | 有 | okx.com/en-us/learn/iso-27001-csa-okx、/okx-soc-1-type-2 | ISO/IEC 27001:2022（BSI 驗證）、CSA STAR Level 1、SOC 2 Type 2（2023-09 宣布）、巴哈馬主體 SOC 1 Type 2 | 搜尋 |
| C4 | 滲透測試公開摘要 | 未驗證 | — | 搜尋未見 | 搜尋 |
| C5 | 漏洞賞金 | 有 | okx.com/en-us/threat-hunters、/help/bug-bounty-learn-more | 自營計畫，五級，最高 100 萬 USDT；累計發放 230 萬美元 | 搜尋 |
| C6 | security.txt | 未驗證 | — | 無法直接 GET | — |
| C7 | 官方渠道驗證工具 | 有 | okx.com/en-us/support-center/channel-verification | 選渠道類型貼上連結或帳號查真偽；說明頁列官方信箱網域 | 搜尋 |
| C8 | 反詐騙教育專區 | 部分 | okx.com/en-us/learn/crypto/crypto-scams-guide 與多篇說明 | App 內 Security → Community safety 可舉報；文章分散 | 搜尋 |
| C9 | 安全事件歷史 | 部分 | okx.com/en-us/help/okx-official-announcement-reopening-of-withdrawals… | 2020 年提幣暫停的官方公告仍在；無集中事件紀錄頁 | 搜尋 |
| C10 | 系統狀態頁 | 有 | okx.com/en-us/status | 維護資訊、問題描述、各幣充提狀態（UTC+8） | 搜尋 |
| D1 | 用戶協議 | 有 | okx.com/en-us/help/terms-of-service | 各主體各一份 | 搜尋 |
| D2 | 隱私政策 | 有 | okx.com/en-us/help/privacy-policy-statement-eea 等 | 依主體分版 | 搜尋 |
| D3 | Cookie 政策 | 部分 | 隱私聲明內 cookie 段＋Cookie Preference Centre | 未見獨立 cookie 頁 | 搜尋 |
| D4 | 風險揭露總則 | 有 | okx.com/en-us/help/risk-compliance-disclosure | 2026-07-08 更新；併談風險、制裁、AML 計畫、受限地區 | 搜尋 |
| D5 | 分產品風險揭露 | 有 | 各產品協議（永續合約、Web3、借貸） | 分產品協議內寫風險 | 搜尋 |
| D6 | AML／KYC 政策頁 | 有 | 同 D4 | AML／CTF／制裁計畫寫在 Risk & Compliance Disclosure 內：風險為本、篩查名單、可疑交易申報、保存五年 | 搜尋 |
| D7 | 執法機關請求入口 | 有 | okx.com/en-us/help/okx-law-enforcement-request-guide | Kodex 入口＋enforcement@okx.com；2024 年收 34,583 件請求 | 搜尋 |
| D8 | Travel Rule 說明 | 有 | okx.com/en-gb/help/travel-rule-faqs、/travel-rule-faq-eea | EEA 2024-12-30 起；超過 1,000 歐元驗證私人錢包 | 搜尋 |
| D9 | 上幣與下架標準 | 部分 | okx.com/en-us/help/okx-margin-futures-perpetual-swap-delisting-process-standards | 衍生品下架流程標準公開（提前 7 天公告）；現貨下架引用內部準則未公開 | 搜尋 |
| D10 | 市場監控／公平交易 | 未驗證 | — | 搜尋未見 | 搜尋 |
| E1 | 費率表 | 有 | okx.com/fees（各地區 Trading Fees 頁） | 依地區分費率表 | 搜尋 |
| E2 | 客服聯絡 | 有 | okx.com/en-us/contact-us | 聯絡頁＋App 內客服 | 搜尋 |
| E3 | 正式客訴流程 | 有 | okx.com/en-us/help/formal-complaint-handling-process（EEA）等 | 各主體一頁：EEA 5 個工作日確認、15 個工作日最終回覆、可轉馬爾他金融仲裁；AU 可轉 AFCA | 搜尋 |
| E4 | 透明度／年度報告 | 部分 | okx.com/en-us/learn/okx-australia-responsiblity-report | 澳洲主體 2025-03 首份 Responsibility Report；月度 PoR | 搜尋 |

## F. Hub 結構

沒有單一信任中心。最接近的是「OKX Protect」（/protect）與 Learn 文章〈Is OKX Safe?〉，後者把 PoR、冷錢包、安全基金、第三方審計集中在一篇回答「安不安全」的文章裡。說明中心頁尾列 About us、Careers、Contact us、Whistleblower notice、Law enforcement。

## 有特色、Hotcoin 做得到的做法

1. **〈Is OKX Safe?〉這種直接回答品牌疑問的頁面**：用品牌問句當標題，把各信任證據集中後連回原頁。Hotcoin 的 GSC 正好有 is hotcoin safe／legit 的曝光。
2. **PoR 下載頁逐月列出歷史檔案**：Hotcoin 已有快照下拉元件，改成原始 HTML 可見的歷史列表即可。
