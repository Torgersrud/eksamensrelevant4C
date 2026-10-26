### **Løsning til Oppgåve 1**

Den retningseriverte er størst i retningen til gradienten. Vi regner ut gradienten til $f$,

$$\nabla f(x, y, z) = \frac{1}{2} \cos \frac{x}{2} \mathbf{i} + 2z e^{2yz} \mathbf{j} + 2y e^{2yz} \mathbf{k}.$$

Spesielt er $\nabla f(\pi, 0, 1) = 2\mathbf{j}$. Den retningsderiverte er gitt ved $D_{\mathbf{u}}(x, y, z) = \mathbf{u} \cdot \nabla f(x, y, z)$ og er størst når $\mathbf{u}$ er parallell med $\nabla f(x, y, z)$, det vil si $\underline{\mathbf{u} = \mathbf{j}}$, og $D_{\mathbf{u}}(\pi, 0, 1) = |\nabla f(\pi, 0, 1)| = \underline{2}$.

*Kjeldevarsel: løsningsforslaget trykkjer ledda $2z e^{yz}\mathbf{j} + 2y e^{yz}\mathbf{k}$ med eksponent $yz$, medan oppgåva gjev $e^{2yz}$; koeffisientane $2z$ og $2y$ svarer til den deriverte av $e^{2yz}$, og verdien $\nabla f(\pi, 0, 1) = 2\mathbf{j}$ er korrekt i begge tolkingar.*

Kildesett: course=TMA4105 term=var year=2007 problem=1 file=tma4105_07v.pdf
