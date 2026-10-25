### **Løsning til Oppgave 7**

**a)** Vi setter opp ligningssystemet for $p(x_1)=ax_1^2+bx_1+c=y_1$ for punktene $(x_1,y_1)$ og løser

$$\left[\begin{array}{ccc|c}1&1&1&4\\ 4&2&1&1\\ 1&-1&1&0\end{array}\right]\sim\left[\begin{array}{ccc|c}1&0&0&-\frac{5}{3}\\ 0&1&0&2\\ 0&0&1&\frac{11}{3}\end{array}\right],$$

dvs $p(x)=-\frac{5}{3}x^2+2x+\frac{11}{3}$. Setter inn og ser at $p(1)=4$, $p(2)=1$ og $p(-1)=0$.

**b)** Setter opp og løser minste kvadraters metode med $A=\begin{bmatrix}1&1\\ 2&1\\ -1&1\end{bmatrix}$, $A^{T}A=\begin{bmatrix}6&2\\ 2&3\end{bmatrix}$, $b=\begin{bmatrix}4\\ 1\\ 0\end{bmatrix}$

og $A^{T}b=\begin{bmatrix}6\\ 5\end{bmatrix}$.

Dvs. vi løser $A^{T}Ax=A^{T}B$ og finner $x=\begin{bmatrix}a\\ b\end{bmatrix}=\begin{bmatrix}\frac{4}{7}\\ \frac{9}{7}\end{bmatrix}$. Den beste første-ordens tilnærmingen til datapunktene vil altså være $p(x)=\frac{4}{7}x+\frac{9}{7}$.

Kildesett: course=TMA4110 term=host year=2024 problem=7 file=tma4110_24h_bokmaal.pdf
