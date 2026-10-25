### **Løsning til Oppgave 4**

**a)** Ved å bruker tilnærmingene

$$\begin{aligned} u_{xx}(x_i, y_j) &\approx \frac{u_{i-1,j} + u_{i+1,j} - 2u_{i,j}}{h^2}, \\ u_{yy}(x_i, y_j) &\approx \frac{u_{i,j-1} + u_{i,j+1} - 2u_{i,j}}{h^2} \end{aligned}$$

i hvert punkt $(x_i, y_j)$ får man den følgende numeriske metoden

$$\frac{u_{i-1,j} + u_{i+1,j} + u_{i,j-1} + u_{i,j+1} - 4u_{i,j}}{h^2} = x_i u_{i,j} \tag{L-10}$$

I punktet $(x_1, y_1) = (h, h)$, siden $u_{1,0} = x_1 = h$ og $u_{0,1} = 0$, blir (L-10) til

$$\frac{u_{21} + u_{12} + h - 4u_{11}}{h^2} = h u_{11}$$

som kan skrives om

$$27u_{21} + 27u_{12} - 109u_{11} = -9$$

der vi har brukt at $h = \frac{1}{3}$.

I punktet $(x_2, y_1) = (2h, h)$, siden $u_{2,0} = x_2 = 2h$ og $u_{3,1} = 1$, blir (L-10) til

$$\frac{1 + u_{22} + u_{112} + 2h - 4u_{21}}{h^2} = 2h u_{21}$$

som kan skrives om

$$27u_{22} + 27u_{11} - 110u_{21} = -45.$$

I punktet $(x_1, y_2) = (h, 2h)$, siden $u_{1,3} = x_1 = h$ og $u_{0,2} = 0$, blir (L-10) til

$$\frac{u_{11} + u_{22} + h - 4u_{12}}{h^2} = h u_{12}$$

som kan skrives om

$$27u_{22} + 27u_{11} - 109u_{12} = -9.$$

I punktet $(x_2, y_2) = (2h, 2h)$, siden $u_{2,3} = x_2 = 2h$ og $u_{3,2} = 1$, blir (L-10) til

$$\frac{2h + 1 + u_{12} + u_{21} - 4u_{22}}{h^2} = 2h u_{22}$$

som kan skrives om

$$27u_{12} + 27u_{21} - 110u_{22} = -45.$$

Til slutt, får vi det følgende systemet

$$\begin{aligned} -109 \, u_{11} \ + \ \ 27 \, u_{21} \ \ + \ \ 27 \, u_{12} \ &= \ -9 \\ 27 \, u_{11} \ \ - \ \ 110 \, u_{21} \ \ + \ \ \ \ \ \ \ \ \ \ \ \ \ \ 27 \, u_{22} \ &= \ -45 \\ 27 \, u_{11} \ \ \ \ \ \ \ \ \ \ - \ \ 109 \, u_{12} \ \ + \ \ 27 \, u_{22} \ &= \ -9 \\ 27 \, u_{21} \ \ + \ \ 27 \, u_{12} \ \ - \ \ 110 \, u_{22} \ &= \ -45 \end{aligned}$$

for $(u_{11}, u_{21}, u_{12}, u_{22})$.

**b)** Gauss-Seidel metoden kan skrives som

$$\begin{aligned} -109 \, x_1^{(k+1)} \ \ + \ \ \ 27 \, x_2^{(k)} \ \ \ \ + \ \ \ \ 27 \, x_3^{(k)} \ \ \ \ \ \ \ \ \ \ \ &= \ -9 \\ 27 \, x_1^{(k+1)} \ \ - \ \ 110 \, x_2^{(k+1)} \ \ + \ \ \ \ \ \ \ \ \ \ \ \ \ \ 27 \, x_4^{(k)} \ \ \ \ \ \ &= \ -45 \\ 27 \, x_1^{(k+1)} \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ - \ \ 109 \, x_3^{(k+1)} \ \ + \ \ \ 27 \, x_4^{(k)} \ \ \ \ \ \ &= \ -9 \\ 27 \, x_2^{(k+1)} \ \ + \ \ 27 \, x_3^{(k+1)} \ \ - \ \ 110 \, x_4^{(k+1)} \ \ \ \ \ \ \ \ \ &= \ -45 \end{aligned}$$

Man får

$$\begin{array}{ll} x_1 = 0.5779 \quad & x_2 = 0.7964 \\ x_3 = 0.4734 \quad & x_4 = 0.7207 \end{array}$$

*Kjeldevarsel: i utleiinga av $(x_2,y_1)$-likninga står det trykt $u_{112}$ (meinast $u_{11}$, same ledd som i sluttlikninga); tala 0.5779 og 0.7207 er avkutta — med vanleg 4-siffers avrunding får ein 0.5780 og 0.7208 (sympy: 0.57798…, 0.79641…, 0.47344…, 0.72078…). Elles ordrett.*

Kildesett: course=TMA4125 term=var year=2008 problem=4 file=eksamen-bok_2008v.pdf
