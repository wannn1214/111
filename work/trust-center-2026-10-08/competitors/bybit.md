# Bybit 安全與信任內容盤點

讀取日期：2026-10-08。方式：WebSearch 限定 bybit.com 網域（含 learn.bybit.com、announcements.bybit.com）取回的搜尋摘要與頁面網址（下稱「搜尋」）。讀取限制：雲端環境網路政策擋掉 bybit.com，無法直接開頁。

| 編號 | 項目 | 結果 | 證據網址 | 頁上內容 | 讀取方式 |
|---|---|---|---|---|---|
| A1 | 關於我們頁 | 有 | bybit.com/en/promo/global/aboutus | 「About Bybit」頁，列出監管機關（含杜拜 VARA） | 搜尋 |
| A2 | 法律實體全名與地址 | 部分 | 風險揭露、條款 | 全球站由 Bybit Fintech Limited 發布；EEA 為 Bybit EU GmbH（維也納）；各主體分散在條款 | 搜尋 |
| A3 | 管理團隊具名 | 部分 | 新聞稿 | CEO 以新聞稿與活動露面；未確認集中團隊頁 | 搜尋 |
| A4 | 牌照／登記專頁 | 部分 | bybit.com/en/promo/global/aboutus、/learn/regulations/bybit-europe-eu-and-micar | 關於頁列監管機關；MiCA（奧地利 FMA，2025-05）、阿聯 SCA 完整牌照（2025-10）、VARA 為暫准非營運；未見逐列登記號的牌照總表 | 搜尋 |
| A5 | 服務地區／受限國家 | 有 | bybit.com/en/help-center/article/Service-Restricted-Countries | 美國、中國大陸、香港、新加坡、加拿大、北韓、古巴、伊朗等；法幣服務另有清單 | 搜尋 |
| A6 | Media Kit／新聞室 | 有 | bybit.com/en/press | Bybit Press 新聞室 | 搜尋 |
| B1 | PoR 常駐頁 | 有 | bybit.com/app/user/proof-of-reserve（背景知識）＋說明〈How to Verify the Assets in Your Account〉 | 常駐頁＋用戶自驗說明 | 搜尋 |
| B2 | PoR 第三方審計 | 有 | bybit.com/common-static/cht-static/por/Bybit_PoR_Audit_2026_Apr_22.pdf | Hacken 出具 PoR 審計報告：驗證錢包所有權（每個地址轉出小額）、審查 Merkle 生成程式碼、核對負債 | 搜尋 |
| B3 | PoR 用戶自驗 | 有 | 同 B1 | Merkle path；生成與驗證程式碼在 GitHub | 搜尋 |
| B4 | PoR 歷史快照 | 有 | common-static/cht-static/por/*.pdf | 每期一份 PDF（2024-06 起逐月可見），已發到第 29 次 | 搜尋 |
| B5 | 用戶保護基金 | 部分 | bybit.com/en/announcement-info/insurance-fund/ | 只有合約穿倉用的 Insurance Fund（有歷史頁）；不是帳戶資產保障基金 | 搜尋 |
| B6 | 冷錢包比例 | 部分 | bybit.com/en/promo/global/user-protection | 寫「用戶資金存放於離線冷錢包」、多簽、TEE、TSS；沒有比例 | 搜尋 |
| B7 | 第三方保險 | 未驗證 | — | 未見 | 搜尋 |
| B8 | 資產隔離聲明 | 未驗證 | — | 風險揭露寫「數位資產不受存款保險保障」；隔離聲明未見 | 搜尋 |
| C1 | 安全中心 Hub | 部分 | bybit.com/en/promo/global/user-protection | 「Bybit's Commitment to User Protection and Compliance」頁集中講冷錢包、漏洞賞金、合規；名稱不是安全中心 | 搜尋 |
| C2 | 帳戶安全功能說明 | 有 | 說明中心〈How to Enhance the Security of Your Account〉、〈Introduction to Bybit Protect〉 | Bybit Protect 三級保護、新地址提幣鎖 24 小時、安全交易核准 | 搜尋 |
| C3 | 第三方安全認證 | 部分 | bybit.com/en/press | 新聞稿標題寫 2026-09-29 完成 SOC 2 Type II；ISO 27001 未見 | 搜尋 |
| C4 | 滲透測試公開摘要 | 未驗證 | — | 搜尋未見 | 搜尋 |
| C5 | 漏洞賞金 | 有 | bybit.com/en/help-center/article/Bybit-Bug-Bounty-Program-T-C | Low 150–600 USDT 至 Critical 5,000–10,000 USDT；平台說法 HackerOne／Bugcrowd 不一 | 搜尋 |
| C6 | security.txt | 未驗證 | — | 無法直接 GET | — |
| C7 | 官方渠道驗證工具 | 有 | bybit.com/en/verification/ | 「Bybit Authenticity Check」：查電話、信箱、網址；頁上註明信箱寄件者可偽造，驗證結果不等於保證 | 搜尋 |
| C8 | 反詐騙教育專區 | 部分 | 說明中心〈How to Identify Phishing Threats and Avoid Common Scams〉等 | 分散文章；P2P 詐騙另有專文 | 搜尋 |
| C9 | 安全事件歷史 | 有 | bybit.com/en/learn/this-week-in-bybit/bybit-security-incident-timeline | 2025-02-21 冷錢包被盜約 15 億美元：時間線與 FAQ、第三方鑑識（Verichains、Sygnia）初步結論、72 小時內 PoR 回到 1:1、追回進度新聞稿 | 搜尋 |
| C10 | 系統狀態頁 | 部分 | bybit.com/en/announcement-info/deposit-withdraw/ | 各幣充提狀態頁；無整體可用性狀態頁 | 搜尋 |
| D1 | 用戶協議 | 有 | 說明中心 Platform Terms and Conditions | — | 搜尋 |
| D2 | 隱私政策 | 有 | 說明中心 | — | 搜尋 |
| D3 | Cookie 政策 | 未驗證 | — | 未取回 | 搜尋 |
| D4 | 風險揭露總則 | 有 | bybit.com/en/help-center/article/Bybit-Risk-Disclosure | Risk Disclosure Statement，2026-03-20 更新 | 搜尋 |
| D5 | 分產品風險揭露 | 部分 | 說明中心風險限額、預測市場 FAQ 等 | 另有哈薩克主體風險揭露 | 搜尋 |
| D6 | AML／KYC 政策頁 | 未驗證 | — | 本次未取回 | 搜尋 |
| D7 | 執法機關請求入口 | 部分 | 說明中心〈How to Report Stolen Assets〉 | 被盜資產申報流程（最長 12 小時回覆）；專用執法入口未見 | 搜尋 |
| D8 | Travel Rule 說明 | 未驗證 | — | 本次未取回 | 搜尋 |
| D9 | 上幣與下架標準 | 未驗證 | — | 本次未取回 | 搜尋 |
| D10 | 市場監控／公平交易 | 未驗證 | — | 本次未取回 | 搜尋 |
| E1 | 費率表 | 有 | bybit.com/en/help-center 費用說明 | 本次只見個別產品費用文章 | 搜尋 |
| E2 | 客服聯絡 | 有 | 說明中心〈How to Submit a Support Ticket〉 | 工單、即時客服 | 搜尋 |
| E3 | 正式客訴流程 | 未驗證 | — | 只見 P2P 申訴規則 | 搜尋 |
| E4 | 透明度／年度報告 | 部分 | 新聞稿 | 以新聞稿形式發布 PoR 與事件追回進度 | 搜尋 |

## F. Hub 結構

沒有名為安全中心的 Hub。`/promo/global/user-protection` 是一頁式「用戶保護與合規承諾」，集中講冷錢包技術、漏洞賞金與合規；PoR、Authenticity Check、說明中心安全文章各自獨立。

## 有特色、Hotcoin 做得到的做法

1. **安全事件時間線頁**：事件後用一頁寫時間線、影響範圍、第三方鑑識結論、儲備金恢復與後續追回，並持續更新。Hotcoin 不需要有事件才做，但 Hub 應預留「事件與公告」的位置與發布原則。
2. **驗證工具頁直說限制**（寄件者可偽造，驗證通過不等於保證）：誠實寫限制，Hotcoin 的官方渠道驗證頁可照做。
