### **Løsning til Oppgave 4**

Siden intervallene er like store kan vi bruke at

$$\begin{aligned} f(x) = f(-2)\binom{x+2}{0} &+ \Delta f(-2)\binom{x+2}{-2} + \Delta^2 f(-2)\binom{x+2}{2} \\ &+ \Delta^3 f(-2)\binom{x+2}{3} + \Delta^4 f(-2)\binom{x+2}{4}, \end{aligned}$$

der $\Delta f(x_k)$ er foroverdifferansen $f(x_{k+1}) - f(x_k)$.

$$\begin{array}{|c|c|c|c|c|c|} \hline x_k & \text{-2} & \text{-1} & 0 & 1 & 2 \\ \hline f(x_k) & 5 & 1 & \text{-1} & \text{-1} & 1 \\ \hline \Delta f(x_k) & \text{-4} & \text{-2} & 0 & 2 & \\ \hline \Delta^2 f(x_k) & 2 & 2 & 2 & & \\ \hline \Delta^3 f(x_k) & 0 & 0 & & & \\ \hline \end{array}.$$

Dermed blir $f(x) = 5\binom{x+2}{0} - 4\binom{x+2}{-2} + 2\binom{x+2}{2} = x^2 - x - 1$.

*Kjeldevarsel: underindekset i leddet med $\Delta f(-2)$ er trykt som $-2$ både i den utskrivne forma og i «Dermed»-linja; det skal vere $1$. Med $1$ gir rekna $5\binom{x+2}{0} - 4\binom{x+2}{1} + 2\binom{x+2}{2} = x^2 - x - 1$ (sympy-stadfesta) nettop det trykte resultatet, og treffer alle fem datapunkta, mens $\binom{x+2}{-2}$ ikkje gir noka polynomialrekkje; differanstabellen i løysingsforslaget ($\Delta f(-2) = -4$, $\Delta^2 f(-2) = 2$, $\Delta^3 f = 0$) stadfestar ledd med indeks 1. elles ordrett. Løysingsforslaget si overskrift seier elles «13. august 2009» medan eksamenarket og sidefoten seier 10. august 2009.*

Kildesett: course=TMA4130 term=sommer year=2009 problem=4 file=eksamen-bok_2009s.pdf
