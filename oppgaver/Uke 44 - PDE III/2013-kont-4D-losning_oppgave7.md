### **Løsning til Oppgave 7**

**a)** La funksjonen $\hat{u}$ være gitt ved å anvende fouriertransformasjon på $u$ med hensyn på $x$,

$$\hat{u}(\omega,t)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}u(x,t)e^{-i\omega x}\,\mathrm{d}x.$$

Fra egenskapene til fouriertransformasjon får vi at

$$\mathscr{F}(u_{xx})=-\omega^2\hat{u}.$$

Fouriertransformasjon anvendt på den partielle differensiallikningen gitt i oppgaven gir

$$\frac{\partial\hat{u}}{\partial t}=-\omega^2\hat{u}.$$

Fouriertransformasjon anvendt på initialbetingelsen gir

$$\hat{u}_t(\omega,0)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}u_t(x,0)e^{-i\omega x}\,\mathrm{d}x=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-i\omega x}\,\mathrm{d}x=\hat{f}(\omega).$$

Altså kan vi, ved å anvende fouriertransformasjon, skrive det gitte problemet som initialverdiproblemet

$$\frac{\partial\hat{u}}{\partial t}=-\omega^2\hat{u},\quad\hat{u}_t(\omega,0)=\hat{f}(\omega).\tag{3}$$

**b)** Hvis vi fikserer $\omega$ kan vi skrive (3) som den ordinære differensiallikningen

$$\frac{\mathrm{d}\hat{u}}{\mathrm{d}t}=-\omega^2\hat{u},\quad\hat{u}_t(\omega,0)=\hat{f}(\omega),$$

som har løsning

$$\hat{u}(\omega,t)=C(\omega)e^{-\omega^2t}.$$

Fra $\hat{u}_t(\omega,0)=\hat{f}(\omega)$ får vi

$$\hat{u}_t(\omega,0)=-\omega^2C(\omega)=\hat{f}(\omega).$$

Altså er

$$\hat{u}(\omega,t)=-\frac{1}{\omega^2}\hat{f}(\omega)e^{-\omega^2t}.$$

Ettersom $\hat{f}=\mathscr{F}(g'')=-\omega^2\hat{g}$ forenkler dette seg til

$$\hat{u}(\omega,t)=\hat{g}(\omega)e^{-\omega^2t}.\tag{4}$$

**c)** La funksjonen $\hat{h}$ være gitt ved

$$\hat{h}(\omega,t)=\frac{1}{\sqrt{2\pi}}e^{-\omega^2t},$$

slik at (4) kan skrives som

$$\hat{u}(\omega,t)=\sqrt{2\pi}\,\hat{g}(\omega)\,\hat{h}(\omega,t).\tag{5}$$

Ved å ta invers_transformasjonen av (5) får vi

$$u(x,t)=\int_{-\infty}^{\infty}g(x-p)h(p,t)\,\mathrm{d}p,$$

der

$$h(p,t)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\hat{h}(\omega,t)e^{i\omega p}\,\mathrm{d}\omega=\frac{1}{2\sqrt{\pi t}}\underbrace{\left(\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\sqrt{2t}\,e^{-\omega^2t}e^{i\omega p}\,\mathrm{d}\omega\right)}_{e^{-p^2/4t}}=\frac{1}{2\sqrt{\pi t}}e^{-p^2/4t},\quad t>0,$$

hvor vi har benyttet den oppgitte fouriertransformasjonen (i formelarket)

$$\mathscr{F}\{e^{-ax^2}\}=\frac{1}{\sqrt{2a}}e^{-\frac{\omega^2}{4a}}$$

med $a=1/4t$. Altså har vi at

$$u(x,t)=\frac{1}{2\sqrt{\pi t}}\int_{-\infty}^{\infty}g(x-p)\,e^{-p^2/4t}\,\mathrm{d}p,\quad t>0.$$

Kildesett: course=TMA4135 term=kont year=2013 problem=7 file=tma4135_13k.pdf
