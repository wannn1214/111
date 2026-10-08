# Binance 安全與信任內容盤點

讀取日期：2026-10-08。方式：WebSearch 限定 binance.com 網域取回的搜尋摘要與頁面網址（下稱「搜尋」）。讀取限制：本次雲端環境的網路政策擋掉 binance.com，無法直接開頁或 curl 原始 HTML；搜尋摘要多數來自 2023–2025 年的頁面，現況以 Jay 本機重驗為準。沒有直接證據的項目標「未驗證」，不寫「沒有」。

| 編號 | 項目 | 結果 | 證據網址 | 頁上內容 | 讀取方式 |
|---|---|---|---|---|---|
| A1 | 關於我們頁 | 有 | binance.com/en/about | 共同創辦人 CZ、何一具名；頂部導覽 About／Careers／Press／Community | 搜尋 |
| A2 | 法律實體全名與地址 | 部分 | binance.com/en/legal/licenses | 各地子公司全名列在牌照頁（Binance France SAS、Binance FZE、InvestbyBit Pty Ltd 等）；母公司註冊地未見官方說明 | 搜尋 |
| A3 | 管理團隊具名 | 有 | binance.com/en/blog/leadership/… | CEO Richard Teng 有官方簡介；合規團隊負責人具名；以部落格形式為主，非單一團隊頁 | 搜尋 |
| A4 | 牌照／登記專頁 | 有 | binance.com/en/legal/licenses | 「Licenses, Registrations and Other Legal Matters」：依地區→司法管轄區列主體、監管機關、登記編號（如法國 AMF E2022-037、阿根廷 CNV #76、澳洲 AUSTRAC DCE） | 搜尋 |
| A5 | 服務地區／受限國家 | 有 | binance.com/en/legal/list-of-prohibited-countries | 用戶條款連到「List of Prohibited Countries」；條款另點名古巴、伊朗、北韓、敘利亞、克里米亞 | 搜尋 |
| A6 | Media Kit／新聞室 | 有 | binance.com/en/press | Newsroom：公告、媒體素材；媒體信箱 pr@binance.com | 搜尋 |
| B1 | PoR 常駐頁 | 有 | binance.com/en/proof-of-reserves | 常駐頁＋2022-11 上線公告 | 搜尋 |
| B2 | PoR 第三方審計 | 沒有（現況） | — | 上線時說要找第三方審計；Mazars 2022 年底退出後改為 zk-SNARK 自證，學院文章主張「審計方證明仍需信任審計方」 | 搜尋＋背景知識 |
| B3 | PoR 用戶自驗 | 有 | binance.com/en/blog/tech/how-zksnarks-improve-… | Merkle tree＋zk-SNARK（2023-02 升級），驗證用戶餘額被計入且無負餘額帳戶 | 搜尋 |
| B4 | PoR 歷史快照 | 部分 | 同 B1 | 定期快照（資產數從 BTC 擴到 31 種，2023-11）；歷史列表的呈現方式未驗證 | 搜尋 |
| B5 | 用戶保護基金 | 有 | binance.com/en/support/faq/…safu… | SAFU，2018-07 成立；2024-04-18 為 10 億 USDC；申請期限 90 天；公開錢包地址未驗證 | 搜尋 |
| B6 | 冷錢包比例 | 部分 | binance.com/en/blog/all/Binance-Is-SAFU-7-Ways… | 寫有冷錢包，沒有比例數字 | 搜尋 |
| B7 | 第三方保險 | 沒有 | 同 B5 | 安全長公開說「沒有第三方保險比得上 SAFU」，以自有基金取代 | 搜尋 |
| B8 | 資產隔離聲明 | 未驗證 | — | 搜尋未見 | — |
| C1 | 安全中心 Hub | 未驗證 | binance.com/en/support/faq/c-7（Security FAQ 分類） | 未找到獨立安全 Hub；安全內容分散在 FAQ 分類與 blog/security | 搜尋 |
| C2 | 帳戶安全功能說明 | 有 | 說明中心 Security 分類 | 2FA、登入到期、即時安全通知、提幣反詐冷卻（最長 24 小時） | 搜尋 |
| C3 | 第三方安全認證 | 有 | binance.com/en/blog/compliance/…soc-2-audit… | SOC 2 Type II（A-LIGN 執行，2023-12）；ISO 27001／27701 限法國、阿聯、巴林、土耳其四地 | 搜尋 |
| C4 | 滲透測試公開摘要 | 未驗證 | — | 搜尋未見 | — |
| C5 | 漏洞賞金 | 有 | binance.com/en/support/articles/360036542051 | Bugcrowd（bugcrowd.com/binance），獎金以 BNB 支付，依影響分級 | 搜尋 |
| C6 | security.txt | 未驗證 | — | 無法直接 GET | — |
| C7 | 官方渠道驗證工具 | 有 | binance.com/en/official-verification | Binance Verify：可查網址、信箱、電話、微信、X、Telegram | 搜尋 |
| C8 | 反詐騙教育專區 | 部分 | binance.com/en/blog/security/… | 「Know Your Scam」系列、年度反詐退款報告；未見單一集中頁 | 搜尋 |
| C9 | 安全事件歷史 | 部分 | — | 2024 反詐退款年報（追回 910 萬美元）；2019 被盜事件由 SAFU 賠付的官方事後說明未在本次搜尋確認 | 搜尋 |
| C10 | 系統狀態頁 | 沒有（面向用戶） | developers.binance.com/…/system-status | 只有 API 狀態端點與維護公告 | 搜尋 |
| D1 | 用戶協議 | 有 | binance.com/en/terms | Terms of Use | 搜尋 |
| D2 | 隱私政策 | 有 | binance.com/en/about-legal/privacy-portal | Privacy Portal | 搜尋 |
| D3 | Cookie 政策 | 未驗證 | — | 搜尋未取回 | — |
| D4 | 風險揭露總則 | 有 | binance.com/en/risk-warning（條款中定義的 Risk Warning） | 條款定義「Risk Warning means the general risk warning published on the Website」 | 搜尋 |
| D5 | 分產品風險揭露 | 部分 | 各產品服務協議（如 Loans Service Agreement） | 分散在各產品協議與說明 | 搜尋 |
| D6 | AML／KYC 政策頁 | 部分 | binance.com/en/blog/community/playing-by-the-rules-… | 以部落格說明合規計畫（World-Check、即時與事後監控、鏈上制裁篩查）；未見正式政策頁 | 搜尋 |
| D7 | 執法機關請求入口 | 有 | binance.com/en/support/law-enforcement、/guidelines | LERS（Kodex）：只限政府機關、3 個工作日審核、保全 90 天、緊急案件標 Exigent | 搜尋 |
| D8 | Travel Rule 說明 | 未驗證 | — | 只在合規文章中提到名詞 | 搜尋 |
| D9 | 上幣與下架標準 | 未驗證 | — | 本次搜尋未取回；背景知識：有 Monitoring Tag 與定期下架審查公告 | 搜尋 |
| D10 | 市場監控／公平交易 | 未驗證 | — | 搜尋只見 AML 監控 | 搜尋 |
| E1 | 費率表 | 有 | binance.com/en/fee | 背景知識；本次未取回頁面 | 背景知識 |
| E2 | 客服聯絡 | 有 | binance.com/en/support/faq/how-to-contact-customer-support… | AI 助手轉真人、24 小時內回應、給工單號 | 搜尋 |
| E3 | 正式客訴流程 | 部分 | binance.com/en-BH/support/faq/complaints-policy… | 巴林主體有完整客訴政策：5 個工作日內給編號、28 天內書面最終回覆、可轉巴林央行；全球站未見同等頁 | 搜尋 |
| E4 | 透明度／年度報告 | 部分 | binance.com/en/blog/…year-of-compliance… | 年度合規回顧、反詐年報；無固定透明度報告頁 | 搜尋 |

## F. Hub 結構

未找到集中安全或信任 Hub。信任內容的入口分散：頂部導覽 About／Press，頁尾法律文件，Security FAQ 分類，blog/security 文章系列，PoR 與 Verify 各自獨立頁。

## 有特色、Hotcoin 做得到的做法

1. **牌照頁的「地區→司法管轄區→主體→機關→編號」格式**：Hotcoin 只有一筆 AUSTRAC，照同格式寫一列即可，日後新增登記直接加列。
2. **Binance Verify 支援多種管道查驗**（網址、信箱、電話、社群帳號）：Hotcoin 已有驗證工具，可對照補足查驗類型並把官方網域清單以文字輸出。
