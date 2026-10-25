### **Løsning til Oppgave 4**

Ligningen kan skrives på formen:

$$y(x)*e^{-2x^2}=e^{-x^2}. \tag{4}$$

Fouriertransformerer denne:

$$\sqrt{2\pi}\cdot\mathcal{F}(y)\cdot\mathcal{F}(e^{-2x^2})=\mathcal{F}(e^{-x^2})\qquad\Rightarrow\qquad\sqrt{2\pi}\cdot\hat{y}(w)\cdot\frac{1}{2}e^{-\frac{w^2}{8}}=\frac{1}{\sqrt{2}}e^{-\frac{w^2}{4}}$$

$$\Rightarrow\qquad\hat{y}(w)=\frac{1}{\sqrt{\pi}}e^{-\frac{w}{8}}$$

og

$$y(x)=\mathcal{F}^{-1}(\hat{y})=\frac{2}{\sqrt{\pi}}e^{-2x^2}.$$

*Kjeldevarsel: I uttrykket for $\hat{y}(w)$ er eksponenten trykt som $-\frac{w}{8}$ utan kvadrat — både utrekninga over og inversjonen under krev $-\frac{w^2}{8}$; trykkfeila er bevart ordrett. Heile løysinga er kontrollreikna med sympy: $\int_{-\infty}^{\infty}\frac{2}{\sqrt{\pi}}e^{-2p^2}e^{-2(x-p)^2}dp=e^{-x^2}$ treffer eksakt, og transformpara $\mathcal{F}(e^{-2x^2})=\frac{1}{2}e^{-w^2/8}$, $\mathcal{F}(e^{-x^2})=\frac{1}{\sqrt{2}}e^{-w^2/4}$ følgjer same konvolusjonsregel $\hat{\ }{(f*g)}=\sqrt{2\pi}\hat{f}\hat{g}$ som i dei andre 4N-losningane (normalisering $1/\sqrt{2\pi}$).*

Kildesett: course=TMA4125 term=var year=2012 problem=4 file=tma4123_25_v12.pdf
