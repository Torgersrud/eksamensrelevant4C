### **Løsning til Oppgave 5**

a) Vi vil løse ligningen

$$u_{xx}(x, y) + u_{yy}(x, y) = 27(x + y),$$

på firkanten $[0, 1] \times [0, 1]$ med randbetingelser

$$u(0, y) = u(x, 0) = 0, \quad u(x, 1) = 3x, \quad u(1, y) = 3y.$$

Approksimasjon av ligningen i noden $(x_i, y_j)$ ved hjelp av sentraldifferanser, gir

$$U_{i+1}^j + U_i^{j+1} + U_{i-1}^j + U_i^{j-1} - 4U_i^j = h^2 f(x_i, y_j),$$

hvor $U_i^j \approx u(x_i, y_j)$, $f(x, y) = 27(x + y)$ og $x_i = ih, y_j = jh, h = 1/3$.

Approksimasjon av ligningen i $(x_i, y_j)$, hvor $i, j \in \{1, 2\}$, gir ligningene

$$
\begin{aligned}
-4U_1^1 + U_1^2 + U_2^1 + 0 + 0 &= \left(\frac{1}{3}\right)^2 27\left(\frac{1}{3} + \frac{1}{3}\right) & \text{i} \quad (x_1, y_1), \\
-4U_2^1 + U_1^1 + U_2^2 + 0 + 3 \cdot \frac{1}{3} &= \left(\frac{1}{3}\right)^2 27\left(\frac{2}{3} + \frac{1}{3}\right) & \text{i} \quad (x_2, y_1), \\
-4U_1^2 + U_1^1 + U_2^2 + 3 \cdot \frac{1}{3} + 0 &= \left(\frac{1}{3}\right)^2 27\left(\frac{1}{3} + \frac{2}{3}\right) & \text{i} \quad (x_1, y_2), \\
-4U_2^2 + U_1^2 + U_2^1 + 3 \cdot \frac{2}{3} + 3 \cdot \frac{2}{3} &= \left(\frac{1}{3}\right)^2 27\left(\frac{2}{3} + \frac{2}{3}\right) & \text{i} \quad (x_2, y_2).
\end{aligned}
$$

Dette kan skrives på matriseform

$$(1) \qquad \begin{bmatrix} -4 & 1 & 1 & 0 \\ 1 & -4 & 0 & 1 \\ 1 & 0 & -4 & 1 \\ 0 & 1 & 1 & -4 \end{bmatrix} \begin{bmatrix} U_1^1 \\ U_2^1 \\ U_1^2 \\ U_2^2 \end{bmatrix} = \begin{bmatrix} 2 \\ 2 \\ 2 \\ 0 \end{bmatrix}.$$

b) En iterasjon med Gauss-Seidel

$$x_j^{(1)} = \frac{1}{a_{jj}} \left( b_j - \sum_{k=1}^{j-1} a_{jk} x_k^{(1)} - \sum_{k=j+1}^{4} a_{jk} x_k^{(0)} \right), \quad j = 1, \ldots, 4,$$

anvendt på ligningssystemet (1) i a) med startvektoren $\boldsymbol{U}^{(0)} = -[1, 1, 1, 1]^T$, gir

$$
\begin{aligned}
(U_1^1)^{(1)} &= \frac{1}{-4}(2 - 1 \cdot (-1) - 1 \cdot (-1)) &= -1, \\
(U_2^1)^{(1)} &= \frac{1}{-4}(2 - 1 \cdot (-1) - 1 \cdot (-1)) &= -1, \\
(U_1^2)^{(1)} &= \frac{1}{-4}(2 - 1 \cdot (-1) - 1 \cdot (-1)) &= -1, \\
(U_2^2)^{(1)} &= \frac{1}{-4}(0 - 1 \cdot (-1) - 1 \cdot (-1)) &= -0.5.
\end{aligned}
$$

En iterasjon med Gauss-Seidel på systemet

$$\begin{bmatrix} -5 & 1 & 1 & 1 \\ 1 & -5 & 1 & 1 \\ 1 & 1 & -5 & 1 \\ 1 & 1 & 1 & -5 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} 2.5 \\ 2 \\ 2 \\ -0.5 \end{bmatrix}$$

med startvektoren $\boldsymbol{x}^{(0)} = -[1, 1, 1, 1]^T$, gir

$$
\begin{aligned}
x_1^{(1)} &= \frac{1}{-5}(2.5 - 1 \cdot (-1) - 1 \cdot (-1) - 1 \cdot (-1)) &= -1.1, \\
x_2^{(1)} &= \frac{1}{-5}(2 - 1 \cdot (-1.1) - 1 \cdot (-1) - 1 \cdot (-1)) &= -1.02, \\
x_3^{(1)} &= \frac{1}{-5}(2 - 1 \cdot (-1.1) - 1 \cdot (-1.02) - 1 \cdot (-1)) &= -1.024, \\
x_4^{(1)} &= \frac{1}{-5}(-0.5 - 1 \cdot (-1.1) - 1 \cdot (-1.02) - 1 \cdot (-1.024)) &= -0.5288.
\end{aligned}
$$

De eksakte løsningsene av ligningssystemene er like.

$$\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} U_1^1 \\ U_2^1 \\ U_1^2 \\ U_2^2 \end{bmatrix} = -\frac{1}{12} \begin{bmatrix} 11 \\ 10 \\ 10 \\ 5 \end{bmatrix}.$$

Kildesett: course=TMA4135 term=host year=2008 problem=5 file=tma4135_08h.pdf
