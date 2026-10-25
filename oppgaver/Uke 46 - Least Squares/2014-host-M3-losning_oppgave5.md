### **Løsning til Oppgave 5**

a) The system is $A\vec{x} = \vec{b}$ with

$$A = \begin{pmatrix} 1 & 1\\ 2 & 1\\ 3 & 1 \end{pmatrix},\quad \vec{x} = \begin{pmatrix} x_1\\ x_2 \end{pmatrix},\quad \vec{b} = \begin{pmatrix} 2\\ 3\\ 5 \end{pmatrix}.$$

b) Write the augmented matrix:

$$\left(\begin{array}{cc|c} 1 & 1 & 2\\ 2 & 1 & 3\\ 3 & 1 & 5 \end{array}\right) \sim \left(\begin{array}{cc|c} 1 & 1 & 2\\ 0 & -1 & -1\\ 0 & -2 & -1 \end{array}\right) \sim \left(\begin{array}{cc|c} 1 & 1 & 2\\ 0 & -1 & -1\\ 0 & 0 & 1 \end{array}\right)$$

There is a row "$0 = 1$" so the system has no solution.

c) The least-square solution of $A\vec{x} = \vec{b}$ is the solution of

$$A^TA\vec{x} = A^T\vec{b}$$

$$A^TA = \begin{pmatrix} 1 & 2 & 3\\ 1 & 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1\\ 2 & 1\\ 3 & 1 \end{pmatrix} = \begin{pmatrix} 14 & 6\\ 6 & 3 \end{pmatrix}$$

$$A^T\vec{b} = \begin{pmatrix} 1 & 2 & 3\\ 1 & 1 & 1 \end{pmatrix}\begin{pmatrix} 2\\ 3\\ 5 \end{pmatrix} = \begin{pmatrix} 23\\ 10 \end{pmatrix}$$

so we solve:

$$\begin{pmatrix} 14 & 6\\ 6 & 3 \end{pmatrix}^{-1} = \frac{1}{42 - 36}\begin{pmatrix} 3 & -6\\ -6 & 14 \end{pmatrix} = \frac{1}{6}\begin{pmatrix} 3 & -6\\ -6 & 14 \end{pmatrix}$$

$$\text{so } \vec{x} = (A^TA)^{-1}(A^T\vec{b}) = \frac{1}{6}\begin{pmatrix} 3 & -6\\ -6 & 14 \end{pmatrix}\begin{pmatrix} 23\\ 10 \end{pmatrix} = \frac{1}{6}\begin{pmatrix} 69 - 60\\ 140 - 138 \end{pmatrix} = \frac{1}{6}\begin{pmatrix} 9\\ 2 \end{pmatrix} = \begin{pmatrix} 3/2\\ 1/3 \end{pmatrix}$$

$$\text{so } \vec{x} = \begin{pmatrix} 3/2\\ 1/3 \end{pmatrix} \text{ is the least square solution.}$$

*Kjeldevarsel: lausningsarket for 2014h er handskrive på engelsk («Math 3 Fall 2014 — Solution to the exam», `lfdec2014.pdf`, skanna PDF utan tekstlag), og lausninga er difor ordrett engelsk; fila nyttar repo-hovudet «Løsning til Oppgave N» (2015-host-4N-praksis). Arket dekkjer berre a)–c); del d) (skisse av punkta og linja) og e) (svaret $4x_1 + x_2 = 19/3$) har inga publisert løysing. I sluttlina står det ein overstreka feilvektor $\binom{9/8}{1/4}$ attmed den rette $\binom{3/2}{1/3}$ — overstrikinga er utelaten i transkripsjonen, og talet 6 i $\frac{1}{6}$ er streka over og skriven på nytt (framgangsmåten uendra).*

Kildesett: course=TMA4110 term=host year=2014 problem=5 file=exam-bokmal-corrige.pdf
