### **Solution to Problem 4**

**a)** Separating variable method gives a Fourier sine series solution

$$u(x,t)=\sum_{n=1}^{\infty}e^{-\frac{1}{2}n^2t}A_n\sin nx,$$

where

$$A_n=\frac{2}{\pi}\int_0^{\pi}x(\pi-x)\sin nx\,dx.$$

Integration by parts gives

$$A_n=\frac{2}{\pi n}\int_0^{\pi}(\pi-2x)\cos nx\,dx=\frac{4}{\pi n^2}\int_0^{\pi}\sin nx\,dx=\frac{4(1-(-1)^n)}{\pi n^3}.$$

**b)** Solution: Symmetric approximation to $u_{xx}$ and forward Euler for $u_t$ yields

$$U_i^{n+1}=U_i^n+\frac{k}{2h^2}\big(U_{i+1}^n-2U_i^n+U_{i-1}^n\big),\quad i=1,\ldots,M-1,\ n=0,1,2,\ldots,$$

with boundary conditions

$$U_0^n=0,\quad U_M^n=0,\quad n=0,1,2,\ldots,$$

and initial conditions

$$U_i^0=x_i(\pi-x_i)\quad i=0,\ldots,M.$$

**c)** Compute $U_1^2$, the above scheme gives

$$u(\pi/4,0.1)\approx U_1^2=U_1^1+\frac{2}{5\pi^2}(U_2^1-2U_1^1),$$

where

$$U_1^1=\frac{3\pi^2}{16}+\frac{2}{5\pi^2}\big(-\frac{\pi^2}{8}\big)=\frac{3\pi^2}{16}-\frac{1}{20}$$

and

$$U_2^1=\frac{\pi^2}{4}+\frac{2}{5\pi^2}\big(-\frac{\pi^2}{8}\big)=\frac{\pi^2}{4}-\frac{1}{20}.$$

Thus

$$u(\pi/4,0.1)\approx\frac{3\pi^2}{16}-\frac{1}{10}+\frac{1}{50\pi^2}\approx 1.7525772488.$$

Kildesett: course=TMA4135 term=host year=2019 problem=4 points=20 file=unred.pdf
