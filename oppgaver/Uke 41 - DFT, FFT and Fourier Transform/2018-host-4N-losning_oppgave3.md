### **Løsning til Oppgave 3**

**Mat 4N:** Show that for $a\neq 0$

$$\mathcal{F}(f(at))(\omega)=\frac{1}{|a|}\mathcal{F}(f(t))(\frac{\omega}{a})$$

Recall that by definition we have

$$\hat{f}(\omega)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-i\omega x}\,dx.$$

Thus with $a\neq 0$ we have

$$\mathcal{F}(f(at))(\omega)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(at)e^{-i\omega t}\,dt.$$

Now replace $at$ by $x$, we get $dx=a\,dt$, or $t=x/a$ and $dt=\frac{1}{a}dx$. Then, for $a>0$ we find

$$\mathcal{F}(f(at))(\omega)=\frac{1}{a}\mathcal{F}(f(t))(\frac{\omega}{a}).$$

For $a<0$ we obtain

$$\mathcal{F}(f(at))(\omega)=-\frac{1}{a}\mathcal{F}(f(t))(\frac{\omega}{a}).$$

This implies that for $a\neq 0$

$$\mathcal{F}(f(at))(\omega)=\frac{1}{|a|}\mathcal{F}(f(t))(\frac{\omega}{a}).$$

Kildesett: course=TMA4135 term=host year=2018 problem=3 points=6 file=exam_fall18_tma4130_norsk.pdf
