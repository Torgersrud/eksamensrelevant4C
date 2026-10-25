### **Solution to Problem 2**

Notice that we can write $f$ as $e^{ix}+g$, where

$$g(x)=\begin{cases}\alpha,&0\leq x\leq\pi,\\ -1,&-\pi\leq x<0.\end{cases}$$

Hence it suffices to compute the Fourier series for $g$ and add $e^{ix}$ to the final result.

For $c_0$ we get

$$c_0=\frac{1}{2\pi}\Big(\int_{-\pi}^{0}-1dx+\int_{0}^{\pi}\alpha dx\Big)=(\alpha-1)/2.$$

For other $c_n$, we have

$$c_n=\frac{1}{2\pi}\Big(\int_{-\pi}^{0}-e^{-inx}dx+\alpha\int_{0}^{\pi}e^{-inx}dx\Big).$$

Since $\int_{-\pi}^{\pi}e^{-inx}dx=0$, we get $\int_{-\pi}^{0}-e^{-inx}dx=\int_{0}^{\pi}e^{-inx}dx$, which gives

$$c_n=\frac{\alpha+1}{2\pi}\int_{0}^{\pi}e^{-inx}dx=\frac{\alpha+1}{2\pi}\cdot\frac{1-(-1)^n}{in}.$$

Notice that $1-(-1)^n=0$ when $n$ is even and $1-(-1)^n=2$ when $n$ is odd, thus

$$f(x)=e^{ix}+\frac{\alpha-1}{2}+\sum_{n\ \mathrm{odd}}\frac{1+\alpha}{in\pi}e^{inx}.$$

Input $\alpha=-1,-2,2,3$ gives the final results respectively.

Kildesett: course=TMA4135 term=host year=2020 problem=2 points=5 file=completeexam_nosolutions.pdf
