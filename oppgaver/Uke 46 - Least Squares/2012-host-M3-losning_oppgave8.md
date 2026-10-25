### **Løsning til Oppgave 8**

Solution. We will solve the problem by solving the normal equations, but to find the normal equations, we need to express the problem in terms of a matrix equation. First, we form the design matrix

$$X = \begin{bmatrix} 1 & 1\\ 1 & 2\\ 1 & 4\\ 1 & 5 \end{bmatrix}$$

and the observation vector

$$\vec{y} = \begin{bmatrix} 3\\ 5\\ 7\\ 9 \end{bmatrix}$$

Now, we can express the problem as: Find the least-squares solution of $X\beta = \vec{y}$. The normal equations are $X^{T}X\beta = X^{T}\vec{y}$. We compute

$$X^{T}X = \begin{bmatrix} 4 & 12\\ 12 & 46 \end{bmatrix}$$

and

$$X^{T}\vec{y} = \begin{bmatrix} 24\\ 86 \end{bmatrix}$$

so the system we need to solve is

$$\begin{bmatrix} 4 & 12\\ 12 & 46 \end{bmatrix} \begin{bmatrix} \beta_0\\ \beta_1 \end{bmatrix} = \begin{bmatrix} 24\\ 86 \end{bmatrix}$$

The solution is

$$\beta_0 = \frac{18}{10} \quad \text{and} \quad \beta_1 = \frac{14}{10}$$

so the best-fitting line is $y = \frac{18}{10} + \frac{14}{10}x$.

*Kjeldevarsel: lausningsarket for 2012h er typesett på engelsk («Exam in TMA4110 Calculus 3, December 2012», `lf2.pdf`), og lausninga er difor ordrett engelsk; fila nyttar repo-hovudet «Løsning til Oppgave N» (2015-host-4N-praksis). Svaret er skriven uforkorta som $\beta_0 = \frac{18}{10}$ og $\beta_1 = \frac{14}{10}$ (førte ordrett; det forkorta svaret er $\frac{9}{5}$ og $\frac{7}{5}$). Designmatrisa, $X^{T}X = \begin{bmatrix} 4 & 12\\ 12 & 46 \end{bmatrix}$, $X^{T}\vec{y} = (24,86)$, løysinga og linja er kontrollreikna med sympy; residualen står ortogonalt på begge kolonnene i $X$.*

Kildesett: course=TMA4110 term=host year=2012 problem=8 file=norsk.pdf
