### **Solution to Problem 5** **Discrete Fourier Transform (10 points)**

a) No, a unique reconstruction is not possible.

The aliasing lemma for example states that
$$\hat f_j=\sum_{k\in\mathbb{Z}}c_{j+kN}(f),$$
where here $N=6$. But then, for example
$$\hat f_2=\ldots+c_{-10}(f)+c_{-4}(f)+c_2(f)+c_8(f)+\ldots,$$
where we can conclude from the bandlimited function $f$ that $\hat f_2=c_4(f)+c_2(f)$. Similarly, $\hat f_3=c_{-3}(f)+c_3(f)$ and $\hat f_4=c_{-2}(f)+c_4(f)$. These do not allow for a unique reconstruction for $c_k(f)$.

b) Here, the aliasing lemma yields that $c_0(f)=\hat f_0$, $c_1(f)=\hat f_1$ and $c_{-1}(f)=\hat f_5$. All others are zero, either since $|k|>2$ or since the corresponding $\hat f_j=0$.

c) We obtain from the results in Item b) that the real coefficients are $a_0=c_0(f)=\hat f_0=2$ and we can combine $c_{\pm1}=1$ into $a_1=2$. Since these are the only coefficients present, all other $a_n$ and all $b_n$ are zero.

Hence, the function $f$ reads
$$f(x)=2+2\cos(x).$$

**Grading manual**

a) (3p)

b) (3p)

c) (4p)

Kildesett: course=TMA4125 term=var year=2025 problem=5 points=10 file=math4n-2025v-en-lf.pdf
