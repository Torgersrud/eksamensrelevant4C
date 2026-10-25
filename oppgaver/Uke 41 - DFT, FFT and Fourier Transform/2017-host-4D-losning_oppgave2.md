### **Løsning til Oppgave 2**

Observer først at venstresiden er konvolusjonen mellom $f$ og $e^{-|x|}$, slik at ligningen kan skrives

$$f(x)*e^{-|x|}=e^{\frac{-x^2}{2}}.$$

Vi fouriertransformerer begge sider, bruker konvolusjonsteoremet

$$\sqrt{2\pi}\mathcal{F}(f)\mathcal{F}(e^{-|x|})=\mathcal{F}(e^{\frac{-x^2}{2}}),$$

og tabell, slik at

$$\mathcal{F}(f)=\frac{1}{\sqrt{2\pi}}\frac{e^{-\omega^2/2}}{\sqrt{\frac{2}{\pi}}\frac{1}{\omega^2+1}}=\frac{-1}{2}\left(-\omega^2e^{-\omega^2/2}\right)+\frac{1}{2}\left(e^{-\omega^2/2}\right).$$

Vi bruker identiteten $\mathcal{F}(f')=iw\mathcal{F}(f)$, koker litt rundt og inverstransformerer, og får

$$f(x)=\frac{-1}{2}(e^{-x^2/2})''+\frac{1}{2}e^{-x^2/2}=\frac{-1}{2}(x^2-1)e^{-x^2/2}+\frac{1}{2}e^{-x^2/2}=\left(-\frac{x^2}{2}+1\right)e^{-x^2/2}.$$

Kildesett: course=TMA4135 term=host year=2017 problem=2 file=tma4135_eksamen_h17.pdf
