## 三、第二部分：安全與信任中心怎麼做

這一章的順序照你要求的：先盤點有哪些內容和資料（3.1），再定架構（3.2）和 Hub 頁面（3.3），然後是既有頁怎麼接進來（3.4）、入口（3.5）、技術規格（3.6）、上線順序（3.7）和驗收（3.8）。

<!-- include: report-part3-inventory.md -->

### 3.2 架構：一個 Hub，加 6 個新子頁，既有頁不搬家

**建議**：新建一個 Hub，底下只放新做的子頁；已經上線的 10 幾頁留在原網址，由 Hub 連出去，各頁再連回 Hub。

```
/{語言}/trust/                        安全與信任中心（Hub）
├─ /trust/vulnerability-disclosure/   漏洞回報          新｜第一批
├─ /trust/anti-scam/                  防詐騙與官方網域   新｜第一批
├─ /trust/legal-entities/             法律實體與登記     新｜第二批
├─ /trust/complaints/                 客訴與申訴         新｜第二批
├─ /trust/law-enforcement/            執法機關請求指引   新｜第二批
└─ /trust/aml-kyc/                    反洗錢與身分驗證   新｜第三批

既有頁，網址不動，由 Hub 連出：
  /about/  /reserve-fund/certificate/  /insurance-fund/  /support/Service-Regions/
  /support/legal-disclosures/  /support/official-channel/  /status/  /media-kit/
  /rateStandard/index/  /campaign/annualReport/  用戶協議  隱私政策

/.well-known/security.txt  → 指向 /trust/vulnerability-disclosure/
/{語言}/security/          → 301 到 /{語言}/trust/（現在是 302 回首頁）
```

**為什麼既有頁不搬**：儲備金、保護基金、風險揭露、服務地區這幾頁是 09-16 到 09-30 才上線的，頁尾 09-28 才改好。現在搬家要做轉址、重新等收錄，換來的只是網址整齊。Hub 的作用靠連結就做得到，不需要網址層級。

**為什麼不做成一頁**：法律實體、客訴、執法請求、漏洞回報各自的讀者和問題不同，塞進一頁會讓 Hub 變成條款大全，搜「hotcoin complaints」的人也找不到流程。08-18 規劃定過「每頁只處理一個主要任務」，這裡照用。

**為什麼不拆更多頁**：平台安全、帳戶安全、儲備金摘要直接放在 Hub 上。這幾塊單獨成頁會和 Hub 搶同一批「is hotcoin safe」「hotcoin security」查詢。

**每頁承接什麼**：

| 頁面 | 承接的查詢（GSC 08-10 至 09-06） | 讀者 |
|---|---|---|
| Hub | is hotcoin safe（9.6）、is hotcoin legit（7.6）、hotcoin security（8.9）、hotcoin scam（18.6） | 正在考慮要不要用 Hotcoin 的人 |
| 法律實體與登記 | hotcoin license（9.2）、hotcoin regulated（8.3）、what is the company name for hotcoin.com、hotcoin owner | 想知道誰在營運、受誰登記的人，以及 AI 與資料平台 |
| 防詐騙與官方網域 | hotcoin official website（14.4）、冒牌網站相關 | 正在懷疑訊息或網站真假的人 |
| 客訴與申訴 | hotcoin complaints（6.6）、hotcoin withdrawal problems（9.1） | 已經遇到問題的用戶 |
| 漏洞回報 | — | 資安研究者 |
| 執法機關請求指引 | — | 執法與監管機關 |
| 反洗錢與身分驗證 | hotcoin kyc 等 | 註冊前查合規的人 |

括號是平均排名。這些查詢現在大多落在首頁或 insider 子網域。

**和既有頁的分工**：關於我們頁寫公司事實，Hub 寫安全證據，insider 品牌故事寫敘事。三頁的 title 與 H1 不重複用同一組字，延續 09-09「insider 與關於頁不得同時用合規加品牌名」的規則。

**網址用 /trust/ 還是 /security/**：我建議 `/trust/`。子頁有法律實體和客訴，放在 `/security/` 底下不貼切。這一題列在第四章請你決定。如果 09-03 法律實體頁需求已經定了網址，以已定的為準。

### 3.3 Hub 頁面：區塊與順序

Hub 的名稱用關於頁已經寫出去的「Security & Trust Center」，中文「安全與信任中心」。title 建議：`Security & Trust Center | Hotcoin`，H1：`Hotcoin Security & Trust Center`。

| 順序 | 區塊 | 放什麼 | 連到哪裡 | 第一批能上嗎 |
|---|---|---|---|---|
| 0 | 開頭 | H1 下兩到四句：2017 年成立、旗下 Australian Hotcoin Global Exchange Pty Ltd 已在 AUSTRAC 登記、用戶資產怎麼保護（儲備金證明、保護基金）、本頁最後更新日 | — | 能；合約主體定案前只寫登記事實，不寫「由某公司營運」，免得和用戶協議打架 |
| 1 | 重點事實表 | 成立年份；已登記主體與 AUSTRAC 登記號（連 AUSTRAC 查詢頁）；最新儲備金快照日與儲備率；保護基金規模與日期；最近一次第三方滲透測試期間。每列附資料日期 | 各證據頁 | 部分能；保護基金規模、測試摘要要等財務與 Owen |
| 2 | 資產透明 | 儲備金證明怎麼算、怎麼自己驗、限制是什麼；保護基金涵蓋什麼、不涵蓋什麼 | 儲備金頁、保護基金頁 | 能 |
| 3 | 平台安全 | 託管方式（冷熱錢包分離、多簽）、基礎設施防護（DDoS、WAF、零信任，取自關於頁）、第三方滲透測試摘要、漏洞回報 | 漏洞回報頁 | 能；測試摘要待 Owen 確認複測 |
| 4 | 帳戶安全 | 2FA、防釣魚碼、提幣白名單、裝置管理、提幣鎖定，每項一句話加連結 | 說明中心各篇 | 能 |
| 5 | 防詐騙 | 唯一官方網域、驗證工具、Hotcoin 不會做的事（不會私訊要求轉帳、不會要求助記詞；有沒有電話客服待確認）、常見詐騙類型 | 防詐騙頁、官方渠道驗證頁 | 能 |
| 6 | 合規與法律文件 | 法律實體與登記、服務地區、風險揭露、用戶協議、隱私政策、反洗錢與身分驗證 | 各頁 | 能；法律實體頁第二批上線前先連服務地區 |
| 7 | 求助管道 | 客服管道與時間、客訴流程、執法請求 | 客服、客訴頁、執法頁 | 部分；客訴與執法頁第二批 |
| 8 | 透明度 | 年度報告、系統狀態、事件通報原則（出事時在哪裡、多久內通知、會公布什麼） | 年報、狀態頁 | 能 |
| 9 | 常見問題 | 6 到 7 題，每題兩三句加連結：Hotcoin 安全嗎、有沒有受監管、誰在營運、資產放在哪、平台被駭怎麼辦、有沒有保險、怎麼確認官方管道 | 各證據頁 | 能 |
| 10 | 安全資源 | security.txt、漏洞回報、驗證工具、系統狀態，加最後更新日 | — | 能 |

**寫法規則**（取自 08-18 規劃與知識庫的 YMYL 口徑，給內容負責人）：

1. 每一句信任主張都要連到能查證的地方：監管登記庫、鏈上地址、報告或站內證據頁。
2. 不寫「絕對安全」「零風險」「100% 安全」。「100% 儲備」要附定義和快照日。
3. 寫 registration 不寫 license，沒有的資格不包裝成受監管。
4. 數字標日期，和來源頁一致。用戶數、國家數統一前不放。
5. 常見問題的答案和證據頁內容不能有出入，改一邊要同步改另一邊。

**區塊順序的理由**：評分指南要的是「誰負責」和「出事找得到人」，所以重點事實表和主體資訊放最前面。GSC 裡那批 AI 問句（公司名稱、成立年份、客服電話）要的也是這一層的答案。產品安全細節放在中段。

### 3.4 既有頁怎麼接進來、各自要修什麼

這些頁面已經上線或已拍板。照你的指示，放進架構並寫出需要優化的地方，不重寫已拍板的文案。多數問題已經寫在既有需求裡，這裡只彙整並標出還沒修的。

| 頁面 | Hub 裡的位置 | 要修什麼（2026-10-08 實測） | 既有需求 | 誰 |
|---|---|---|---|---|
| 關於我們 `/about/` | 開頭、合規 | 正文「Security & Trust Center」與「Legal Entities, Registration Status & Service Regions」兩段文字補上連結；麵包屑與頁尾「關於我們」錯譯（09-30 決定暫緩，待重啟） | 关于我们页验收修改需求 09-30 | 前端 |
| 儲備金證明 `/reserve-fund/certificate/` | 資產透明 | 原始 HTML 儲備率為「No Data」、快照要 JS 才出現；沒有 canonical、hreflang；title 與 description 是站台通用文案；歷史快照要以列表輸出；補方法與限制；連到 CoinMarketCap 公布的錢包 | 储备金页SEO需求 09-03 | 前端＋財務 |
| 用戶保護基金 `/insurance-fund/` | 資產透明 | title 是站台通用文案；頁內 H3「Total Value of Reserve Assets Exceeds $137,000,000」把儲備金數字混進基金頁；缺基金總額、快照日、申請方式；名稱有三種（Protection Fund、網址 insurance-fund、頁尾 User Protection Fund） | 保险基金页SEO优化需求 09-02 | 前端＋財務 |
| 風險揭露 `/support/legal-disclosures/` | 合規 | 三個網址各自 canonical 指向自己，參數網址要指向乾淨路徑；頁尾改連乾淨路徑；名稱四種（頁尾 Risk Disclosure、H1 Legal Disclosures、正文 Risk Warning、簡中 title 风险提示）要統一 | 风险揭露页与法律实体页需求 09-03 需求 1 | 前端＋內容 |
| 服務地區 `/support/Service-Regions/` | 合規 | 本次沒有發現問題；法律實體頁上線後由該頁連入 | — | — |
| 官方渠道驗證 `/support/official-channel/` | 防詐騙 | 原始 HTML 沒有 H1，沒有官方網域的文字清單 | 官方认证渠道完善需求 08-11 | 前端＋品牌 |
| 系統狀態 `/status/` | 透明度 | 預留事件紀錄與事後報告的位置，作為事件通報的第一管道 | — | 產品 |
| Media Kit `/media-kit/` | 開頭 | title 是站台通用文案 | — | 前端 |
| 費率 `/rateStandard/index/` | 求助管道 | 原始 HTML 沒有 H1、沒有費率數字、沒有 canonical | 费率页SEO优化需求 09-03 | 前端 |
| 年度報告 `/campaign/annualReport/` | 透明度 | 沒有 H1，title 是站台通用文案；2026 版待定稿 | 年度報告中心修改意見 09-28 | 品牌 |
| 用戶協議、隱私政策、法律聲明 | 合規 | 參數網址與乾淨路徑並存；法律聲明乾淨路徑 title 為「/」；`/support/statement/`（2026）與 `/support/legal-statement/`（2019）是兩份不同文本；英文協議時限寫「thirty (20)」、聯絡方式寫成「Service@ www.hotcoin.com/」；主體說法與頁尾不一致 | 09-03 需求 1；主體統一待 Jimmy | 前端＋Jimmy |
| 說明中心〈How to strengthen the account security〉 | 帳戶安全 | 5 個 H1 改成 1 個 | — | 內容 |

**兩個全站問題，Hub 上線前要先修**：

1. `/{語言}/support/{任意字串}/` 一律回 200、title 為「/」，是軟 404。實測 `/en_US/support/zzq-random-test-8841/` 就是如此；`/support/cookie-policy/`、`/support/aml-policy/`、`/support/complaint/` 這些看起來像政策頁的網址也全是空殼。搜尋引擎可能把空殼頁當成正式頁收錄。不存在的路徑要回 404。
2. `/.well-known/security.txt` 回 200，內容是首頁 HTML。要換成真正的純文字檔。

### 3.5 入口與內鏈

| 入口 | 做法 | 開發量 |
|---|---|---|
| 關於我們頁 | 正文已有的兩段文字補連結，分別連 Hub 與法律實體頁 | 最小，Hub 上線當天就能做 |
| 頁尾 | 「關於我們」欄加一條「安全與信任中心」，放在儲備金證明（A9）之前，讓信任類連結排在一起。沿用 09-28 頁尾說明的三個值（顯示文字、網址、正式站是否顯示），Hub 上線當天開 | 小 |
| 既有信任頁 | 儲備金、保護基金、風險揭露、服務地區、官方驗證、系統狀態、Media Kit、年報各加一個「回到安全與信任中心」文字連結 | 小 |
| 新子頁 | 麵包屑：首頁 › 安全與信任中心 › 子頁名稱 | 隨頁面做 |
| 說明中心 | 安全分類頂部放 Hub 連結 | 小 |
| 文章 | 18 篇反詐與信任文章、insider 品牌故事頁，文內連回 Hub 或對應子頁 | 內容 |

不動頂部主導覽：「頂部主導覽改可爬連結」已列在本季不做清單，頁尾已能讓所有頁面被發現。錨文字用頁名，不用「點此」「了解更多」。

### 3.6 技術規格（給前端）

全站通用規則以《Hotcoin 公開頁面 SEO 發版驗收表 v0.1》（09-08，25 條）為準，這裡只列信任中心特有的部分：

1. **正文直出**：所有文字、數字、表格、連結都在伺服器回傳的第一份 HTML 裡，不靠 JS 補。儲備金與保護基金頁現在的問題就是這一條。
2. **一頁一個 H1；自指 canonical；只開有內容的語言網址**，有內容的語言之間互相 hreflang。延續保護基金頁需求第 3 項的規則。
3. **結構化資料**：Hub 與子頁輸出精簡版 Organization（v3.3 規定的六項，全站同一個 `@id`）、WebPage、BreadcrumbList。不用 FinancialService。常見問題可以加 FAQPage，但 Google 2023 年起只對政府與醫療網站顯示 FAQ 摘要，不要期待搜尋結果多出摘要。
4. **Sitemap**：Hub 與子頁上線同批加入。
5. **最後更新日**：每頁顯示，和實際修改日一致。
6. **security.txt**：放在 `/.well-known/security.txt`，純文字，包含 Contact、Expires、Policy（指向漏洞回報頁）、Preferred-Languages、Canonical 五個欄位。
7. **轉址**：`/{語言}/security/` 301 到 `/{語言}/trust/`。
8. **第一批語言**：英文與簡中。這兩種語言的風險揭露、服務地區已經上線，Hub 連出去不會連到空頁。其他語言等文案到位再開。

### 3.7 上線順序

| 批次 | 做什麼 | 等誰 | 建議時間 |
|---|---|---|---|
| 第 0 批：先修 | 3.4 表裡的技術缺陷（儲備金、保護基金、費率頁直出與標記；風險揭露與法律文件的 canonical；官方驗證頁 H1；Media Kit title；說明中心文章 H1）；軟 404；security.txt | 不等任何人，多數已在既有需求裡，只差排期 | 10 月 |
| 第 1 批：Hub v1 | Hub（只放已確認的事實）、漏洞回報頁、防詐騙頁；關於頁與頁尾入口 | Owen 定回報信箱並確認複測；品牌給官方網域清單；你定第四章 1 到 5 題 | 10 月底前 |
| 第 2 批 | 法律實體與登記頁、客訴頁、執法請求頁；用戶協議錯字與主體說法統一 | Jimmy 定合約主體、FinCEN 用哪一筆、客訴時限；客服負責人定流程 | 11 月 |
| 第 3 批 | 反洗錢與身分驗證頁；第二章「有條件再做」各項，條件到位一項做一項 | 合規、財務、上幣團隊 | 12 月起 |

這個順序和《九到十一月 SEO 優先級》第 8 項「十月補實體信任頁」一致。第 1 批不等法律實體頁，因為主體定案的時間不在 SEO 能控制的範圍；Hub 先用已確認的 AUSTRAC 登記上線，主體定案後再補。

### 3.8 驗收：不看點擊

第一章已經說明，信任類查詢的量很小，點擊不是這件事的驗收指標。延續你在首頁 FAQ 那次定的兩項驗收（AI 是否收錄、關鍵字查詢是否被覆蓋），具體做法：

1. **上線驗收（每頁上線當天）**：用不執行 JS 的方式抓原始 HTML，H1、正文、數字、連結都在；canonical、hreflang 正確；已進 sitemap；security.txt 回純文字。
2. **查詢承接（上線後 4 到 8 週）**：用第一章的七組信任查詢，看落地頁是否從首頁、insider、已 301 的團隊頁換成 Hub 與子頁。基線用 08-10 至 09-06 的快照；GSC 連線恢復後重拉一份 10 月基線。
3. **AI 收錄（每月一次）**：固定 6 個問題問 ChatGPT、Perplexity、Google AI Mode：Who operates hotcoin.com? Is Hotcoin regulated? Is Hotcoin safe? Does Hotcoin have proof of reserves? Hotcoin customer service phone number? What is Hotcoin's official website? 記錄答案有沒有引用 hotcoin.com 的信任頁、內容和頁面是否一致。Ahrefs Brand Radar 不在目前方案內，先手動記錄。
