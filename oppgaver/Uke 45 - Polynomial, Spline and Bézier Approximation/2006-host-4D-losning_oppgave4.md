### **Løsning til Oppgave 4**

**a)** Newtons dividerte differans Interpolasjon formel

$$\begin{array}{c|c|cccc}x_j&f_j&f[x_j,x_{j+1}]&f[x_j,x_{j+1},x_{j+2}]&f[x_j,\ldots,x_{j+3}]&f[x_j,\ldots,x_{j+4}]\\ \hline -2&12\\ &&-12\\ -1&0&&6&&-1\\ &&0&&3&&0\\ 0&0&&-1\\ &&6\\ 1&6&&0\\ &&6\\ 2&12\end{array}\tag{1}$$

Interpolasjonen er

$$p(t)=12-12(x+2)+6(x+2)(x+1)-1(x+2)(x+1)x=-x^3+3x^2+4x\tag{2}$$

**b)** Integrasjon med Simpson

$$\frac{1}{3}(12+4\cdot 0+2\cdot 0+4\cdot 6+12)=16\tag{3}$$

Analytisk integrasjon. 1. og 3. ledd er odde:

$$\int_{-2}^{2}-x^3+3x^2+4x\,dx=[x^3]_{-2}^{2}=16\tag{4}$$

Simpson's formel for integrasjon ga eksakt resultat.

Feilen til Simpson er gitt ved

$$\frac{h}{12}p^{(4)}(\xi)\tag{5}$$

der $\xi$ er et element i integrasjonsintervallet. Derivasjon av $p(t)$ gir $p^{(4)}(t)\equiv 0$. Derfor var det forventet at Simpson skulle gi nøyaktig svar.

Kildesett: course=TMA4135 term=host year=2006 problem=4 file=tma4135_06h.pdf
