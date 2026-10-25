### **Solution to Problem 1** **Fourier Series (10 points)**

a) **Determine symmetry**

Check $f(-t)$:

$$f(-t)=\begin{cases}-t,&0<t<\pi,\\ \pi+t,&-\pi<t<0,\end{cases}$$

which is neither $f(t)$ nor $-f(t)$. Therefore, $f(t)$ is neither even nor odd, so the Fourier series will contain both cosine and sine terms.

b) **Fourier series formula**

For a $2\pi$-periodic function:

$$f(t)\sim\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos(nt)+b_n\sin(nt)\right),$$

where

$$a_0=\frac{1}{\pi}\int_{-\pi}^{\pi}f(t)\,dt,\quad a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(t)\cos(nt)\,dt,\quad b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt.$$

Compute $a_0$:

$$a_0=\frac{1}{\pi}\left(\int_{-\pi}^{0}t\,dt+\int_{0}^{\pi}(\pi-t)\,dt\right)=\frac{1}{\pi}\left(0-\frac{\pi^2}{2}+\frac{\pi^2}{2}\right)=0$$

Compute $a_n$:

$$a_n=\frac{1}{\pi}\left(\int_{-\pi}^{0}t\cos(nt)\,dt+\int_{0}^{\pi}(\pi-t)\cos(nt)\,dt\right)$$

$$\int t\cos(nt)\,dt=\frac{t\sin(nt)}{n}+\frac{\cos(nt)}{n^2}$$

$$\int_{-\pi}^{0}t\cos(nt)\,dt=\frac{1-(-1)^n}{n^2},\quad\int_{0}^{\pi}(\pi-t)\cos(nt)\,dt=\frac{1-(-1)^n}{n^2}$$

$$\Rightarrow a_n=\frac{2(1-(-1)^n)}{\pi n^2}$$

$$\text{Thus: }a_n=\begin{cases}0,&n\ \text{even},\\ \dfrac{4}{\pi n^2},&n\ \text{odd}.\end{cases}$$

Compute $b_n$:

$$b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt=\frac{1}{\pi}\bigg(\int_{-\pi}^{0}t\sin(nt)\,dt+\int_{0}^{\pi}(\pi-t)\sin(nt)\,dt\bigg).$$

First integral:

$$\int t\sin(nt)\,dt=-\frac{t\cos(nt)}{n}+\frac{\sin(nt)}{n^2}.$$

Hence

$$\int_{-\pi}^{0}t\sin(nt)\,dt=\left[-\frac{t\cos(nt)}{n}+\frac{\sin(nt)}{n^2}\right]_{t=-\pi}^{0}=\frac{\pi\cos(n\pi)}{n}.$$

Second integral:

$$\int_{0}^{\pi}(\pi-t)\sin(nt)\,dt=\pi\int_{0}^{\pi}\sin(nt)\,dt-\int_{0}^{\pi}t\sin(nt)\,dt.$$

We have

$$\int_{0}^{\pi}\sin(nt)\,dt=\frac{1-(-1)^n}{n},$$

and

$$\int_{0}^{\pi}t\sin(nt)\,dt=\left[-\frac{t\cos(nt)}{n}+\frac{\sin(nt)}{n^2}\right]_{0}^{\pi}=-\frac{\pi\cos(n\pi)}{n}.$$

Thus

$$\int_{0}^{\pi}(\pi-t)\sin(nt)\,dt=\frac{\pi(1-(-1)^n)}{n}+\frac{\pi\cos(n\pi)}{n}.$$

Adding and dividing by $\pi$,

$$b_n=\frac{1}{\pi}\left(\frac{\pi\cos(n\pi)}{n}+\frac{\pi(1-(-1)^n)}{n}+\frac{\pi\cos(n\pi)}{n}\right)=\frac{1-(-1)^n}{n}.$$

Therefore

$$\boxed{\,b_n=\frac{1-(-1)^n}{n}=\begin{cases}0,&n\ \text{even},\\ \dfrac{2}{n},&n\ \text{odd}.\end{cases}\,}$$

The Fourier series becomes

$$f(t)\sim\sum_{\begin{subarray}{c}n\geq 1\\ n\ \mathrm{odd}\end{subarray}}\frac{4}{\pi n^2}\cos(nt)\ +\sum_{\begin{subarray}{c}n\geq 1\\ n\ \mathrm{odd}\end{subarray}}\frac{2}{n}\sin(nt).$$

c) **First three nonzero terms**

$$\boxed{\,f(t)\approx\frac{4}{\pi}\cos t+2\sin t+\frac{4}{9\pi}\cos 3t+\frac{2}{3}\sin 3t+\cdots\,}$$

Grading manual: a) 1 point, b) 8 points c) 1 point

Kildesett: course=TMA4130 term=host year=2025 problem=1 points=10 file=exam_math_4n_4d_tma4130_35-21.pdf
