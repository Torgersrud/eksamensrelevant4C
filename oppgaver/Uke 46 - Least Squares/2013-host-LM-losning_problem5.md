### **Solution to Problem 5**

**a)** Gram–Schmidt: Let

$$e_1=\frac{(1,0,1,1)}{\lVert(1,0,1,1)\rVert}=\frac{1}{\sqrt{3}}(1,0,1,1).$$

Then let

$$\tilde{v}_2=(1,2,3,2)-\left\langle(1,2,3,2),\tfrac{1}{\sqrt{3}}(1,0,1,1)\right\rangle\tfrac{1}{\sqrt{3}}(1,0,1,1)$$

$$=(1,2,3,2)-(2,0,2,2)$$

$$=(-1,2,1,0),$$

and

$$e_2=\frac{(-1,2,1,0)}{\lVert(-1,2,1,0)\rVert}=\frac{1}{\sqrt{6}}(-1,2,1,0).$$

Then $\{e_1,e_2\}$ form an orthonormal set, spanning the same linear space as $\{(1,2,3,2),(1,0,1,1)\}$. Note that this set is closed, convex and non-empty, so that the existence of a minimising point $x_0$, as asked for the in the problem, is guaranteed by the minimal distance theorem.

To find it, project $y$ onto $\text{span}\{e_1,e_2\}$:

$$x_0=\langle y,e_1\rangle e_1-\langle y,e_2\rangle e_2$$

$$=\left\langle(2,0,3,1),\tfrac{1}{\sqrt{3}}(1,0,1,1)\right\rangle\tfrac{1}{\sqrt{3}}(1,0,1,1)$$

$$\quad+\left\langle(2,0,3,1),\tfrac{1}{\sqrt{6}}(-1,2,1,0)\right\rangle\tfrac{1}{\sqrt{6}}(-1,2,1,0)$$

$$=(2,0,2,2)+\tfrac{1}{6}(-1,2,1,0)$$

$$=\tfrac{1}{6}(11,2,13,12).$$

The distance $d$ is then given by

$$d^{2}=\lVert y\rVert^{2}-|\langle y,e_1\rangle|^{2}-|\langle y,e_2\rangle|^{2}=14-12-\frac{1}{6}=\frac{11}{6},$$

meaning $d=\sqrt{\frac{11}{6}}$.

*Kjeldevarsel: første linja i $x_0$-utrekninga er trykt med minusteikn — $\langle y,e_1\rangle e_1-\langle y,e_2\rangle e_2$ — medan leddet på neste linje har pluss, og sluttresultatet $\frac{1}{6}(11,2,13,12)$ krev pluss (kontrollrekna: $\langle y,e_1\rangle e_1=(2,0,2,2)$, $\langle y,e_2\rangle e_2=\frac{1}{6}(-1,2,1,0)$). Teksten «as asked for the in the problem» står trykt som det gjer.*

*(Oppgåvens punkt b) og c) er utelpte — sjå Kjeldevarselet i oppgåveteksten. Løysingsforslaget reknar likevel begge ut; dei er utelatte her.)*

Kildesett: course=TMA4145 term=host year=2013 problem=5 file=tma4145eksh13en.pdf
