# Spectral Parameterization

將對數功率譜建模為非週期背景與候選峰之和；逐次擬合背景與峰，再檢視殘差和模型假設。

來源：[S01](../papers/S01.md)，Fig. 2; Methods: Fitting algorithm。參照 paper note 的原文定位；獨立科學審查仍待完成。

## 參數與模型

固定模式可寫 L(f)=b−χ log₁₀(f/f₀)：b 為參考頻率 f₀ 的 offset，χ 為 exponent，f 與 f₀ 為相同單位的頻率。候選峰可描述中心頻率、相對功率與頻寬。

**直觀例子：** 先估背景再找峰並重新擬合；若資料有彎折 knee，強制使用無 knee 模式可能造成誤差。

**定位：** [S01](../papers/S01.md) Fig. 2、Methods、Extended Data Fig. 2。

相關概念：[頻譜參數化](spectral-parameterization.md) · [方法限制](limitations.md) · [Wiki 首頁](../index.md)。
