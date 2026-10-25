### **Løsning til Oppgave 1**

First we extend the function $f$ to an odd function on the interval $[-2,2]$ by setting $g(x):=-f(-x)$ for $-2<x<0$. This means that $g(x)=-f(-x)=-(1-(-x))=-1-x$ for $-2<x<0$. Thus we have

$$g(x)=\begin{cases}1-x&\text{if }0<x<2,\\ -1-x&\text{if }-2<x<0.\end{cases}$$

Next,we consider the 4-periodic extension of this function. In particular, we have for $2<x<4$ that $g(x)=g(x-4)=-1-(x-4)=3-x$, and for $-4<x<-2$ we have $g(x)=g(x+4)=1-(x+4)=-3-x$. Thus the function $g$ is defined on the interval where we need to sketch it as

$$g(x)=\begin{cases}-3-x&\text{if }-4<x<-2,\\ -1-x&\text{if }-2<x<0,\\ 1-x&\text{if }0<x<2,\\ 3-x&\text{if }2<x<4.\end{cases}$$

The sketch we obtain is:

[Figure: Coordinate axes with $1$ ticked on both axes. A sawtooth graph on $[-4,4]$ consisting of four parallel line segments of slope $-1$, each falling from $1$ to $-1$ over an interval of length $2$, with jump discontinuities at the even integers; on $(0,2)$ the segment of $1-x$ starts at height $1$ and crosses zero at $x=1$.]

One might note here that the function $g$ is not only 4-periodic, but also 2-periodic. (Rather: Its fundamental period is 2).

Because the function $g$ is odd, the Fourier coefficients $a_n$, $n=0,1,\ldots$, are all zero. Moreover, we obtain for the Fourier coefficients $b_n$ the expression

$$\begin{array}{rl}b_n=&\displaystyle\frac{2}{2}\int_0^2(1-x)\sin\frac{n\pi x}{2}\,dx\\[10pt]
=&\displaystyle\int_0^2\sin\frac{n\pi x}{2}\,dx-\int_0^2x\sin\frac{n\pi x}{2}\,dx\\[10pt]
=&\displaystyle-\frac{2}{n\pi}\left(\cos n\pi-1\right)-\left[\frac{n^2\pi^2}{4}\sin\frac{n\pi x}{2}-\frac{2x}{n\pi}\cos\frac{n\pi x}{2}\right]_{x=0}^{x=2}\\[10pt]
=&\displaystyle\frac{2}{n\pi}\left(1-\cos n\pi\right)+\frac{4}{n\pi}\cos n\pi\\[10pt]
=&\displaystyle\frac{2}{n\pi}\left(1-\cos n\pi+2\cos n\pi\right)\\[10pt]
=&\displaystyle\frac{2}{n\pi}\left(1+(-1)^n\right)\\[10pt]
=&\left\{\begin{array}{ll}0&\quad\text{when }n\text{ is odd}\\[4pt] \frac{4}{n\pi}&\quad\text{when }n\text{ is even}.\end{array}\right.\end{array}$$

Thus the Fourier series we obtain is

$$\sum_{n=1}^{\infty}\frac{4}{2n\pi}\sin\frac{2n\pi x}{2}\,,$$

or simplified slightly,

$$\sum_{n=1}^{\infty}\frac{1}{n\pi}\sin n\pi x.$$

(Note that it is also possible (and perfectly fine) to regard the function $g$ as a 2-periodic function and compute the Fourier coefficients on the interval $[-1,1]$ instead. This changes the integration interval to $[0,1]$ and the factor in front of the integral to $2$. The final series remains unchanged.)

Kildesett: course=TMA4130 term=host year=2015 problem=1 file=bokmal.pdf
