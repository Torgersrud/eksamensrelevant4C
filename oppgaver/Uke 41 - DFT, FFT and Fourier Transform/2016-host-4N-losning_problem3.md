### **Solution to Problem 3**

We have that

$$\begin{array}{rcl}
\mathcal{F}(xe^{-|x|})&=&\displaystyle\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}xe^{-|x|}e^{-iwx}\,dx=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{0}xe^{x}e^{-iwx}\,dx+\frac{1}{\sqrt{2\pi}}\int_{0}^{\infty}xe^{-x}e^{-iwx}\,dx\\[8pt]
&=&\displaystyle\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{0}xe^{(1-iw)x}\,dx+\frac{1}{\sqrt{2\pi}}\int_{0}^{\infty}xe^{(-1-iw)x}\,dx\\[8pt]
&=&\displaystyle\frac{1}{\sqrt{2\pi}}\left(\frac{xe^{(1-iw)x}}{(1-iw)}-\frac{e^{(1-iw)x}}{(1-iw)^2}\right)\Bigg|_{x=-\infty}^{x=0}+\frac{1}{\sqrt{2\pi}}\left(\frac{xe^{(-1-iw)x}}{(-1-iw)}-\frac{e^{(-1-iw)x}}{(-1-iw)^2}\right)\Bigg|_{x=0}^{x=\infty}\\[8pt]
&=&\displaystyle\frac{1}{\sqrt{2\pi}}\frac{-1}{(1-iw)^2}+\frac{1}{\sqrt{2\pi}}\frac{-(1+iw)^2+(1-iw)^2}{(1+iw)^2(1-iw)^2}\\[8pt]
&=&\displaystyle\frac{1}{\sqrt{2\pi}}\frac{-4iw}{((1+iw)(1-iw))^2}=-\frac{2\sqrt{2}i}{\sqrt{\pi}}\frac{w}{(1+w^2)^2}\,,
\end{array}$$

as desired.

For the last part, we use the inverse of the Fourier transform, that is,

$$xe^{-|x|}=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}-\frac{2\sqrt{2}i}{\sqrt{\pi}}\frac{w}{(1+w^2)^2}e^{iwx}\,dw=-\frac{2}{\pi}\int_{-\infty}^{\infty}i\frac{w}{(1+w^2)^2}e^{iwx}\,dw\,.$$

Now if we set $x=1$ we have that

$$\begin{array}{rcl}
e^{-1}&=&\displaystyle-\frac{2}{\pi}\int_{-\infty}^{\infty}i\frac{w}{(1+w^2)^2}e^{iw}\,dw=-\frac{2}{\pi}\int_{-\infty}^{\infty}i\frac{w}{(1+w^2)^2}(\cos w+i\sin w)\,dw\\[8pt]
&=&\displaystyle-i\frac{2}{\pi}\int_{-\infty}^{\infty}\frac{w}{(1+w^2)^2}\cos w\,dw+\frac{2}{\pi}\int_{-\infty}^{\infty}\frac{w}{(1+w^2)^2}\sin w\,dw
\end{array}$$

But then observe that $\int_{-\infty}^{\infty}\frac{w}{(1+w^2)^2}\cos w\,dw=0$ because $\frac{w}{(1+w^2)^2}\cos w$ is an odd function, so it follows that

$$e^{-1}=\frac{2}{\pi}\int_{-\infty}^{\infty}\frac{w}{(1+w^2)^2}\sin w\,dw$$

whence

$$\frac{\pi}{2e}=\int_{-\infty}^{\infty}\frac{w}{(1+w^2)^2}\sin w\,dw\,.$$

Kildesett: course=TMA4130 term=host year=2016 problem=3 file=n16h.pdf
