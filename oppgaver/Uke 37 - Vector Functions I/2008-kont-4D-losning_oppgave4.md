### **Løsning til Oppgave 4**

Enhetsvektoren i retningen $\mathbf{v}$ er $\mathbf{e} = \frac{1}{3}(2\mathbf{i} + 2\mathbf{j} + \mathbf{k})$. Evaluerer vi funksjonen i punktet $P$ får vi $f|_P = e^{-5}$. De partiellderiverte er,

$$
\begin{aligned}
\frac{\partial}{\partial x} f &= (y + z)f, \\
\frac{\partial}{\partial y} f &= (z + x)f, \\
\frac{\partial}{\partial z} f &= (x + y)f.
\end{aligned}
$$

Evaluerer vi i $P$ finner vi at gradienten til $f$ i $P$ er $\text{grad} f|_P = 2e^{-5}(\mathbf{i} + \mathbf{j} - \mathbf{k})$. Den retningsderiverte er altså

$$D_{\mathbf{e}} f|_P = \mathbf{e} \cdot \text{grad} f|_P = 2e^{-5}.$$

Kildesett: course=TMA4135 term=kont year=2008 problem=4 file=tma4135_08k.pdf
