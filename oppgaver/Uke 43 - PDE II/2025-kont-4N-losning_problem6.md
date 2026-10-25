### **Solution to Problem 6** **Wave Equation [10 pts]**

a) The initial shape function is
$$f(x)=\begin{cases}\frac{3}{10}x,&0\le x\le\frac{1}{3},\\[2mm]\frac{3(1-x)}{20},&\frac{1}{3}\le x\le1.\end{cases}$$

This corresponds to $u(x,0)=f(x)$ for $0<x<L$. From this one computes
$$\begin{aligned}b_n&=2\int_0^1f(v)\sin(n\pi v)dv\\&=\frac{3}{5}\int_0^{\frac{1}{3}}v\sin(n\pi v)dv+\frac{3}{10}\int_{\frac{1}{3}}^{1}(1-v)\sin(n\pi v)dv\\&=-\frac{\cos\left(\frac{n\pi}{3}\right)}{5n\pi}+\frac{3\sin\left(\frac{n\pi}{3}\right)}{5n^2\pi^2}+\frac{\cos\left(\frac{n\pi}{3}\right)}{5n\pi}+\frac{3\sin\left(\frac{n\pi}{3}\right)}{10n^2\pi^2}\\&=\frac{9\sin\left(\frac{n\pi}{3}\right)}{10\pi^2n^2}.\end{aligned}$$

The string starts from rest, i.e., $u_t(x,0)=g(x)=0$ for $0<x<L$, therefore the coefficients $b_n^*=0$.

b) Recall the general expression
$$\lambda_n=c\frac{n\pi}{L},\quad n=1,2,3,\ldots.$$

In the the problem, we assume $c=1/\pi$ (recall the general wave equation $u_{tt}=c^2u_{xx}$) and $L=1$, which implies that $\lambda_n=n$.

c) The complete solution is
$$u(x,t)=\frac{9}{10\pi^2}\sum_{n>0}\frac{\sin\left(\frac{n\pi}{3}\right)}{n^2}\sin n\pi x\cos nt.$$

**Grading manual** (10p)

a) (6p)

b) (2p)

c) (2p):

Kildesett: course=TMA4130 term=kont year=2025 problem=6 points=10 file=exam_math_4n_4d_tma4130_35-5.pdf
