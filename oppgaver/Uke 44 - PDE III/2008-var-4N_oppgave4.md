### **Oppgave 4**

**a)** Vi vil løse ligningen

$$u_{xx}(x,y) + u_{yy}(x,y) = x \, u(x,y)$$

på firkanten $[0,1] \times [0,1]$ med randbetingelser

$$u(x,0) = x, \ u(x,1) = x \ \text{for} \ 0 \leq x \leq 1,$$
$$u(0,y) = 0, \ \text{for} \ 0 \leq y \leq 1,$$
$$u(1,y) = 1, \ \text{for} \ 0 \leq y \leq 1.$$

La $h = \frac{1}{3}$ være skrittlengden for det gitteret som er gitt av punktene $(x_i, y_j) = (ih, jh)$ for $i, j = 0, \ldots, 3$. Sett opp et system av ligninger for $u_{1,1}$, $u_{2,1}$, $u_{1,2}$ og $u_{2,2}$, der $u_{i,j}$ er en tilnærming av $u(x_i, y_j)$.

**b)** Utfør ett steg med Gauss-Seidel iterasjon på systemet

$$\begin{pmatrix} -109 & 27 & 27 & 0 \\ 27 & -110 & 0 & 27 \\ 27 & 0 & -109 & 27 \\ 0 & 27 & 27 & -110 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} = \begin{pmatrix} -9 \\ -45 \\ -9 \\ -45 \end{pmatrix}$$

ved å begynne i punktet $(1, 1, 1, 1)^T$. Bruk 4 siffers nøyaktighet.

Kildesett: course=TMA4125 term=var year=2008 problem=4 file=eksamen-bok_2008v.pdf
