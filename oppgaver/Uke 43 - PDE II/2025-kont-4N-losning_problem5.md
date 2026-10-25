### **Solution to Problem 5** **Heat Equation [10 pts]**

a) We directly compute
$$\frac{1}{L}\int_0^Lu_n(t,x)dx=\frac{1}{L}\int_0^L\cos\left(\frac{n\pi}{L}x\right)e^{-\left(\frac{n\pi c}{L}\right)^2t}dx=\frac{1}{L}e^{-\left(\frac{n\pi c}{L}\right)^2t}\left[\frac{L}{n\pi}\sin\left(\frac{n\pi}{L}x\right)\right]_0^L=0$$

b) For a general $t$ we have
$$\int_0^L|u_n(t,x)|^2dx=\int_0^L\cos^2\left(\frac{n\pi}{L}x\right)e^{-2\left(\frac{n\pi c}{L}\right)^2t}dx=e^{-2\left(\frac{n\pi c}{L}\right)^2t}\left[\frac{x}{2}+\frac{L}{2n\pi}\sin\left(\frac{2n\pi}{L}x\right)\right]_0^L=\frac{L}{2}e^{-2\left(\frac{n\pi c}{L}\right)^2t}.$$

Thus we find the $L^2$-norm
$$\left(\int_0^L|u_n(t,x)|^2dx\right)^{1/2}=\sqrt{\frac{L}{2}}e^{-\left(\frac{n\pi c}{L}\right)^2t}$$

and its derivative
$$\frac{d}{dt}\left(\int_0^L|u_n(t,x)|^2dx\right)^{1/2}=\frac{\frac{d}{dt}\left(\int_0^L|u_n(t,x)|^2dx\right)}{2\left(\int_0^L|u_n(t,x)|^2dx\right)^{1/2}}=-\sqrt{\frac{L}{2}}\left(\frac{n\pi c}{L}\right)^2e^{-\left(\frac{n\pi c}{L}\right)^2t}<0,$$

so the $L^2$-norm is decreasing. We also want to find $T$ such that
$$e^{-\left(\frac{n\pi c}{L}\right)^2T}=\frac{1}{2},$$

that is,
$$T=\frac{-\ln\left(\frac{1}{2}\right)}{\left(\frac{n\pi c}{L}\right)^2}=\frac{L^2\ln(2)}{(n\pi c)^2}.$$

c) We use the equation and boundary conditions to obtain
$$\frac{\partial}{\partial t}\frac{1}{L}\int_0^Lu(t,x)dx=\frac{1}{L}\int_0^L\frac{\partial}{\partial t}u(t,x)dx=\frac{c^2}{L}\int_0^L\frac{\partial^2}{\partial x^2}u(t,x)dx=\frac{c^2}{L}\left[\frac{\partial}{\partial x}u(t,x)\right]_0^L=0$$

and
$$\begin{aligned}\frac{\partial}{\partial t}\frac{1}{L}\int_0^L|u(t,x)|^2dx&=\frac{2}{L}\int_0^Lu(t,x)\frac{\partial}{\partial t}u(t,x)dx\\&=\frac{2c^2}{L}\int_0^Lu(t,x)\frac{\partial^2}{\partial x^2}u(t,x)dx\\&=\frac{2c^2}{L}\left[\frac{\partial}{\partial x}u(t,x)\,u(t,x)\right]_0^L-\frac{2c^2}{L}\int_0^L\frac{\partial}{\partial x}u(t,x)\frac{\partial}{\partial x}u(t,x)dx\\&=-\frac{2c^2}{L}\int_0^L\left(\frac{\partial}{\partial x}u(t,x)\right)^2dx\le0\end{aligned}$$

Alternatively the last part can be solved using the formula for the general solution $u(x,t)=\hat{f}_0+\sum_{n=1}^{\infty}\hat{f}_nu_n(t,x)$, where $\hat{f}_i$ are the Fourier coefficients of $f$ using the facts about $u_n(t,x)$ from the first two parts and the orthogonality of the $u_n(t,x)$.

**Grading manual**

a) (2p)

b) (3p) - (2p) for showing that the L2 norm is decreasing and (1p) for finding T

c) (5p) - (2p) for showing that the average temperature is constant and (3p) for showing that the L2 norm is decreasing.

Kildesett: course=TMA4130 term=kont year=2025 problem=5 points=10 file=exam_math_4n_4d_tma4130_35-5.pdf
