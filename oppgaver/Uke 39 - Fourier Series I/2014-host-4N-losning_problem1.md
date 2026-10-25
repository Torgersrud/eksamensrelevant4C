### **Solution to Problem 1**

**a)** First we must observe that $f(x)$ is an even function, so the Fourier series of $f(x)$ will be of the form

$$a_0+\sum_{i=1}^{\infty}a_n\cos(nx)\,.$$

So the computation follows to

$$a_0=\frac{1}{\pi}\int_0^{\pi}\sin(x)dx=\left.\frac{-\cos(x)}{\pi}\right|_0^{\pi}=\frac{2}{\pi}$$

$$a_n=\frac{2}{\pi}\int_0^{\pi}\sin(x)\cos(nx)\,dx=\frac{1}{\pi}\int_0^{\pi}\sin((n+1)x)-\sin((n-1)x)\,dx$$

First if $n=1$, we have that

$$a_1=\frac{1}{\pi}\int_0^{\pi}\sin(2x)-\sin(0x)\,dx=\left.\frac{-\cos(2x)}{2\pi}\right|_0^{\pi}=0$$

and for $n\ge 2$

$$a_n=\frac{1}{\pi}\int_0^{\pi}\sin((n+1)x)-\sin((n-1)x)\,dx=\left.\frac{1}{\pi}\left(\frac{-\cos((n+1)x)}{n+1}+\frac{\cos((n-1)x)}{n-1}\right)\right|_0^{\pi}$$

$$=\left\{\begin{array}{ll}-\displaystyle\frac{4}{\pi}\frac{1}{n^2-1}&\text{if n is even,}\\ 0&\text{if n is odd.}\end{array}\right.$$

Therefore we have that the Fourier series of $f(x)$ is

$$\frac{2}{\pi}-\frac{4}{\pi}\sum_{n\ \text{even}}\frac{1}{n^2-1}\cos(nx)=\frac{2}{\pi}-\frac{4}{\pi}\sum_{n=1}^{\infty}\frac{1}{4n^2-1}\cos(2nx)$$

**b)** First observe that $f(x)$ is continuous at 0, so we have that

$$0=f(0)=\frac{2}{\pi}-\frac{4}{\pi}\sum_{n=1}^{\infty}\frac{1}{4n^2-1}\cos(2n0)=\frac{2}{\pi}-\frac{4}{\pi}\sum_{n=1}^{\infty}\frac{1}{4n^2-1}\,,$$

therefore

$$\sum_{n=1}^{\infty}\frac{1}{4n^2-1}=\frac{1}{2}$$

Kildesett: course=TMA4130 term=host year=2014 problem=1 file=eksam2014.pdf
