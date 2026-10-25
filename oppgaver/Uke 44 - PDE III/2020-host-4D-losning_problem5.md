### **Solution to Problem 5**

a) We have $w_t=0$, and $w_{xx}=-\alpha/c^2$, which implies that $w_t-c^2w_{xx}=\alpha$.

b) Consider the function $v=u-w$. Linearity (or superposition) implies that $v$ satisfies

$$v_t=c^2v_{xx},\quad v(0,t)=v(\pi,t)=0,\quad t>0,$$

(note that $w$ vanishes at $x=0$ and $\pi$), with initial data

$$v(x,0)=u(x,0)-w(x,0)=\begin{cases}0,&0\leq x<\frac{\pi}{2},\\ x-\pi,&\frac{\pi}{2}<x\leq\pi.\end{cases}$$

Standard separation of variables (Kreyszig, pp. 558ff) gives that

$$v(x,t)=\sum_{n=1}^{\infty}B_n\sin(nx)e^{-(cn)^2t}$$

where $B_n$ are given as the Fourier coefficients of the initial data, thus

$$v(x,0)=\sum_{n=1}^{\infty}B_n\sin(nx)=\begin{cases}0,&0\leq x<\frac{\pi}{2},\\ x-\pi,&\frac{\pi}{2}<x\leq\pi.\end{cases}$$

Standard formulas for Fourier series yield

$$B_n=\frac{2}{\pi}\int_{0}^{\pi}\sin(nx)w(x,0)dx$$

$$=\frac{2}{\pi}\int_{\pi/2}^{\pi}\sin(nx)(x-\pi)dx$$

$$=\frac{2}{\pi}\Big[-\Big|_{\pi/2}^{\pi}\frac{1}{n}\cos(nx)(x-\pi)+\frac{1}{n}\int_{\pi/2}^{\pi}\cos(nx)dx\Big]$$

$$=-\frac{1}{n}\cos\big(\frac{n\pi}{2}\big)-\frac{2}{\pi n^2}\sin\big(\frac{n\pi}{2}\big).$$

Thus the answer reads

$$u(x,t)=w(x,t)+v(x,t)$$

$$=\frac{\alpha}{2c^2}x(\pi-x)-\sum_{n=1}^{\infty}\Big(\frac{1}{n}\cos\big(\frac{n\pi}{2}\big)+\frac{2}{\pi n^2}\sin\big(\frac{n\pi}{2}\big)\Big)\sin(nx)e^{-(cn)^2t}.$$

c) We see that each term in the infinite sum contains the exponentially decaying factor $e^{-(cn)^2t}$. Thus these terms will all vanish in the limit when $t\to\infty$. Hence

$$u(x,t)\to\frac{\alpha}{2c^2}x(\pi-x),\quad t\to\infty.$$

Kildesett: course=TMA4135 term=host year=2020 problem=5 points=20 file=completeexam_nosolutions.pdf
