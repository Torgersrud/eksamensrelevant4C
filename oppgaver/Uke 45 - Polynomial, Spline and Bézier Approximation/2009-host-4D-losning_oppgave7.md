### **Løsning til Oppgave 7**

Differansetabellen blir seende slik ut.

Dividerte differanser på det gitte datasettet gir:

$$
\begin{aligned}
f_0 &= 1 \\
f[x_0, x_1] &= -1 \\
f[x_0, x_1, x_2] &= 1 \\
f[x_0, x_1, x_2, x_3] &= 0 \\
f[x_0, x_1, x_2, x_3, x_4] &= 0
\end{aligned}
$$

Interpolasjonspolynomet er dermed gitt som:

$$
\begin{aligned}
p(x) = f_0 &+ (x - x_0)f[x_0, x_1] + (x - x_0)(x - x_1)f[x_0, x_1, x_2] \\
&+ (x - x_0)(x - x_1)(x - x_2)f[x_0, x_1, x_2, x_3] \\
&+ (x - x_0)(x - x_1)(x - x_2)(x - x_3)f[x_0, x_1, x_2, x_3, x_4] \\
= 1 &+ (x - (-1)) \cdot (-1) + (x - (-1))(x - 1) \cdot 1 \\
&+ (x - (-1))(x - 1)(x - 2) \cdot 0 + (x - (-1))(x - 1)(x - 2)(x - 3) \cdot 0 \\
= \; &x^2 - x - 1.
\end{aligned}
$$

Kildesett: course=TMA4135 term=host year=2009 problem=7 file=tma4135_09h.pdf
