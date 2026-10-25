### **Løsning til Oppgave 2**

**a)** Definisjon av fouriertransformen gir oss

$$\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{\sin ax}{x}e^{-i\omega x}\mathrm{d}x=\begin{cases}\ \sqrt{\frac{\pi}{2}},&|\omega|<a,\\ 0,&a<|\omega|\end{cases}\tag{1}$$

Hvis vi setter $a=1$ og $\omega=0$, får vi

$$\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{\sin x}{x}\mathrm{d}x=\sqrt{\frac{\pi}{2}},$$

og følgelig blir

$$\int_{-\infty}^{\infty}\frac{\sin x}{x}\mathrm{d}x=\pi.$$

For det neste integralet må vi benytte at $\frac{\sin ax}{x}$ er en *like* funksjon, og vi kan dermed forenkle FT ved å observere at

$$\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{\sin ax}{x}e^{-i\omega x}\mathrm{d}x=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{\sin ax}{x}\left(\cos\omega x-i\sin\omega x\right)\mathrm{d}x$$

$$=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{\sin ax}{x}\cos\omega x\mathrm{d}x.$$

Hvis vi lar $\omega=1$ vil, etter lign. 1,

$$\int_{-\infty}^{\infty}\frac{\sin ax}{x}\cos x\mathrm{d}x=\sqrt{2\pi}\sqrt{\frac{\pi}{2}}=\begin{cases}\ \pi,&1<a,\\ \ 0,&a<1\end{cases}$$

Det gjenstår å sjekke $a=1$, men her observerer vi at

$$\int_{-\infty}^{\infty}\frac{\sin x}{x}\cos x\mathrm{d}x=\int_{-\infty}^{\infty}\frac{\sin 2x}{2x}\frac{1}{2}\mathrm{d}\left(2x\right)\overset{t=2x}{=}\frac{1}{2}\int_{-\infty}^{\infty}\frac{\sin t}{t}\mathrm{d}t=\frac{\pi}{2}.$$

**b)** Fra den oppgitte fouriertransformen ser vi at

$$\mathcal{F}\left(\frac{1}{\pi}\frac{\sin ax}{x}\right)=\frac{1}{\pi}\times\sqrt{\frac{\pi}{2}}=\begin{cases}\frac{1}{\sqrt{2\pi}}&\text{for}\ |\omega|<a,\\ 0&\text{for}\ |\omega|>a.\end{cases}$$

Dette betyr at FT til $g=h_a*f$ vil være

$$\hat{g}(\omega)=\sqrt{2\pi}\hat{h}_a(\omega)\,\hat{f}(\omega)=\begin{cases}\ \hat{f}(\omega)\,,&|\omega|<a,\\ \ \ 0,&a<|\omega|\,.\end{cases}$$

Filteret ”kapper av” FT til signalet utenfor intervallet $[-a,a]$ (Dette kalles en *lavpassfiltrering* av signalet).

Legg merke til at alle funksjoner $f$ der $\hat{f}(\omega)$ er null for $|\omega|\geq a$ går uforandret gjennom filteret. Vi kan også observere at

$$\lim_{a\to\infty}\hat{h}_a(\omega)=\frac{1}{\sqrt{2\pi}}$$

for alle $\omega$. En kan derfor si at grensen for $h_a$ når $a\to\infty$ må være *deltafunksjonen*, $\delta(x)$, siden $\hat{\delta}(\omega)=\frac{1}{\sqrt{2\pi}}$ for alle $\omega$.

Kildesett: course=TMA4125 term=var year=2011 problem=2 file=tma4125nbokmaal.pdf
