### **Solution to Problem 2** **Fourier series [10 pts] (4N)**

For $k=1,2,3,\dots$, we get:
$$\begin{aligned}\frac{\partial E_N}{\partial a_k}&=-2\int_{-\pi}^{\pi}\left(f(x)-a_0-\sum_{n=1}^N a_n\cos(nx)\right)\cdot\cos(kx)dx\\
&=-2\int_{-\pi}^{\pi}f(x)\cdot\cos(kx)dx+2a_0\underbrace{\int_{-\pi}^{\pi}\cos(kx)dx}_{=0}+2\int_{-\pi}^{\pi}\sum_{n=1}^N a_n\cos(nx)\cdot\cos(kx)dx\\
&=-2\int_{-\pi}^{\pi}f(x)\cdot\cos(kx)dx+2\underbrace{\sum_{n=1}^N a_n\int_{-\pi}^{\pi}\cos(nx)\cdot\cos(kx)dx}_{=2\int_{-\pi}^{\pi}\cos(kx)\cdot\cos(kx)dx=\pi}\\
&\quad\text{(orthogonality of the trigonometric system)}\\
&=-2\int_{-\pi}^{\pi}f(x)\cdot\cos(kx)dx+2\pi a_k.\end{aligned}$$
Setting $\frac{\partial E_N}{\partial a_k}$ to $0$ gives
$$a_k=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos(kx)dx.$$
For $a_0$, we obtain:
$$\begin{aligned}\frac{\partial E_N}{\partial a_0}&=-2\int_{-\pi}^{\pi}\left(f(x)-a_0-\sum_{n=1}^N a_n\cos(nx)\right)dx\\
&=-2\int_{-\pi}^{\pi}f(x)dx+2a_0\underbrace{\int_{-\pi}^{\pi}dx}_{=2\pi}+2\int_{-\pi}^{\pi}\sum_{n=1}^N a_n\cos(nx)dx\\
&=-2\int_{-\pi}^{\pi}f(x)dx+4\pi a_0+2\sum_{n=1}^N\underbrace{\int_{-\pi}^{\pi}a_n\cos(nx)dx}_{=0}\\
&=-2\int_{-\pi}^{\pi}f(x)dx+4\pi a_0.\end{aligned}$$
Setting $\frac{\partial E_N}{\partial a_0}$ to $0$ gives
$$a_0=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)dx.$$

**Grading manual** (5p) for correctly identifying $a_k$ ($k=1,2,3,\dots$) from $\frac{\partial E_N}{\partial a_k}=0$ and (5p) for correctly identifying $a_0$ from $\frac{\partial E_N}{\partial a_0}=0$.

Kildesett: course=TMA4135 term=kont year=2023 problem=2 points=10 file=tma4130_2023h_exam-19.pdf
