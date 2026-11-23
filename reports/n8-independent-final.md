# N8 獨立科學審查：最終 15 頁

- 審查日期：2026-11-23（臺北時間）；審查基準：GitHub `main` HEAD `66269cea58b88cabd9be787603db70d0dc3805ce`。GitHub API 確認與本機 HEAD 一致。後續提交僅加入本報告。
- **本次獨立審查：PENDING。** S05 完整方法及結果無法讀取，其他五篇以相關段落為主而非逐字通讀，故無法完成使用者要求的六篇全文核對；不是宣稱內容已證偽。以下頁面判斷只適用已核對的範圍，不是全部內容已獲全面證實。
- 判準：PASS＝本頁重要主張在已核範圍有足夠支持；PARTIAL＝部分支持但重要來源定位或核對未完成；FAIL＝重要主張有足以要求修正的錯誤；UNVERIFIED＝重要主張缺少可供判斷的證據。數學例以獨立代數核對，不冒稱論文原有實驗。程式檢查不代替科學審查。

## 範圍與實際來源

讀取 `index.html` 的 15 個 section、`slides/evidence-map.json`、`raw/sources.json`、`wiki/concepts/teaching-foundations.md` 與相關概念頁及比較頁。人工核對主張、公式、方法、結果、局限和所附定位；不是獨立重做統計、重新分析資料、驗證所有互動控制項的計算或進行視覺／可及性審查。合成圖的數學主張依文字檢查，未逐一驗證互動圖執行時所有數值。沒有先讀既有 N8 報告或其他製作者審查結論。

- [S01 Donoghue et al. 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC8106550/)：取得全文網頁並閱讀核對相關段落，重點 Fig. 2、Methods「Algorithmic parameterization」、Extended Data Fig. 2–3；對照模型、峰與 Welch。
- [S02 Donoghue et al. 2022](https://old.postlab.psych.wisc.edu/files/9516/2715/7291/Donoghue2021_MethodologicalConsiderationsOscillations.pdf)：取得原文 PDF 並閱讀核對相關段落，重點 Box 1、Fig. 1、3 與第 7 節（第六項考量：空間重疊）。
- [S03 Cochrane et al. 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13064800/)：取得全文並閱讀核對相關段落，重點 Methods、Results、Tables 1–2、Discussion；核對受試者、模態與受試者內／間分析。
- [S04 Gao et al. 2017](https://inc.ucsd.edu/publications/Gao-NeuroImage2017.pdf)：取得全文 PDF 並閱讀核對相關段落，重點 §2.1–2.4、2.7、Fig. 1、§3–4；核對模型和動物資料。
- [S05 Salvatore et al. 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11305649/)：網址返回 reCAPTCHA；其他全文入口亦未能取得。搜尋引擎提供原文摘要及 Discussion 的索引文字，支持清醒活動、藥物方向及 Gi DREADD 反例，但 **未取得完整 Methods、Results、圖表，不能聲稱全文已讀或核對電極手術與全部條件**。原始來源索引的 FULL_ACCESS 狀態不代表本次實際取得。
- [S06 Sun & Mou 2023](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1203059/full)：取得全文網頁並閱讀核對相關段落，重點 Introduction、§1.1、§3–4；其為綜述，非此處假想機器學習實驗。

## 逐頁判斷

1. **PARTIAL** — 教學目標及「間接線索而非直接測量」與 S01 Fig. 2、S03 Discussion 相符；S05 Discussion 的可取得索引亦支持謹慎解讀，但未完整取得 S05，涉及反例的來源鏈尚待全文核對。
2. **PASS** — 多來源混合及非單細胞讀值有據：S02 第六項「Multiple oscillations coexist across the brain / Why this matters」討論體積傳導；S06 Introduction 討論 EEG 與參考，S04 §2.1、4.1 為模型與限制，並非完整頭皮前向模型。電位差是測量關係。
3. **PASS** — 差值公式與 5−2=3、5−1=4 正確，且標明合成；S06 Introduction、§1.1.4 對參考與眼肌干擾有據；S02 Box 1 對訊噪比有一般提醒。
4. **PASS** — Δt=1/fs；10 Hz 以 12 Hz 取樣時 sin(2π·10n/12)=−sin(2π·2n/12)，符合反相 2 Hz；32 Hz 下 10 Hz 低於 Nyquist。例子假設理想正弦與均勻取樣，不能推廣為真實 EEG 不需抗混疊。S06 §1.1、S02 Box 1 支持前處理／品質的一般背景，取樣計算是教學推導。
5. **PASS** — DFT 定義、FFT 作為演算法、複數係數及有符號頻率格點正確；N 偶數時 Nyquist 點的正負標記本屬慣例。1 秒 128 點格距 1 Hz；合成示例非研究結果。S04 §2.2 使用 STFT/FFT，並非該完整推導的直接來源。
6. **PASS** — PSD 線性頻帶積分、μV²/Hz、功率 dB 因子 10 與 Welch 分段加窗平均之敘述正確；S01 Methods「Algorithmic parameterization」說使用 Welch；S04 §2.2 明確以 STFT 功率中位數取代 Welch 平均，頁面區分正確。圖中單位與正規化之實際執行未另驗證。
7. **PASS** — S02 Fig. 1、3 說明頻帶功率可由背景造成，峰為候選振盪；S01 Methods eq. 1 將模型成分相加於對數功率空間。線性 PSD 面積與 log 峰增量有區分；固定增量與改變背景時面積可改變是模型推論。
8. **PASS** — S01 Fig. 2、Methods 的初始背景、扁平化、候選 Gaussian、聯合擬合及重新估計背景支持教學步驟；fixed/knee 與模型適配見 Methods、Extended Data Fig. 2–3。該圖明示不是實際執行擬合；峰不保證真實振盪（S01 Discussion）。
9. **PASS** — 在 f、f₀、P、P₀ 為正的固定模型下，斜率為 −β；所列 0.1、0.01 正確。S01 Methods eq. 3 的 k=0 支持此形式；不能由指數直接得突觸 E/I，亦符合 S04 模型限定與 S05 可取得 Discussion。此頁數學結論不依賴 S05 全文。
10. **PASS** — S04 §2.1 的 mean(gE)/mean(gI) 是模型電導比；S03 Methods「MRS-based E/I ratio」定義 Glx（glutamate＋glutamine）／GABA+（含共編輯巨分子）。電導、電生理頻譜及 MRS 代謝物指標不可當作相同物理量；箭頭是模型及關聯。
11. **PASS** — S04 §2.1、Fig. 1 設兩種不同時間常數的突觸電流，模型電導比和 30–50 Hz 斜率相關；§2.4、2.7、§3 為大鼠 CA1 LFP 與獼猴麻醉 ECoG 分析。動物證據與預測一致不等於直接測得各動物突觸比，§4.1 有模型簡化與其他電流限制；本頁保留限制。
12. **PASS** — S03 Results 排除 18 人中的 3 人後為 15 人；Methods 比較枕部 EEG 與早期視覺皮質同步 MRS 的五分鐘估計。Results Fig. 1、Table 1 支持部分跨人關聯；Fig. 2、Table 2 與 Discussion 顯示受試者內效應較弱，並非全部為零。關聯不能證明因果、突觸電流比或跨狀態泛化。
13. **PARTIAL** — S05 可取得摘要與 Discussion 支持活動小鼠、pentobarbital/diazepam 增加指數、亞麻醉 ketamine 無變化，以及 Gi DREADD 改變方向與假說相反；行為狀態與藥物作用的限制亦有討論。**硬腦膜外電極位置、各操弄的具體分析及 Fig. 1、2、6 尚需完整 Methods/Results 查證**。應在可讀全文後核對此頁與 evidence map S05 Methods 定位，現階段不判定其為錯。
14. **PASS** — 作為假想的跨受試者評估，先依人分組、訓練資料擬合標準化、驗證選設定、留出測試可防止所指洩漏；缺峰處理須只用訓練資料擬合其統計量。S06 Introduction、§1.1.2、§4 為動作想像、增強及泛化背景，不是該範例的實測證明；S02 Fig. 3 提醒頻帶混淆。無分類績效聲稱。
15. **PARTIAL** — S04 §3–4 的模態與模型限制、S03 Results/Discussion 的跨人關聯與濃度比，以及固定模型斜率的測驗皆有依據。S05 原文摘要與 Discussion 索引支持反例與狀態限制，但尚欠完整方法及結果核對；因此此跨研究總結暫不全通過。不同實驗不能直接視為互相推翻，不代表其假說間不存在實質張力。

## 待解決事項

取得 S05 完整原文，核對 EEG Surgery、EEG Analysis、Results 與 Figs. 1、2、6，尤其電極位置、藥物條件與 Gi DREADD 對指數的方向；再重新評估第 1、13、15 頁與整體狀態。必要時核查互動圖與其單位、圖例在實際執行時是否一致；本次未將此視為已完成。沒有要求修改 HTML、Wiki 或程式的結論，除非後續全文核對發現矛盾。

## 獨立初判後與既有 N8 報告比較

完成以上逐頁初判後，才讀取 `reports/n8-independent-review.md`。該報告審查基準為較早的 `7631b06`，並記錄其後同一製作者的局部修正；本次對 `66269ce` 的現有內容評分，兩個表格不可當成同一版本的直接比較。對修正後第 2–5、9、10、14 頁的科學內容，我的 PASS 與製作者再次核對的內容初判一致；第 6–8、11–12 頁亦無實質歧見。雙方都將整體 N8 保持 PENDING，且都區分科學審查與程式檢查。

差異在證據範圍與原因：既有報告稱當時取得 S05 PMC 全文，並將第 1、13、15 頁內容初判 PASS；本次實際只取得其摘要與 Discussion 的索引文字，無法獨立複核手術、分析及圖表，所以這三頁暫為 PARTIAL。製作者先前因參與製作而保留獨立性限制；本次為獨立 session，仍因原文核對範圍不全而 PENDING，不能用先前報告替代本次原文查核。

## 後續追加：S05 正式全文核對（2026-11-23）

本次只延續 S05 未完成的查核。期刊[正式全文頁](https://journals.physiology.org/doi/full/10.1152/jn.00445.2023)透過網頁檢索回傳 HTTP 403；PMC 於相同檢索方式仍顯示 reCAPTCHA。但透過瀏覽器成功開啟並閱讀 [PMC 收錄的正式期刊全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11305649/)，核對 Methods「EEG Surgery」「EEG Recording」「Drugs」「DREADDs」「EEG Analysis」、Results、Discussion 與 Fig. 1、2、6 的圖及圖說，另參照 Fig. 4 的 ketamine 結果。前述存取限制與原先 PARTIAL 初判保留作歷史；本次結果更新如下。

- **電極與狀態**：EEG Surgery 說明雙側額葉與頂葉硬腦膜外螺絲電極，小腦上方螺絲為參考；EEG Analysis 明定藥物分析使用右側頂葉電極的 5 分鐘 active-wake EEG。EEG Recording 說明錄影確認行為狀態。大多數藥物的分析時段約注射後 30 分鐘；若鎮靜則約 1 小時後。這是活動清醒時的皮質電極記錄，並非人類頭皮 EEG。
- **分析方法**：EEG Analysis 描述 5 秒分段、多錐窗頻譜，並以 FOOOF knee 模式分析 2–100 Hz；峰設定依操弄類別不同，在同一動物條件內保持一致。因此指數是此模型及頻段的參數，不能直接等同量得的突觸比。
- **Pentobarbital／diazepam**：Results「GABAAR-Positive Allosteric Modulators Increase Aperiodic Exponent」與 Fig. 1C、2C–D 顯示，分別為 15 與 1 mg/kg 時，active-wake 頂葉頻譜的指數增加，方向符合作者的抑制假說；資料中也有 offset 變化，不能把所有變化單歸因於唯一機制。
- **Ketamine**：Results「Ketamine, a Putative Agent of Cortical Disinhibition, Fails to Change the Aperiodic Exponent」及 Fig. 4C–D 顯示，10 mg/kg 亞麻醉劑量、15 隻小鼠的 exponent 未見變化，儘管週期成分改變；未觀察到變化不證明真實效應為零。120 mg/kg 麻醉劑量的小樣本及狀態不同，不能與此直接混同。
- **Gi DREADD**：Methods「DREADDs」、Results「Chemogenetic Disinhibition Fails to Decrease Aperiodic Exponent」、Fig. 6D–E：對表現 hM4D(Gi) 的 parvalbumin 陽性中間神經元施予 DCZ 後，exponent **增加**，與作者預測的下降方向相反，而非單純沒有變化。Discussion 指出病毒表現可能遍及腦內、網路與行為狀態均限制生理解讀；不等於直接測得突觸 E/I 比。

### 第 1、13、15 頁重新評估

- **第 1 頁：PASS**（取代前述 PARTIAL 的本次判斷）。S05 Discussion 支持頻譜指數需經跨證據比較，不能視為普遍可靠的 E/I 直接量測；其他既核對的 S01、S03 證據保持不變。
- **第 13 頁：PASS**。硬腦膜外電極、活動清醒、pentobarbital／diazepam 增加及 ketamine／Gi DREADD 不符合預期方向均獲上述 Methods、Results 與 Fig. 1、2、4、6 支持。現有「部分結果沒有依假說預期改變」涵蓋 Gi 的反向增加，但較不具體；不是必須修正的科學錯誤。
- **第 15 頁：PASS**。S05 的小鼠皮質 EEG 操弄與反例、行為狀態限制經全文核對，與先前核對的 S03、S04 合併後支持此頁審慎比較；研究間差異不能消除其對相同假說所形成的實質張力。

**整體 N8：PENDING。** S05 指定核對已完成，上述三頁在原先逐頁核對範圍內改為 PASS，未發現需修改 HTML、Wiki 或程式的具體科學錯誤。整體不升為 PASS，因先前報告已明記 S01–S04、S06 僅以相關段落為主，未完成使用者原先要求的五篇逐字全文閱讀；本次依指示僅處理 S05，未補做其他來源。互動圖的全部運行數值與補充資料亦未在本次重新驗證。
