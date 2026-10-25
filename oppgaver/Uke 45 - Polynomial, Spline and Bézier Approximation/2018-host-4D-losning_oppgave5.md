### **Løsning til Oppgave 5**

In this case, the easy solution is to use finite differences and Newton interpolation. The table of finite differences is:

| $x_i$ | $y_i$ | | | |
|---|---|---|---|---|
| $-2$ | $0$ | | | |
| $0$ | $1$ | $1/2$ | | |
| $1$ | $9/8$ | $1/8$ | $-1/8$ | |
| $2$ | $0$ | $-9/8$ | $-5/8$ | $-1/8$ |

and the interpolation polynomial becomes:

$$p(x)=\frac{1}{2}(x+2)-\frac{1}{8}(x+2)x-\frac{1}{8}(x+2)x(x-1)=1+\frac{1}{2}x-\frac{1}{4}x^2-\frac{1}{8}x^3.$$

Kildesett: course=TMA4135 term=host year=2018 problem=5 points=10 file=exam_fall18_tma4130_norsk.pdf
