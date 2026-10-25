### **Løsning til Oppgave 7**

Solution:

We write this in matrix form as follows:

$$\begin{bmatrix} 0 & 1\\ 1 & 1\\ 2 & 1\\ 3 & 1\\ 4 & 1\\ 5 & 1 \end{bmatrix} \begin{bmatrix} m\\ c \end{bmatrix} = \begin{bmatrix} 3\\ 3\\ 6\\ -3\\ 1\\ -1 \end{bmatrix}$$

This does not have a solution so we look for a least-squares solution.

Setting $A$ to be the matrix in the above and $\vec{b}$ the vector on the right-hand side, we examine the linear system $A^{\top}A\vec{x} = A^{\top}\vec{b}$. This is:

$$\begin{bmatrix} 55 & 15\\ 15 & 6 \end{bmatrix} \begin{bmatrix} m\\ c \end{bmatrix} = \begin{bmatrix} 5\\ 9 \end{bmatrix}$$

To solve this, we row reduce the augmented matrix. One possible row reduction is as follows.

$$\begin{bmatrix} 55 & 15 & 5\\ 15 & 6 & 9 \end{bmatrix} \xrightarrow[\frac{1}{3}\rho_2]{\frac{1}{5}\rho_1} \begin{bmatrix} 11 & 3 & 1\\ 5 & 2 & 3 \end{bmatrix} \xrightarrow{\rho_1 - 2\rho_2} \begin{bmatrix} 1 & -1 & -5\\ 5 & 2 & 3 \end{bmatrix} \xrightarrow{\rho_2 - 5\rho_1} \begin{bmatrix} 1 & -1 & -5\\ 0 & 7 & 28 \end{bmatrix} \xrightarrow{\frac{1}{7}\rho_2} \begin{bmatrix} 1 & -1 & -5\\ 0 & 1 & 4 \end{bmatrix} \xrightarrow{\rho_1 + \rho_2} \begin{bmatrix} 1 & 0 & -1\\ 0 & 1 & 4 \end{bmatrix}$$

Thus the solution is $m = -1$, $c = 4$ and so the least-squares line is $y = -x + 4$.

*Kjeldevarsel: lausningsarket for 2013h er typesett på engelsk («TMA4110 Matematikk 3, 3. desember 2013 — Problem 7 … Solution», `tma4110h13lf.pdf`), og lausninga er difor ordrett engelsk; fila nyttar repo-hovudet «Løsning til Oppgave N» (2015-host-4N-praksis). Tekstlaget i PDF-en gir rot-glyfer for operasjonsetikettane i rekkereduksjonen, så etikettane ⅕ρ₁, ⅓ρ₂, ρ₁−2ρ₂, ρ₂−5ρ₁, ⅐ρ₂ og ρ₁+ρ₂ er lesne frå rendera bilete. $A^{\top}A$, $A^{\top}\vec{b}$, heile rekkereduksjonen og svaret $m=-1$, $c=4$ (linja $y=-x+4$) er kontrollreikna med sympy; residualen står ortogonalt på begge kolonnene i $A$.*

Kildesett: course=TMA4110 term=host year=2013 problem=7 file=tma4110h13.pdf
