### **Solution to Problem 5** **Wave equation and Heat equation (10 points)**

a) We compute partial derivations:

$$u_t(x,t)=\partial_tu(x,t)=2\cos(2t)\cos(x)$$

and

$$u_{tt}(x,t)=\partial_t\partial_tu(x,t)=-4\sin(2t)\cos(x).$$

Now with respect to $x$:

$$u_x(x,t)=\partial_xu(x,t)=-\sin(2t)\sin(x)$$

and

$$u_{xx}(x,t)=\partial_x\partial_xu(x,t)=-\sin(2t)\cos(x).$$

We see that:

$$u_{tt}=4u_{xx}.$$

b) We compute

$$u_{tt}(x,t)=\partial_t\partial_tF(a\cdot x-\lambda t)=\lambda^2F''(a\cdot x-\lambda t)$$

and

$$u_{x_ix_i}(x,t)=\partial_{x_i}\partial_{x_i}F(a\cdot x-\lambda t)=a_i^2F''(a\cdot x-\lambda t).$$

We then see that the condition $\lambda^2-\sum_{i=1}^{n}c_i^2a_i^2=0$ implies that $u(x,t)=F(a\cdot x-\lambda t)$ is a solution to (1).

c) Recall that the solution to the 1–dimensional heat boundary value problem

$$\begin{aligned}u_t(x,t)-c^2u_{xx}(x,t)=0,&\quad 0<x<L,\quad t>0\\ \text i)\ u(0,t)=0&=u(L,t),\quad t>0\\ \text{ii})\ u(x,0)=f(x),&\quad 0<x<L\end{aligned}$$

is given by

$$u(x,t)=\sum_{n=1}^{\infty}b_ne^{-\lambda_n^2t}\sin\left(\frac{n\pi}{L}x\right),\tag{4}$$

where

$$b_n=\frac{2}{L}\int_0^Lf(x)\sin\left(\frac{n\pi}{L}x\right)dx,\qquad\lambda_n=c\frac{n\pi}{L},\qquad n=1,2,\dots\tag{5}$$

From (4) and $L=\pi$ and $c=1$, we deduce that

$$u(x,t)=\sum_{n=1}^{\infty}b_ne^{-n^2t}\sin nx\tag{6}$$

where

$$b_n=\frac{2}{\pi}\int_0^{\pi}100\sin nx\,dx=\frac{200}{n\pi}(1-\cos n\pi).$$

Substituting $b_n$ and using the fact that $(1-\cos n\pi)=0$ if $n$ is even and $2$ if $n$ is odd, we obtain

$$\begin{aligned}u(x,t)=\frac{400}{\pi}\sum_{\begin{subarray}{c}n=1\\ n\ \mathrm{odd}\end{subarray}}^{\infty}\frac{e^{-n^2t}}{n}\sin nx\\ =\frac{400}{\pi}\sum_{k=0}^{\infty}\frac{e^{-(2k+1)^2t}}{2k+1}\sin(2k+1)x.\end{aligned}$$

Interpretation: If we fix a value of time $t$ in the series solution, then we obtain a function of $x$. It describes the temperature distribution of the bar at the given time $t$. In particular, when $t=0$, $u(x,0)$ gives the sine-expansion of the initial temperature distribution $f(x)$ over half-range domain.

**Grading manual**

a) (2p)

b) (3p)

c) (5p)

Kildesett: course=TMA4130 term=host year=2025 problem=5 points=10 file=exam_math_4n_4d_tma4130_35-21.pdf
