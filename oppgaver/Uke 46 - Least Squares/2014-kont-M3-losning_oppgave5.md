### **Løsning til Oppgave 5**

Solution: We first need an orthogonal basis of $V$ to compute the orthogonal projection.

Run Gram-Schmidt algorithm on the generating set of $V$:

$$\vec{v}_1 = \begin{bmatrix} 1\\ 2\\ 2\\ 1 \end{bmatrix},\qquad \vec{v}_2 = \begin{bmatrix} 2\\ 3\\ 1\\ 2 \end{bmatrix} - \frac{\vec{v}_1\cdot\begin{bmatrix} 2\\ 3\\ 1\\ 2 \end{bmatrix}}{\vec{v}_1\cdot\vec{v}_1}\,\vec{v}_1 = \begin{bmatrix} 2\\ 3\\ 1\\ 2 \end{bmatrix} - \frac{12}{10}\begin{bmatrix} 1\\ 2\\ 2\\ 1 \end{bmatrix} = \frac{1}{5}\begin{bmatrix} 4\\ 3\\ -7\\ 4 \end{bmatrix}$$

$$\vec{v}_3 = \begin{bmatrix} 0\\ 1\\ 3\\ 0 \end{bmatrix} - \frac{\vec{v}_1\cdot\begin{bmatrix} 0\\ 1\\ 3\\ 0 \end{bmatrix}}{10}\,\vec{v}_1 - \frac{\vec{v}_2\cdot\begin{bmatrix} 0\\ 1\\ 3\\ 0 \end{bmatrix}}{\vec{v}_2\cdot\vec{v}_2}\,\vec{v}_2 = \begin{bmatrix} 0\\ 0\\ 0\\ 0 \end{bmatrix} \quad \text{(so } \begin{bmatrix} 0\\ 1\\ 3\\ 0 \end{bmatrix} \text{ does not contribute anything and we drop it from the computation)}$$

$$\vec{v}_3 = \begin{bmatrix} 1\\ 1\\ -1\\ 1 \end{bmatrix} - \frac{\vec{v}_1\cdot\begin{bmatrix} 1\\ 1\\ -1\\ 1 \end{bmatrix}}{10}\,\vec{v}_1 - \frac{\vec{v}_2\cdot\begin{bmatrix} 1\\ 1\\ -1\\ 1 \end{bmatrix}}{\vec{v}_2\cdot\vec{v}_2}\,\vec{v}_2 = \begin{bmatrix} 0\\ 0\\ 0\\ 0 \end{bmatrix}$$

again we get nothing new, so an orthogonal basis for $V$ is given by $\{\vec{v}_1, \vec{v}_2\}$.

From the lecture we know that the orthogonal projection of $\vec{y} = \begin{bmatrix} 4\\ -2\\ 0\\ 2 \end{bmatrix}$ is given by the formula

$$\frac{\vec{y}\cdot\vec{v}_1}{\vec{v}_1\cdot\vec{v}_1}\,\vec{v}_1 + \frac{\vec{y}\cdot\vec{v}_2}{\vec{v}_2\cdot\vec{v}_2}\,\vec{v}_2$$

$$= \frac{2}{10}\begin{bmatrix} 1\\ 2\\ 2\\ 1 \end{bmatrix} + \frac{\frac{1}{5}\cdot 18}{\frac{18}{5}}\cdot\frac{1}{5}\begin{bmatrix} 4\\ 3\\ -7\\ 4 \end{bmatrix}$$

$$= \frac{1}{5}\begin{bmatrix} 1\\ 2\\ 2\\ 1 \end{bmatrix} + \frac{1}{5}\begin{bmatrix} 4\\ 3\\ -7\\ 4 \end{bmatrix} = \begin{bmatrix} 1\\ 1\\ -1\\ 1 \end{bmatrix}$$

*Kjeldevarsel: lausningsarket for 2014-kont er handskrive på engelsk («Problem 5», `lfkont2014.pdf`, skanna PDF utan tekstlag), og lausninga er difor ordrett engelsk; fila nyttar repo-hovudet «Løsning til Oppgave N» (2015-host-4N-praksis). Arket merker både den tredje og den fjerde generatoren si Gram-Schmidt-rekning med $\vec{v}_3$ (behalde som det står; begge rekningslinjene går til $\vec 0$, slik at merkinga ikkje påverkar noko). Mellombrøken i projeksjonsformelen er skriven samanstreka på arket med ein nemnar som berre lesast som ein understreka `18'; verdien $\frac{18}{5} = \vec{v}_2\cdot\vec{v}_2$ er påkravd av neste linje (brøken blir 1). Gram-Schmidt, projeksjonen $\begin{bmatrix} 1\\ 1\\ -1\\ 1 \end{bmatrix}$ og at restvektoren $\begin{bmatrix} 3\\ -3\\ 1\\ 1 \end{bmatrix}$ står ortogonalt på alle fire generatorane, er kontrollrekna med sympy; same svar kjem ut av normallikningane på søylene $(1,2,2,1)$ og $(2,3,1,2)$.*

Kildesett: course=TMA4110 term=kont year=2014 problem=5 file=kont2014nor.pdf
