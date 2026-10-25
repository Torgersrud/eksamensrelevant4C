### **Løsning til Oppgave 1**

Oppgaven kan, for eksempel, løses ved hjelp av Lagrange-interpolasjon eller Newtons interpolasjonsformel.

* *Lagrange-interpolasjon:*

$$
\begin{aligned}
p(x)&=3.0\frac{x(x-1)(x-2)}{-1(-1-1)(-1-2)}+0.5\frac{(x+1)(x-1)(x-2)}{1(-1)(-2)}\\
&\quad-1.0\frac{(x+1)x(x-2)}{(1+1)1(1-2)}-1.5\frac{(x+1)x(x-1)}{(2+1)2(2-1)}\\
&=-\frac{1}{2}(x^3-3x^2+2x)+\frac{1}{4}(x^3-2x^2-x+2)\\
&\quad+\frac{1}{2}(x^3-x^2-2x)-\frac{1}{4}(x^3-x)\\
&=0.5x^2-2.0x+0.5
\end{aligned}
$$

* *Newtons interpolasjonsformel:* Tabellen over dividerte differenser er gitt ved

$$\begin{array}{|cc|ccc|}\hline x_i&f(x_i)&f[x_i,x_{i+1}]&f[x_i,x_{i+1},x_{i+2}]&f[x_i,\ldots,x_{i+3}]\\ \hline -1.0&3.0&&&\\ &&-2.5&&\\ 0.0&0.5&&0.5&\\ &&-1.5&&0.0\\ 1.0&-1.0&&0.5&\\ &&-0.5&&\\ 2.0&-1.5&&&\\ \hline\end{array}$$

så interpolasjonspolynomet blir

$$
\begin{aligned}
p(x)&=3.0-2.5(x+1.0)+0.5(x+1.0)x+0.0(x+1.0)x(x-1.0)\\
&=0.5x^2-2.0x+0.5.
\end{aligned}
$$

Kildesett: course=TMA4135 term=host year=2010 problem=1 file=tma4135_10h.pdf
