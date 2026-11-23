# N8 科學審查：原始來源逐頁核對與獨立性狀態

2026-11-23（Asia/Taipei）；審查對象為提交 `7631b06` 的正式 15 頁版本。**N8 狀態：PENDING，不是獨立審查 PASS。** 本回合的執行者在同一對話中曾參與製作，雖重新讀取來源並逐頁核對，不能事後宣稱自己未參與過或已形成獨立審查。下表是本回合的內容核對結論，不代表獨立審查已完成。

## 範圍與證據

讀取 `raw/sources.json`、`slides/evidence-map.json`、`wiki/concepts/teaching-foundations.md`、S01–S06 paper notes、`index.html` 與其互動程式；核對六篇原文相關全文段落。S01、S02、S03、S06 直接查閱全文網頁；S04 使用作者提供的 PDF；S05 使用已取得的 PMC 全文。未以現有 review 文件的判斷作為來源。原文網址與 DOI 以 `raw/sources.json` 為準。DFT、取樣、Welch 的純數學算例為教學推導，不能冒充六篇論文各自報告的研究結果。`scripts/check_deck.py` 與 HTML section ID 的檢查只驗結構，不能證明來源忠實。

原文連結：[S01 Donoghue 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC8106550/)；[S02 Donoghue 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8761223/)；[S03 Cochrane 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13064800/)；[S04 Gao 2017](https://inc.ucsd.edu/publications/Gao-NeuroImage2017.pdf)；[S05 Salvatore 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11305649/)；[S06 Sun & Mou 2023](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1203059/full)。

狀態意義：PASS 表示本回合核對的頁面主張受到指定段落或明示的數學推導支持；PARTIAL 表示部分主張／引文定位或前提需要收斂；FAIL 表示重要主張直接錯誤或不支持；UNVERIFIED 表示相關原文或必要證據未能取得。這些狀態是**內容初判，不等於獨立審查認證**。

## 階段一：修正前的 15 頁逐頁表

| 頁 | 判定 | 原始定位與核對／問題 | 建議的回退 |
|---|---|---|---|
| 01 | PASS | S01 Fig. 2 及 S03、S05 Discussion 支持建模與審慎比對的教學路線；此頁是問題陳述，不宣稱直接量到 E/I。 | 無。 |
| 02 | PARTIAL | S06 Introduction 說明頭皮電極及多來源混合；指定的 S04 §2.1、§4.1 主要是 LFP 模型與其限制，並非頭皮組織傳播的直接定位。S02「#6 Multiple oscillations coexist across the brain / Why this matters」明確描述體積傳導、多來源與 EEG/MEG。 | 回 N6：增加 S02 #6 精確定位，Wiki 先補來源；不必推翻生理敘述。 |
| 03 | PARTIAL | S06 Introduction 支持參考電極與通道差；S06 §1.1.4 對眼／肌肉干擾較精確。指定的 S02 Box 1 是訊噪比方法建議；六篇中本次未定位到具體電源線干擾的直接陳述。合成 5−2=3、5−1=4 μV 正確。 | 回 N6/N7：精確標註 S06 §1.1.4；若不另增已審來源，將電源干擾改成較一般的外部干擾。 |
| 04 | PARTIAL | Δt=1/fₛ 及 10 Hz 在 12 Hz 取樣時與相反相位 2 Hz 正弦樣本重合可由算式驗證；S06 Introduction/§1.1 和 S02 Box 1 提供處理背景，並未在引用位置明確推導 Nyquist。32 Hz 的教學例子應限定單一 10 Hz 合成分量；真實混合 EEG 的高頻內容仍須抗混疊。 | 回 N7／Wiki：限定合成信號，增加真實資料的抗混疊前提；數學示例明示為推導而非論文結果。 |
| 05 | PARTIAL | DFT 公式、1 秒 128 Hz 的 1 Hz 格點及 4/10 Hz 合成例子數學正確；S04 §2.2 使用 FFT/STFT，但引用處不是 DFT 定義的詳細證明。`fₖ=kfₛ/N` 若未說明高半部的週期性／負頻率，初學者可能將其視為全部獨立正頻率。 | 回 N7／Wiki：補 k>N/2 的負頻率解讀與顯示範圍，保留現有合成圖。 |
| 06 | PASS | S01 Methods: Simulated PSD creation 等使用 Welch；S04 §2.2 明說其 STFT 分段功率取中位數、而 Welch 取平均。PSD、dB 轉換與先還原線性密度積分的數學說明一致；合成 Welch 不是聲稱重現 S04。 | 無；實作正規化需另以數學測試驗證。 |
| 07 | PASS | S01 Methods 方程式與 Fig. 2 是對數功率下背景加 Gaussian 峰；S02 Fig. 1、3 支持非週期背景改變時頻帶功率亦可改變。教學圖標示合成並區分 G 與線性 PSD。 | 無。 |
| 08 | PASS | S01 Fig. 2、Methods 與 Extended Data Fig. 2–3 支持背景、殘差、候選峰及重新估計；fixed/knee 的選擇與假設需依資料檢查。示意明示不是執行 FOOOF。 | 無。 |
| 09 | PARTIAL | S01 Methods fixed 情況支持冪次模型及 −β 的 log-log 斜率，S05 Discussion 不支持普遍直接 E/I 解讀；10 的負一／負二次方算例正確。但把有單位的 f 直接取 log，且改變 β 同時固定 A 的物理量綱未交代；應明確以參考頻率形成無因次比值。 | 回 N7／Wiki：改寫為 P(f)=P₀(f/f₀)^(−β)，說明 f₀=1 Hz 與 P₀；圖的合成數值可保持相同。 |
| 10 | PASS | S04 §2.1 模型 gE、gI 的時間平均 conductance 比；S03 Materials and Methods「MRS-based E/I ratio」明確將 Glx 定為 glutamate+glutamine、GABA+ 含共編輯巨分子，且指出不等同。箭頭並非等號。 | 無。 |
| 11 | PASS | S04 §2.1、§2.4、§2.7、§3.1–3.3、§4.1：模擬 E/I、海馬大鼠 LFP、propofol 下獼猴 ECoG；未直接驗證人類頭皮 EEG。 | 無。 |
| 12 | PASS | S03 Experimental design、MRS-based E/I ratio、Results Fig. 1–2/Tables 1–2 及 Discussion：原始 18 人中最後分析 15 人；部分受試者間關聯、受試者內整體較弱。位置、非因果與睡眠樣本限制合適。 | 無。 |
| 13 | PASS | S05 Methods「EEG Surgery」「EEG Analysis」、Results Figs. 1、2、6、Discussion：小鼠硬腦膜外皮質 EEG，正向變構藥物及 ketamine／Gi DREADD 的結果不全符合單一指數假說；行為狀態可能混淆。 | 無；不推廣為所有 EEG 指標均無效。 |
| 14 | PARTIAL | S06 Introduction 談動作想像；§1.1.2 討論增強樣本相似及過擬合；§3.1 討論 subject-independent 與 subject-dependent；S02 Fig. 3 指出背景混淆。X/y、訓練與切分是頁面明示的假想方案，非 S06 實驗成績；原 locator 未指向最直接的 §3.1。 | 回 N6：補 S06 §3.1 定位，保留假想與跨受試者限制。 |
| 15 | PASS | S04 §3–4、S03 Results/Discussion、S05 Results/Discussion 分別支持模型／動物、人類跨模態關聯及小鼠操弄的條件性比較；quiz 正確答案不是直接量測 E/I。 | 無。 |

## 三篇核心文獻的審查邊界

- **S04 Gao**：§2.1 的模型 E:I 是平均興奮／抑制 conductance 之比，§2.4 和 §2.7 是不同動物與侵入式量測；§4.1 也指出其他電流與模型獨立相加假設。不能把其實測當成人類頭皮 EEG 的驗證。
- **S03 Cochrane**：Results Fig. 1/Table 1 為受試者間比較；Fig. 2/Table 2 的受試者內關聯整體較弱且方向不一，不能說每個演算法每個頻帶都穩定正相關。MRS 的 Glx/GABA+ 是代謝物指標，不是突觸 conductance；相關不是因果。
- **S05 Salvatore**：Methods 為硬腦膜外電極、活動清醒時段與特定分析；Results、Discussion 提供支持與反例。藥理效應、鎮靜及狀態限制一般化。

## 階段二處置與狀態

上述 PARTIAL 退回 N6/N7 與 Wiki 進行局部修正，再重跑結構、數學及瀏覽器測試；實際結果及修正後狀態將追加於本節。若無未參與製作的審查者，N8 維持 PENDING，不以同一執行者的第二次核對冒充獨立驗證。

### 追加發現：對應 Wiki 的量綱表述

在核對第 10 頁對應的 `wiki/concepts/ei-balance.md` 時，發現該頁原本寫 conductance 比和 MRS 代謝物比「單位不同」。兩者若各以相同單位相除都可以是無因次比值，不能以單位不同作區分；正確差異是所比物理量及生理意義不同。第 10 頁本身沒有宣稱兩比值單位不同，故上表對該頁的內容初判不變；需退回 N6 修正 Wiki，並在第 10 頁明示 Gao 模型是平均 conductance 之比。依 S04 §2.1 和 S03 Methods「MRS-based E/I ratio」核對。

### 本回合局部修正與同一執行者的再次核對

以下是本回合的修正後內容判斷，**不是另一名獨立審查者的驗證**；N8 仍為 PENDING。

| 頁／Wiki | 修正 | 同一執行者的重新核對 |
|---|---|---|
| 02 | Evidence Map 加入 S02 #6「Why this matters」，Wiki 補體積傳導定位 | S02 原文該節描述電場跨組織傳至電極及多來源混合；S06 Introduction 說明頭皮電極。修正後內容初判 PASS。 |
| 03 | 補 S06 §1.1.4 定位，將未在六篇定位到的電源干擾改為一般外來干擾 | S06 §1.1.4 直接討論眼與肌肉干擾；差值算例仍為合成。修正後內容初判 PASS。 |
| 04 | 明示 32 Hz 只針對合成單一 10 Hz，並說明真實混合 EEG 的抗混疊前提 | 12 Hz 樣本上的 10 Hz 與反相 2 Hz 正弦值一致；屬可重現數學推導，非六篇論文的實驗值。修正後內容初判 PASS。 |
| 05 | 明確區分 DFT 正頻率格點與高半部的負頻率，並標記為數學推導 | N=128、fₛ=128 時 k=10 對應 +10 Hz，k=118 對應 −10 Hz；修正後內容初判 PASS。 |
| 09 | 改為 P=P₀(f/f₀)^(−β)，對數與圖軸均使用無因次比值 | 在 f₀=1 Hz、P₀=1 的合成情況下，f=10 Hz、β=1 與 2 分別為 0.1 和 0.01；與 S01 Methods fixed 模型等價。修正後內容初判 PASS。 |
| 10／Wiki | 將「比值單位不同」改為「所比物理量及意義不同」；第 10 頁標明兩種 conductance 的時間平均值 | S04 §2.1 是模型平均 gE/gI；S03 MRS-based E/I ratio 是 Glx/GABA+。兩種比值都可以是無因次，但不因此成為同一量。修正後內容初判 PASS。 |
| 14 | Evidence Map 補 S06 §3.1 | 該節明確區分新受試者測試和同一受試者不同片段；具體 X/y 模型仍標記假想。修正後內容初判 PASS。 |

以上之外其餘頁面維持修正前表格的內容初判。實際重新執行結果：`reports/n8-20261123/graph.txt` 的 N4 與 N6/N9 結構檢查通過；`mathematics.txt` 的 DFT、混疊、Welch、頻率正負與標準化冪次算例通過；`render-plot.txt` 的固定軸圖表通過；`browser.txt` 桌機／手機 errors 0、failures 0。程式通過不能證明科學來源忠實或提供審查者獨立性。

**仍需另一位未參與生成或修正的獨立審查者**，只接收最終逐頁內容、證據地圖與原始論文，再逐項驗證；在此之前 N8 不可標示 PASS。
