### **Løsning til Oppgave 5**

Integrallikninga kan skrives på formen

$$xe^{-x^2}=(f*g)(x), \tag{*}$$

der $g(x)=e^{-2x^2}$.

For en passende funksjon $H$ gjelder det at $\mathscr{F}(H')=i\omega\mathscr{F}(H)$. La

$$H(x)=-\frac{1}{2a}e^{-ax^2},\quad a>0,$$

og la $h(x)=xe^{-ax^2}$. Legg merke til at $H'=h$. Det gir

$$\hat{h}(\omega)=\mathscr{F}(h)(\omega)=i\omega\mathscr{F}(H)(\omega)=-\frac{i\omega}{(2a)^{3/2}}e^{-\frac{\omega^2}{4a}}.$$

La $\hat{f}=\mathscr{F}(f)$. Fouriertransformasjon anvendt på (*) gir så

$$-\frac{i\omega}{2\sqrt{2}}e^{-\frac{\omega^2}{4}}=\sqrt{2\pi}\hat{f}(\omega)\cdot\frac{1}{2}e^{-\frac{\omega^2}{8}},$$

der vi har satt $a=1$ i uttrykket for $\hat{h}(\omega)$ og brukt at $\mathscr{F}(f*g)=\sqrt{2\pi}\mathscr{F}(f)\mathscr{F}(g)$. Det gir

$$\hat{f}(\omega)=-\frac{i\omega}{2\sqrt{\pi}}e^{-\frac{\omega^2}{8}}=\frac{4}{\sqrt{\pi}}\left(-\frac{i\omega}{8}e^{-\frac{\omega^2}{8}}\right).$$

Ved å ta inverstransformen får vi

$$f(x)=\frac{4}{\sqrt{\pi}}xe^{-2x^2}.$$

Kildesett: course=TMA4135 term=host year=2012 problem=5 file=tma4135_12h.pdf
