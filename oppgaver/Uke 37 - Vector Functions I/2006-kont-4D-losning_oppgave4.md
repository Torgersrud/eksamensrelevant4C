### **Løsning til Oppgave 4**

Vi regner først ut gradienten.

$$\text{grad} f = [2yz(e^x + e^y - e^z) + 2xyze^x]\mathbf{i} + [2xz(e^x + e^y - e^z) + 2xyze^y]\mathbf{j} + [2xy(e^x + e^y - e^z) - 2xyze^z]\mathbf{k}.$$

Evalering i punktet $P : (1, -1, -1)$ gir oss

$$\text{grad} f|_P = 4e\mathbf{i} + (-2e + 2e^{-1})\mathbf{j} + (-2e - 2e^{-1})\mathbf{k}.$$

Enhetsvektoren vinkelrett både på $\mathbf{a} = \mathbf{i} + \mathbf{k}$ og $\mathbf{b} = \mathbf{j} - \mathbf{k}$ og som har negativ $\mathbf{k}$-komponent er $\mathbf{e} = \frac{1}{\sqrt{3}}(\mathbf{i} - \mathbf{j} - \mathbf{k})$.

Vi finner at den retningsderiverte er

$$D_{\mathbf{e}} f|_P = \frac{8e}{\sqrt{3}}.$$

Kildesett: course=TMA4135 term=kont year=2006 problem=4 file=tma4135_06k.pdf
