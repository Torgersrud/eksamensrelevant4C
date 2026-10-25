### **Solution to Problem 7** (Discrete Fourier Transform, 10 points)

a) No, a unique reconstruction is not possible.

The aliasing lemma for example states that

$$\hat{f}_j=\sum_{k\in\mathbb{Z}}c_{j+kN}(f),$$

where here $N=6$. But then, for example

$$\hat{f}_2=\ldots+c_{-10}(f)+c_{-4}(f)+c_2(f)+c_8(f)+\ldots,$$

where we can conclude from the bandlimited function $f$ that $\hat{f}_2=c_{-4}(f)+c_2(f)$. Similarly, $\hat{f}_3=c_{-3}(f)+c_3(f)$ and $\hat{f}_4=c_{-2}(f)+c_4(f)$. These do not allow for a unique reconstruction for $c_k(f)$. (3 P.)

b) Here, the aliasing lemma yields that $c_0(f)=\hat{f}_0$, $c_1(f)=\hat{f}_1$ and $c_{-1}(f)=\hat{f}_5$. All others are zero, either since $|k|>2$ or since the corresponding $\hat{f}_j=0$. (3 P.)

c) We obtain from the results in Item b) that the real coefficients are $a_0=c_0(f)=\hat{f}_0=2$ and we can combine $c_{\pm 1}=1$ into $a_1=2$. Since these are the only coefficients present, all other $a_n$ and all $b_n$ are zero. (2 P.)

Hence, the function $f$ reads (2 P.)

$$f(x)=2+2\cos(x).$$

Kildesett: course=TMA4432 term=test year=2026 problem=7 points=10 file=test-exam-math4c_web.pdf
