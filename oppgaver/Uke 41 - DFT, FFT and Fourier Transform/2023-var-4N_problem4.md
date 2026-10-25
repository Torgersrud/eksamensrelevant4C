### **Problem 4** **Discrete Fourier Transform (12 points)**

In this task we consider the discrete Fourier Transform (DFT) for signals of length $n=5$. We denote by $w_5=e^{-2\pi i/5}$.

a) Using $w_5$, what does the Fourier matrix $F_5$ look like?

b) Assume $\mathbf{f}=(f_0,f_1,f_2,f_3,f_4)$, is given by $f_i=g(x_j)$, $x_j=\frac{2\pi j}{N}$, $i=0,\dots,4$, i.e. sampling a $2\pi$-periodic function $g$, which is known to be bandlimited, that is $c_k(g)=0$ for $|k|>k_{\max}>0$.
What is the highest frequency $k_{\max}\in\mathbb{N}$ where you can reconstruct $g$ from $\hat{\mathbf{f}}=F_5\mathbf{f}$?
What happens if frequencies $k>k_{\max}$ occur?

c) What does the inverse DFT $F_5^{-1}\hat{\mathbf{f}}$ look like for $\hat{\mathbf{f}}=(c,0,0,0,0)$, $c\in\mathbb{R}$?

Kildesett: course=TMA4125 term=var year=2023 problem=4 points=12 file=tma4125-matematikk-4n-2023v_lf.pdf
