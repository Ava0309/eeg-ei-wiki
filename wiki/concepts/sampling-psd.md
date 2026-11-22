# Sampling, Filtering, FFT & PSD

取樣率 fs 為每秒樣本數；FFT 將有限數列轉換至頻域，PSD 描述功率如何分布於頻率。濾波與取樣選擇會影響可解釋範圍。

來源：[S06](../papers/S06.md)，§1.1。參照 paper note 的原文定位；獨立科學審查仍待完成。

## 取樣與頻譜

取樣率 fₛ 是每秒樣本數；X[k]=Σₙ₌₀ᴺ⁻¹ x[n]e^(−i2πkn/N)，其中 n 是時間樣本索引、k=0,…,N−1 是頻率索引、N 是樣本數、i²=−1；取樣率為 fₛ 時，頻率格點 fₖ=kfₛ/N。這是 DFT 定義；FFT 是高效計算 DFT 的演算法。PSD 是功率隨頻率的分布，需依取樣率及窗函數正規化。

**直觀例子：** 一秒 128 個樣本的合成訊號中，10 Hz 正弦波在 10 Hz 出現功率峰；真實資料需要檢查濾波、雜訊及時間窗。

**定位：** [S04](../papers/S04.md) §2.2；[S06](../papers/S06.md) Introduction。

相關概念：[頻譜參數化](spectral-parameterization.md) · [方法限制](limitations.md) · [Wiki 首頁](../index.md)。
