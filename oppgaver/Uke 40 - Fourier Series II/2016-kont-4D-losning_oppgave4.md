### **Løsning til Oppgave 4**

**a)** Standard formulas give (Kreyszig, p. 484)

$$a_0=\frac{1}{2L}\int_{-L}^{L}f(x)dx=\frac{1}{L}\int^L(L-x)dx=\frac{L}{2},$$

$$a_n=\frac{1}{L}\int_{-L}^{L}f(x)\cos\left(\frac{n\pi x}{L}\right)dx=\frac{2}{L}\int_0^L(L-x)\cos\left(\frac{n\pi x}{L}\right)dx=-\frac{2L}{(n\pi)^2}\left((-1)^n-1\right),\quad n\in\mathbb N,$$

$$b_n=0,\quad n\in\mathbb N.$$

Thus

$$\begin{aligned}f(x)&=\frac{L}{2}-\frac{2L}{\pi^2}\sum_{n=1}^{\infty}\frac{(-1)^n-1}{n^2}\cos\left(\frac{n\pi x}{L}\right)\\
&=\frac{L}{2}+\frac{4L}{\pi^2}\sum_{n=1}^{\infty}\frac{1}{(2n-1)^2}\cos\left(\frac{(2n-1)\pi x}{L}\right),\quad x\in[0,L].\end{aligned}$$

**b)** Standard formulas give (Kreyszig, p. 484)

$$\begin{aligned}a_0&=0,\\ a_n&=0,\quad n\in\mathbb N,\\ b_n&=\frac{1}{L}\int_{-L}^{L}f(x)\sin\left(\frac{n\pi x}{L}\right)dx=\frac{2}{L}\int_0^L(L-x)\sin\left(\frac{n\pi x}{L}\right)dx\\
&=\frac{2L}{n\pi},\quad n\in\mathbb N.\end{aligned}$$

Thus

$$f(x)=\frac{2L}{\pi}\sum_{n=1}^{\infty}\frac{1}{n}\sin\left(\frac{n\pi x}{L}\right),\quad x\in(0,L].$$

**c)** For $x\in(0,L)$ we have

$$\begin{aligned}0&=\text{Fourier series in (b)}-\text{Fourier series in (a)}\\
&=\frac{2L}{\pi}\sum_{n=1}^{\infty}\frac{1}{n}\sin\left(\frac{n\pi x}{L}\right)-\left(\frac{L}{2}+\frac{4L}{\pi^2}\sum_{n=1}^{\infty}\frac{1}{(2n-1)^2}\cos\left(\frac{(2n-1)\pi x}{L}\right)\right)\end{aligned}$$

which can easily be rewritten to the given expression. When $x=0$ the Fouries series in (a) sums to $L$ while the Fourier series in (b) sums to zero. Thus the left-hand side equals $-L/2$ for $x=0$. When $x=L$, both Fourier series sum to zero, and thus the identity is still valid for $x=L$.

**d)** Parseval's formula (Kreyszig, p. 497, replace $\pi$ by $L$) gives for the functions in (a)

$$2a_0^2+\sum_{n=1}^{\infty}a_n^2=\frac{1}{L}\int_{-L}^{L}f(x)^2dx$$

Thus

$$\frac{1}{2}L^2+\sum_{n=1}^{\infty}\frac{16L^2}{\pi^4(2n-1)^4}=\frac{2}{3}L^2$$

or

$$\sum_{n=1}^{\infty}\frac{1}{(2n-1)^4}=\frac{\pi^4}{16L^2}\left(\frac{2}{3}L^2-\frac{1}{2}L^2\right)=\frac{\pi^4}{96}.$$

Kildesett: course=TMA4135 term=kont year=2016 problem=4 file=tma4135_16k.pdf
