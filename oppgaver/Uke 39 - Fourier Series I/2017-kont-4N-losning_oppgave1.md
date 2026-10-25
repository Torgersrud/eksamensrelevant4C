### **Løsning til Oppgave 1**

**a)** $f$ is an even function.

$f$ has a period of $4$, as

$$f(x+4)=f(x)\quad\text{for all } x .$$

**b)**

$$f(x)=\left\{\begin{array}{ll} 1 & 0<x<1\\ 2-x & 1<x<2 \end{array}\right.$$

we have

$$a_0=\frac{2}{4}\left(\int_0^1 dx+\int_1^2(2-x)\,dx\right)=\frac{1}{2}\left(1+\left[2x-\frac{x^2}{2}\right]_1^2\right)=\frac{1}{2}\left(1+4-2-2+\frac{1}{2}\right)=\frac{3}{4}$$

$$\begin{array}{rcl}
a_n&=&\displaystyle\frac{2}{2}\left(\int_0^1\cos\frac{n\pi x}{2}\,dx+\int_1^2(2-x)\cos\frac{n\pi x}{2}\,dx\right)\\[8pt]
&=&\displaystyle\left[\frac{2}{n\pi}\sin\frac{n\pi x}{2}\right]_0^1+\left[\frac{4}{n\pi}\sin\frac{n\pi x}{2}\right]_1^2-\left[\frac{2x}{n\pi}\sin\frac{n\pi x}{2}\right]_1^2-\left[\frac{4}{n^2\pi^2}\cos\frac{n\pi x}{2}\right]_1^2\\[8pt]
&=&\displaystyle\frac{4}{n^2\pi^2}\left(-\cos n\pi+\cos\frac{n\pi}{2}\right)
\end{array}$$

$$=\left\{\begin{array}{ll}
\displaystyle\frac{4}{n^2\pi^2}\,, & n=2k+1\quad\text{odd}\\[10pt]
\displaystyle-\frac{8}{n^2\pi^2}\,, & n=4k+2\\[10pt]
0\,, & n=4k \end{array}\right.$$

$b_n=0$ as $f$ is even.

$$f=\frac{3}{4}+\frac{4}{\pi^2}\sum_{k=0}^{\infty}\left(\frac{1}{(2k+1)^2}\cos\frac{(2k+1)\pi x}{2}-\frac{2}{(4k+2)^2}\cos\frac{(4k+2)\pi x}{2}\right)$$

Kildesett: course=TMA4125 term=kont year=2017 problem=1 file=kont_bok.pdf
