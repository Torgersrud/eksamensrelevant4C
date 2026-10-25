### **Løsning til Oppgave 2**

**a)** Et Newton-differensskjema for interpolasjonsdataene er

$$\begin{array}{r|c|l|l}
-1&e^{-1}&&\\
&&\frac{1-e^{-1}}{0-(-1)}=1-e^{-1}&\\
0&1&&\frac{e^{-1}-1-(1-e^{-1})}{1-(-1)}=e^{-1}-1\\
&&\frac{e^{-1}-1}{1-0}=e^{-1}-1&\\
1&e^{-1}&&
\end{array}\,,$$

som gir polynomet

$$\begin{aligned}p(x)&=e^{-1}+(1-e^{-1})(x-(-1))+(e^{-1}-1)(x-(-1))(x-0)\\
&=1+(e^{-1}-1)x^2.\end{aligned}$$

**b)** Vi har

$$I=\int_{-1}^{1}p(x)\,\mathrm{d}x=\int_{-1}^{1}1\,\mathrm{d}x+(e^{-1}-1)\int_{-1}^{1}x^2\,\mathrm{d}x=2+\frac{2}{3}(e^{-1}-1).$$

Integralet $I$ er nettopp Simpsons metodes tilnærming til

$$\int_{-1}^{1}e^{-x^2}\,\mathrm{d}x$$

med $2m=2$ skritt. Vi vet at feilen i Simpsons metode, altså

$$\left|I-\int_{-1}^{1}e^{-x^2}\,\mathrm{d}x\right|,$$

er begrenset av

$$\frac{M\cdot(b-a)^5}{180\cdot(2m)^4}=\frac{M}{90},$$

hvor $M$ er en konstant slik at $|f^{(4)}(x)|\le M$ for alle $x\in[-1,1]$, hvor $f^{(4)}$ er den fjerdederiverte til integranden. I vårt tilfelle er

$$f^{(4)}(x)=e^{-x^2}(16x^4-48x^2+12).$$

Vi har $|f^{(4)}(x)|\le|16x^4-48x^2+12|$, og ved å analysere dette polynomet på vanlig måte, ser vi at det har maksimum på intervallet $[-1,1]$ når $x=0$. Med $M=f^{(4)}(0)=12$ finner vi da

$$\left|I-\int_{-1}^{1}e^{-x^2}\,\mathrm{d}x\right|\le\frac{12}{90}=\frac{2}{15}.$$

*Kjeldevarsel: Resonnementet for $M$ er slapt slik det er formulert — polynomet $|16x^4-48x^2+12|$ har maksimum $20$ (ikkje $12$) på intervallet, ved $x=\pm1$. Men med Gauss-faktaren rekna med er påstanden likevel korrekt: $|f^{(4)}(x)|$ har faktisk maksimum $12$ ved $x=0$ på $[-1,1]$ (ved $x=\pm1$ er $|f^{(4)}|=20/e\approx 7.36$), så endelege estimat $M=12$ og $\frac{2}{15}$ er rett.*

Kildesett: course=TMA4135 term=host year=2014 problem=2 file=tma4135_14h.pdf
