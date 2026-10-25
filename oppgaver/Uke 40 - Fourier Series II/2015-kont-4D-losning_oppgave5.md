### **Løsning til Oppgave 5**

**a)** Vi har

$$f(x)= \begin{cases} \cos(x), & \text{for } x\in(0,\pi), \\ -\cos(x), & \text{for } x\in(-\pi,0), \end{cases} \qquad (10)$$

og slik at $f(x+2\pi)=f(x)$. ($f$ har faktisk periode $\pi$.)

[Figur: Grafen til $\bar f$: ei rekkje fallande cosinusforma bogar som går frå $1$ ned til $-1$ på kvart intervall $(n\pi,(n+1)\pi)$, med hopp opp att til $1$ ved $x=n\pi$. $x$-aksen er merkt frå $-10$ til $10$, den loddrette aksen er merkt $1.0$ og $-1.0$.]

**b)** Funksjonen $f$ oppfyller betingelsene for konvergens av Fourier-rekken, se Teorem 2, s. 480. La $S(x)$ betegne summen av Fourier-rekken. Da gjelder

$$S(x)=\frac{1}{2}\big(f(x+)+f(x-)\big),$$

der $f(x\pm)$ betegner (ensidige) høyre og venstre grenseverdier. Der betyr at

$$\begin{aligned}S(0)&=\frac{1}{2}\big(f(0+)+f(0-)\big)=0,\\ S\left(\frac{\pi}{4}\right)&=\frac{1}{2}\left(f\left(\frac{\pi}{4}+\right)+f\left(\frac{\pi}{4}-\right)\right)=f\left(\frac{\pi}{4}\right)=\cos\left(\frac{\pi}{4}\right)=\frac{\sqrt{2}}{2},\\ S(-4\pi)&=S(0)=0.\end{aligned}$$

*(Oppgavens punkt c) gjekk ut av eksamen — sjå Kjeldevarselet i oppgåveteksten. Løsningsforslaget reknar likevel dette punktet ut; det er utelatt her.)*

Kildesett: course=TMA4135 term=kont year=2015 problem=5 file=tma4135_15k.pdf
