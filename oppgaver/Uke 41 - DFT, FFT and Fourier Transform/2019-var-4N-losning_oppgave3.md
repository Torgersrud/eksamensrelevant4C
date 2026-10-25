### **Løsning til Oppgave 3**

Funksjonen

$$-u(x+1)+2u(x)+u(x-1)=\begin{cases}-1 & -1\le x<0\\ 1 & 0\le x<1\\ 0 & \text{ellers}\end{cases}$$

ser slik ut:

[Figure: trappefunksjon over $[-2,2]$: $-1$ på $[-1,0)$, $+1$ på $[0,1)$, ellers $0$.]

*Kjeldevarsel: fasitfila skriv pluss-teikn framfor $u(x-1)$ i uttrykket over, men stykkefunksjonen, plottet og rekninga under svarer til eksamensutgåva $-u(x+1)+2u(x)-u(x-1)$ (sjå `eksamen-TMA4125-v19-BM.pdf`), og det er dette som er rekna ut. Pluss-teiknet er ein trykkfeil i fasitfila — en av to feil merkta på old_exams-sida.*

Fouriertransformen blir:

$$\begin{aligned}\mathcal{F}(u)&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}u(x)e^{-iwx}\,dx=\frac{1}{\sqrt{2\pi}}\left(-\int_{-1}^{0}e^{-iwx}\,dx+\int_{0}^{1}e^{-iwx}\,dx\right)\\
&=\frac{1}{\sqrt{2\pi}}\left(\frac{1}{iw}(1-e^{iw})+\frac{1}{iw}(1-e^{-iw})\right)=\sqrt{\frac{2}{\pi}}\frac{1}{iw}(1-\cos w).\end{aligned}$$

Kildesett: course=TMA4125 term=var year=2019 problem=3 file=eksamen-TMA4125-v19-BM.pdf
