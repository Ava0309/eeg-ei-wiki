# EEG、頻譜與 E/I：教學基礎

本頁整合原始來源及明確標示的數學教學例子；示意圖和數值不是論文的受試者結果。逐項來源定位如下。獨立科學審查仍未完成。

## 從神經活動到 EEG

神經元的電活動產生電流與電場；許多來源的訊號經腦組織、頭骨與頭皮傳播並混合，頭皮電極量得兩點之間的微小電位差，而不是單一神經元的放電紀錄。訊號也可能含眼動、肌肉及環境干擾。參考電極的選擇決定通道比較的兩點：referential montage 比較各電極與參考點，bipolar montage 比較兩個電極。這是量測與混合，不是直接量測 E/I。參照 [S06](../papers/S06.md) Introduction 的 EEG、montage 與低訊噪比；[S02](../papers/S02.md)「#6 Multiple oscillations coexist across the brain / Why this matters」說明體積傳導和多來源混合；[S04](../papers/S04.md) §2.1、§4.1 說明突觸電流與場電位的模型假設與限制，並非頭皮 EEG 的完整前向模型。[S06](../papers/S06.md) §1.1.4 討論眼動與肌肉干擾。

## Sampling、FFT、PSD 與 Welch

取樣是以固定時間間隔記錄訊號：取樣率 fₛ（Hz）是每秒樣本數，間隔 Δt=1/fₛ。若頻率高於 fₛ/2，離散樣本可能與較低頻訊號無法區別，稱為 aliasing；濾波與取樣策略需考慮此問題；對含多頻率的真實訊號，即使某一分量低於 Nyquist 頻率，取樣前仍應考慮抗混疊濾波。基線漂移與眼動等雜訊要依任務與資料品質處理，濾波也可能改變訊號。這些是一般訊號處理數學與教學說明，並非六篇中的新實驗結果；[S06](../papers/S06.md) Introduction、§1.1 與 [S02](../papers/S02.md) Box 1 討論前處理及分析假設。

DFT：X[k]=Σₙ₌₀ᴺ⁻¹x[n] exp(−i2πkn/N)，x[n] 是樣本、N 是數目、k 是頻率索引。對 0≤k≤N/2，fₖ=kfₛ/N；對 N/2<k<N，對應的有符號頻率為 (k−N)fₛ/N，代表負頻率。FFT 是高效計算 DFT 的演算法；複數 X[k] 編碼幅值與相位。例：一秒、fₛ=128 Hz 的 x(t)=sin(2π·4t)+0.5sin(2π·10t)，理想頻率格點分別為 4 與 10 Hz；合成例子的幅值，不代表 EEG 真實數據。

頻譜 magnitude |X[k]| 描述傅立葉係數的大小；PSD 描述單位頻率的平均功率密度，常用電壓平方／Hz，需對時間窗、取樣率與單／雙側頻譜正規化。圖中 dB re 1 μV²/Hz 定義為 10log₁₀(PSD／1 μV²/Hz)，頻帶面積必須用線性 PSD 計算，不能直接積分 dB。Welch 方法將時序切成可重疊片段、對各片加窗、計算各片 periodogram，再逐頻率取**平均**；它通常減少估計變異，但片段較短會影響頻率解析度。[S01](../papers/S01.md) Methods: Simulations 使用 Welch；[S04](../papers/S04.md) §2.2 使用加窗 STFT 功率的**中位數**，作者特別指出這不同於 Welch 的平均；兩者不可混同。合成互動中採 Hann 窗（降低片段邊緣權重）與平均是示範 Welch，不是重現任何論文數據。

## Periodic、aperiodic 與參數化

[S01](../papers/S01.md) Fig. 2、Methods 在對數功率空間建模：log₁₀PSD=L(f)+ΣGᵢ(f)，L 為非週期背景，Gᵢ 為候選峰；相加是在 log 功率空間，不能直接當成線性 PSD 相加。演算法先估背景、找背景以上殘差的候選峰、擬合多個 Gaussian、重新估背景；必須檢查殘差、頻段、噪音、峰寬與模型假設。合成圖形直接用已知函數畫出，不代表真實擬合。

固定模式可寫 L=b−βlog₁₀(f/f₀)；b 是參考頻率 f₀ 的 offset，β 為 exponent，f 與 f₀ 為相同單位的頻率；取對數的是無因次比值。knee 模式在背景彎折時可允許曲率；若頻帶太窄或彎折不明顯，knee 未必可辨識，模型需與資料及殘差一起檢查。[S01](../papers/S01.md) Methods、Extended Data Fig. 2–3；[S02](../papers/S02.md) Fig. 1、3 指出單看頻帶功率可能混合背景與峰的變化。圖解可計算固定頻帶下的線性 PSD 積分，但峰高度不變時，背景改變也可改變總頻帶功率。

## E/I 生理量與三種證據

興奮性與抑制性輸入共同影響神經元及網路活動；conductance（電導）描述在特定電位差下離子通道有多容易導電，不等於神經傳遞物質的濃度。Gao 模型以興奮與抑制 conductance 的平均值之比表示模型 E/I，假設兩類突觸電流的時間常數不同，分析大鼠海馬 LFP（局部場電位）和獼猴 ECoG（皮質表面電極記錄）；結果提供模型條件下的場電位線索，不能直接等同頭皮 EEG。[S04](../papers/S04.md) §2.1–2.4、§2.7、§3、§4.1。

MRS（magnetic resonance spectroscopy，磁振波譜）利用 MR 訊號估計選定腦區內代謝物的濃度。Cochrane 以睡眠人類同步 EEG 與視覺皮質 MRS 比較候選指標；Glx 含 glutamate 與 glutamine，GABA+ 含 GABA 及共編輯巨分子，Glx/GABA+ 不等於突觸 conductance 比。作者報告部分受試者間關聯，受試者內關聯較弱；小樣本、睡眠狀態、腦區及相關性限制推論。[S03](../papers/S03.md) Materials and Methods: Experimental design、MRS-based E/I ratio；Results、Discussion。

Salvatore 使用小鼠硬腦膜外皮質 EEG 與藥理、化學遺傳操弄（以設計過的受體及藥物調整特定細胞活動）；pentobarbital 與 diazepam 對 exponent 的方向符合假說，而 ketamine 和 Gi DREADD 的部分結果不支持普遍可靠性。行為狀態及操弄的廣泛作用是解釋限制，不代表各研究必然互相推翻。[S05](../papers/S05.md) Methods: EEG Surgery、EEG Analysis；Results、Discussion。

## 假想機器學習工作流程

以左右手動作想像為假想分類標籤 y，將 alpha 候選峰頻率與 exponent 組成 X；不存在峰時須先規定缺失處理。先依受試者分訓練、驗證與測試，再僅用訓練資料擬合前處理與分類器；驗證集選設定，保留測試受試者到最後評估。重疊片段或增強樣本不能跨受試者分組邊界。這是教學設計，沒有聲稱已在資料上取得準確率。參照 [S06](../papers/S06.md) Introduction、§1.1.2、§4 和 [S02](../papers/S02.md) Fig. 3 對背景混淆的討論。
