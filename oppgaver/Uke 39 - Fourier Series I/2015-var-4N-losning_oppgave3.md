### **Løsning til Oppgave 3**

a) Figur 1 viser grafen til den $2\pi$-periodiske utvidelsen av $f$.

[Figure: Horisontal akse med merke og etikettene $-2\pi$, $-\pi$, $0$, $\pi$, $2\pi$, $3\pi$, $4\pi$ og en vertikal akse. Ei solid linjestrek er grafen til $(\pi-x)/2$ på $(0,2\pi)$: ho startar i høgd $\pi/2$ ved $x=0$, går gjennom null i $x=\pi$ og endar i $-\pi/2$ ved $x=2\pi$. Stipla strekar viser den odde $2\pi$-periodiske utvidelsen på $(-2\pi,0)$ og $(2\pi,4\pi)$. Punkt på aksen ved $-2\pi$, $0$ og $2\pi$ markerer at funksjonen er $0$ i desse punkta.]

Figur 1: Grafen til den $2\pi$-periodiske utvidelsen til funksjonen i oppgave 3a. Den heltrukne linjen er definisjonsområdet til den opprinnelige funksjonen, mens den stiplede er utvidelsen.

Utvidelsen til $f$ er odde, så vi vet umiddelbart at $a_0=a_1=a_2=...=0$. Videre er

$$\begin{array}{rl}b_n=&\displaystyle\frac{2}{\pi}\int_0^\pi f(x)\sin nx\,\mathrm{d}x=\int_0^\pi\sin nx\,\mathrm{d}x-\frac{1}{\pi}\int_0^\pi x\sin nx\,\mathrm{d}x\\[10pt] =&\displaystyle-\frac{1}{n}\left[\cos nx\right]_{x=0}^{x=\pi}-\frac{1}{\pi n^2}\left[\sin nx-nx\cos nx\right]_{x=0}^{x=\pi}\\[10pt] =&\displaystyle\frac{1+(-1)^{n+1}}{n}+\frac{1}{n}(-1)^n=\frac{1}{n}.\end{array}$$

Fourier-rekken til den $2\pi$-periodiske utvidelsen til $f$ er derfor

$$\sum_{n=1}^{\infty}\frac{1}{n}\sin nx.$$

b) Siden (den $2\pi$-periodiske utvidelsen til) $f$ er kontinuerlig i $\pi/2$, er

$$\frac{\pi}{4}=f\left(\frac{\pi}{2}\right)=\sum_{n=1}^{\infty}\frac{1}{n}\sin\frac{n\pi}{2}=1+\sum_{n=2}^{\infty}\frac{1}{n}\sin\frac{n\pi}{2}.$$

Siden

$$\sin\frac{n\pi}{2}=\begin{cases}1&\text{for }n=1,5,9,...\\ -1&\text{for }n=3,7,11,...\\ 0&\text{ellers},\end{cases}$$

er

$$\frac{\pi}{4}=1+\sum_{n=2}^{\infty}\frac{1}{n}\sin\frac{n\pi}{2}=1+\sum_{m=1}^{\infty}\frac{(-1)^m}{2m+1},$$

så den første rekken vi ble bedt om er $\pi/4-1$.

For den andre rekken bruker vi Parsevals identitet, som gir

$$2a_0^2+\sum_{n=1}^{\infty}(a_n^2+b_n^2)=\frac{1}{\pi}\int_{-\pi}^{\pi}(g(x))^2\,\mathrm{d}x,$$

hvor $g$ er den $2\pi$-periodiske utvidelsen til $f$. Ved bruk av periodisitet får vi

$$\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{1}{\pi}\int_0^{2\pi}(f(x))^2\,\mathrm{d}x=\frac{1}{\pi}\int_0^{2\pi}\frac{(\pi-x)^2}{4}\,\mathrm{d}x=\frac{\pi^2}{6}.$$

Kildesett: course=TMA4123 term=var year=2015 problem=3 file=eksamen-nb.pdf
