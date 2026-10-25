### **Løsning til Oppgave 4**

$u_t=u_{xx}$, $u(x,0)=e^{-x^2}$

Now takeing fourier transforms with respect to $x$ gives

$$\hat{u}_t(\omega,t)=-\omega^2\hat{u}(\omega,t)$$

$$\Rightarrow\quad \hat{u}=\hat{u}(\omega,0)\,e^{-\omega^2t}$$

where

$$\begin{aligned}
\hat{u}(\omega,0)&=\mathcal{F}\big(u(x,0)\big)\\
&=\mathcal{F}\big(e^{-x^2}\big)\\
&=\frac{1}{\sqrt{2}}\,e^{-\omega^2/4}
\end{aligned}$$

here $\hat{u}=\frac{1}{\sqrt{2}}\,e^{-\omega^2/4}e^{-\omega^2t}=\frac{\sqrt{a}}{\sqrt{2a}}\,e^{-\omega^2\left(t+\frac{1}{4}\right)}$

then $\hat{u}=e^{-\omega^2/4a}$, $\frac{1}{4a}=t+\frac{1}{4}=\frac{4t+1}{4}$

$$\Rightarrow\quad a=\frac{1}{4t+1}$$

and

$$u=\mathcal{F}^{-1}\big(\hat{u}\big)=\frac{1}{\sqrt{4t+1}}\,e^{-\frac{x^2}{4t+1}}$$

Kildesett: course=TMA4125 term=kont year=2017 problem=4 file=kont_bok.pdf
