### **Solution to Problem 8** **Discrete Fourier Transform [10 pts]**

We use the convention $f_N=f_0$. By the definition of the discrete Fourier transform,

$$\tilde c_j=\frac{1}{N}\sum_{k=0}^{N-1}w^{-jk}\tilde f_k=\frac{1}{N}\sum_{k=0}^{N-1}w^{-jk}f_{k+1}=\frac{w^j}{N}\sum_{k=0}^{N-1}w^{-j(k+1)}f_{k+1}.$$

In the last sum we consider the term corresponding to $k=N-1$. We have $w^{-jN}f_N=e^{-2\pi ij}f_0=f_0$. Thus

$$\tilde c_j=w^j\frac{1}{N}\left(\sum_{k=1}^{N-1}w^{-jk}f_k+f_0\right)=w^jc_j.$$

**Grading manual** (10p)

Kildesett: course=TMA4135 term=kont year=2023 problem=8 points=10 file=tma4130_2023h_exam-19.pdf
