### **Løsning til Oppgave 1**

Lagrange interpolasjon:

$$p_2(x)=f(1)\frac{(x-1.5)(x-2)}{(1-1.5)(1-2)}+f(1.5)\frac{(x-1)(x-2)}{(1.5-1)(1.5-2)}+f(2)\frac{(x-1)(x-1.5)}{(2-1)(2-1.5)}$$

$$=2x^2-7x+6+\frac{2}{3}(-4x^2+12x-8)+\frac{1}{2}(2x^2-5x+3)$$

$$=\frac{1}{3}x^2-\frac{3}{2}x+\frac{13}{6}.$$

Newton interpolasjon:

$$\begin{array}{c|c|ccc}x_i&f(x_i)\\ \hline 1&1\\ &&-2/3\\ 3/2&2/3&&1/3\\ &&-1/3\\ 2&1/2\end{array}$$

og

$$p_2(x)=1-\frac{2}{3}(x-1)+\frac{1}{3}(x-1)\left(x-\frac{3}{2}\right)=\frac{1}{3}x^2-\frac{3}{2}x+\frac{13}{6}.$$

Til sist bruker vi

$$\int_1^2 f(x)dx\approx\int_1^2 p_2(x)dx=\frac{25}{36}.$$

*Ikke en del av oppgaven:* Den feilen som blir gjort her er altså

$$\int_1^2 f(x)dx-\int_1^2 p_2(x)dx=\ln 2-\frac{25}{36}=-1.2\cdot 10^{-3}$$

*Kjeldevarsel: Differansen $\ln 2-\frac{25}{36}$ er $-0.001297\ldots$, vanleg avrunda $-1.3\cdot 10^{-3}$; LF skriv $-1.2\cdot 10^{-3}$ (avkorta mot null) — bevart ordrett. Polynomet $\frac{1}{3}x^2-\frac{3}{2}x+\frac{13}{6}$, dividerte differansar og integraltilnærminga $\frac{25}{36}$ er kontrollreikna med sympy utan avvik.*

Kildesett: course=TMA4125 term=var year=2012 problem=1 file=tma4123_25_v12.pdf
