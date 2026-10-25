### **Solution to Problem 1**

First observe that $f(-x)=\cos\left(\frac{-x}{2}\right)=\cos\left(\frac{x}{2}\right)$, so $f(x)$ is an even function. Then the Fourier series of the function $f(x)$ is of the form

$$a_0+\sum_{n=1}^{\infty}a_n\cos(nx)\,.$$

Then

$$\begin{array}{rcl}
a_0&=&\displaystyle\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)\,dx=\frac{1}{\pi}\int_{0}^{\pi}f(x)\,dx\\[8pt]
&=&\displaystyle\frac{1}{\pi}\int_{0}^{\pi}\cos\left(\frac{x}{2}\right)\,dx=\left.\frac{1}{\pi}\frac{\sin\left(\frac{x}{2}\right)}{\frac{1}{2}}\right|_{x=0}^{x=\pi}=\frac{2}{\pi}\,,
\end{array}$$

and

$$\begin{array}{rcl}
a_n&=&\displaystyle\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos(nx)\,dx=\frac{2}{\pi}\int_{0}^{\pi}f(x)\cos(nx)\,dx\\[8pt]
&=&\displaystyle\frac{2}{\pi}\int_{0}^{\pi}\cos\left(\frac{x}{2}\right)\cos(nx)\,dx=\frac{2}{\pi}\int_{0}^{\pi}\frac{1}{2}\left(\cos\left(\frac{2n+1}{2}x\right)+\cos\left(\frac{2n-1}{2}x\right)\right)\,dx\\[8pt]
&=&\displaystyle\frac{1}{\pi}\int_{0}^{\pi}\cos\left(\frac{2n+1}{2}x\right)+\cos\left(\frac{2n-1}{2}x\right)\,dx\\[8pt]
&=&\displaystyle\frac{1}{\pi}\left(\frac{2}{2n+1}\sin\left(\frac{2n+1}{2}x\right)+\frac{2}{2n-1}\sin\left(\frac{2n-1}{2}x\right)\right)\Big|_{x=0}^{x=\pi}\\[8pt]
&=&\displaystyle\frac{1}{\pi}\left(\frac{2}{2n+1}\sin\left(\frac{2n+1}{2}\pi\right)+\frac{2}{2n-1}\sin\left(\frac{2n-1}{2}\pi\right)-0-0\right)\\[8pt]
&=&\displaystyle\frac{1}{\pi}\left(\frac{2}{2n+1}(-1)^n+\frac{2}{2n-1}(-1)^{n+1}\right)=\frac{(-1)^n}{\pi}\left(\frac{2}{2n+1}-\frac{2}{2n-1}\right)\\[8pt]
&=&\displaystyle\frac{(-1)^n}{\pi}\left(\frac{-4}{4n^2-1}\right)=\frac{(-1)^n}{\pi}\left(\frac{4}{1-4n^2}\right)\,.
\end{array}$$

Thus, the Fourier series to $f(x)$ is

$$\frac{2}{\pi}+\sum_{n=1}^{\infty}\frac{(-1)^n}{\pi}\frac{4}{1-4n^2}\cos(nx)\,.$$

Finally to find the value of the series, we evaluate the Fourier series of $f(x)$ at $x=0$, and by the Fourier Theorem and since $f(x)$ is continuous at $x=0$ we have that

$$1=\cos\left(\frac{0}{2}\right)=f(0)=\frac{2}{\pi}+\sum_{n=1}^{\infty}\frac{(-1)^n}{\pi}\frac{4}{1-4n^2}\cos(0)=\frac{2}{\pi}+\frac{4}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^n}{1-4n^2}\,,$$

whence

$$\sum_{n=1}^{\infty}\frac{(-1)^n}{1-4n^2}=\frac{\pi}{4}\left(1-\frac{2}{\pi}\right)=\frac{\pi-2}{4}\,.$$

Kildesett: course=TMA4130 term=host year=2016 problem=1 file=n16h.pdf
