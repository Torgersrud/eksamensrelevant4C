### **Løsning til Oppgave 2**

La $g_a\colon\mathbb{R}\to\mathbb{R}$ være gitt ved $g_a(x)=e^{-a|x|}$. Den gitte integralligningen kan skrives ved hjelp av konvolusjonsprodukt, det vil si

$$f(x)=g_2(x)-(g_1*f)(x).\tag{1}$$

Fra tabellen vedlagt eksamensoppgavene har vi at

$$\mathscr{F}(g_1)(\omega)=\sqrt{\frac{2}{\pi}}\frac{1}{1+\omega^2}$$

og

$$\mathscr{F}(g_2)(\omega)=\sqrt{\frac{2}{\pi}}\frac{2}{4+\omega^2}.$$

La $\hat{f}=\mathscr{F}(f)$. Fouriertransformasjon anvendt på (1) gir

$$\hat{f}(\omega)=\sqrt{\frac{2}{\pi}}\frac{2}{4+\omega^2}-\frac{2}{1+\omega^2}\hat{f}(\omega),\tag{2}$$

der vi har benyttet at $\mathscr{F}(g_2*f)=\sqrt{2\pi}\mathscr{F}(g_2)\mathscr{F}(f)$. Ved å løse (2) med hensyn på $\hat{f}(\omega)$ får vi

$$\hat{f}(\omega)=\sqrt{\frac{2}{\pi}}\frac{2(1+\omega^2)}{(3+\omega^2)(4+\omega^2)}=\sqrt{\frac{2}{\pi}}\left(\frac{6}{4+\omega^2}-\frac{4}{3+\omega^2}\right),$$

der den siste likheten fremkommer ved delbrøkoppspalting. Invers transformasjon gir

$$f(x)=3e^{-2|x|}-\frac{4}{\sqrt{3}}e^{-\sqrt{3}|x|}.$$

Kildesett: course=TMA4135 term=host year=2013 problem=2 file=tma4135_13h.pdf
