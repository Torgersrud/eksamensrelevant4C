### **Solution to Problem 3** **Fourier Series (14 points)**

a) The sketch looks like

[Plot: the $2\pi$-periodic even extension $g(x)$ drawn over $[-3\pi,3\pi]$: a zig-zag of straight line segments with maximum value $0$ (peaks) at $x=0$ and $x=\pm 2\pi$, dropping linearly to $-\pi$ (corners) at $x=\pm\pi$; vertical axis labelled $g(x)$ with tick $-\frac{\pi}{2}$, horizontal axis $x$ with ticks $-3\pi$, $-2\pi$, $-\pi$, $\pi$, $2\pi$, $3\pi$; the segment on $[0,\pi]$ is drawn darker.]

b) We can use the the even extension is an even function. Hence $b_n=0$ for $n=1,2,\dots$.
For the $a_n$ we use, that integrating over half an interval and multiplying that by 2 yields the result. Hence
$$a_0=\frac{2}{2\pi}\int_0^{\pi}g(x)\mathrm{d}x=-\frac{1}{\pi}\int_0^{\pi}x\mathrm{d}x=-\frac{\pi}{2}.$$
and
$$a_n=\frac{2}{\pi}\int_0^{\pi}g(x)\cos(nx)\mathrm{d}x=-\frac{2}{\pi}\int_0^{\pi}x\cos(nx)\mathrm{d}x$$
where we apply integration by parts. We have in $\int fg'\mathrm{d}x=fg-\int f'g\mathrm{d}x$ here with $f(x)=x$ and $g'(x)=\cos(nx)$ so $f'(x)=1$ and $g(x)=\frac{1}{n}\sin(nx)$
$$-\frac{2}{\pi}\left(\frac{x}{n}\sin(nx)\Big|_0^{\pi}-\int_0^{\pi}1\cdot\frac{1}{n}\sin(nx)\mathrm{d}x\right)=\frac{2}{n\pi}\int_0^{\pi}\sin(nx)\mathrm{d}x,$$
since $\sin(n\pi)=\sin(0)=0$ for all $n$. Now we just have to integrate and obtain
$$a_n=-\frac{2}{\pi n^2}\cos(nx)\Big|_0^{\pi}=-\frac{2}{\pi n^2}\left(\cos(n\pi)-\cos(0)\right)=-\frac{2}{\pi n^2}\left((-1)^n-1\right)$$
Since $\cos(0)=1$ and $\cos(n\pi)=\begin{cases}1&\text{if }n\text{ even},\\ -1&\text{if }n\text{ odd},\end{cases}$
the coefficient can further be simplified to
$$a_n=\begin{cases}\frac{4}{\pi n^2}&\text{if }n\text{ odd},\\ 0&\text{if }n\text{ even}.\end{cases}$$

c) We can directly read off $c_{-1}=7$, $c_3(f_1)=5$, $c_{-5}(f_1)=3$, $c_7(f_1)=1$ and all other coefficients are zero.

d) We can write $2(cos(2x))^2=\cos(4x)+1$. Hence the function reads
$$f_2(x)=\cos(4x)+1+2\sin(4x)-2\cos(8x)$$
and can directly read off the real coefficients $a_0=1$, $a_4=1$, $b_4=2$ and $a_8=-2$ and all others are zero. This means for the complex coefficients, that

- $c_0=a_0=1$
- $c_4=\frac{1}{2}(a_4-ib_4)=\frac{1}{2}-i$
- $c_{-4}=\frac{1}{2}+i$ (either the same way as above or since $f_2$ is real)
- $c_8=c_{-8}=-1$ (since $b_8=0$)
- all other coefficients are zero.

**Grading manual**

a) (3p)

b) (4p)

c) (3p)

d) (4p)

Kildesett: course=TMA4125 term=var year=2023 problem=3 points=14 file=tma4125-matematikk-4n-2023v_lf.pdf
