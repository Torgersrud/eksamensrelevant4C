### **Solution to Problem 4** **Fourier Transform (10 points)**

a) First note that $f$ is an odd function between $-1$ and $1$. Thus, the product $f(t)\cos(wt)$ is an odd function, whereas the product $f(t)\sin(wt)$ is an even function.

Next, recall that
$$\exp(-iws)=\cos(ws)-i\sin(ws).$$

The computation of the Fourier transform then yields
$$\begin{aligned}\mathcal{F}[f](w)&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(s)\exp(-iws)ds\\&=\frac{1}{\sqrt{2\pi}}\int_{-1}^{1}f(s)\exp(-iws)ds\\&=\frac{1}{\sqrt{2\pi}}\int_{-1}^{1}f(s)\cos(ws)ds-\frac{i}{\sqrt{2\pi}}\int_{-1}^{1}f(s)\sin(ws)ds\\&=-\frac{i}{\sqrt{2\pi}}\int_{-1}^{1}f(s)\sin(ws)ds\\&=-\frac{2i}{\sqrt{2\pi}}\int_{0}^{1}\sin(ws)ds\\&=\frac{2i}{\sqrt{2\pi}}\left[\frac{\cos(ws)}{w}\right]_{0}^{1}\\&=i\sqrt{\frac{2}{\pi}}\frac{\cos(w)-1}{w}\end{aligned}$$

Observe that this formula holds for $w$ different from zero. The case $w=0$ can be computed separately, giving $\mathcal{F}[f](0)=0$.

b) Define the function
$$g(t)=\frac{1}{t^2+c^2}$$
and observe that
$$f(t)=-\frac{1}{2}\frac{d}{dt}g(t).$$

The result from the lecture together with the hint then imply that
$$\begin{aligned}\mathcal{F}[g'](w)&=iw\mathcal{F}[g](w)\\&=iw\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{1}{s^2+c^2}\exp(-iws)ds\\&=-\frac{iw}{2c}\sqrt{\frac{\pi}{2}}\exp(-c|w|).\end{aligned}$$

**Grading manual:** a) 4 points and 1 point for w = 0 case b) 5 points

Kildesett: course=TMA4130 term=kont year=2025 problem=4 points=10 file=exam_math_4n_4d_tma4130_35-15.pdf
