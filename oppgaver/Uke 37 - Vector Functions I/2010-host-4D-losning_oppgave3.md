### **Løsning til Oppgave 3**

Den retningsderiverte til $f(x,y)$ i punktet $(1,1)$ langs vektoren $\mathbf{a}$ kan uttrykkes som

$$D_{\mathbf{a}}f(1,1)=\frac{\mathbf{a}}{\|\mathbf{a}\|}\bullet\nabla f(1,1).$$

Med andre ord, vil $D_{\mathbf{e}}f(1,1)=0$ for de enhetsvektorene $\mathbf{e}$ som står ortogonalt på $\nabla f(1,1)$. Gradienten til $f(x,y)=\ln(x^2+e^{2xy})$ er gitt ved

$$\nabla f=\frac{\partial f}{\partial x}\mathbf{i}+\frac{\partial f}{\partial y}\mathbf{j}=\frac{2}{x^2+e^{2xy}}\big((x+ye^{2xy})\mathbf{i}+xe^{2xy}\mathbf{j}\big),$$

slik at

$$\nabla f(1,1)=\frac{2}{1+e^2}\big((1+e^2)\mathbf{i}+e^2\mathbf{j}\big).$$

Altså er

$$\mathbf{e}=\frac{\pm 1}{\sqrt{1+2e^2+2e^4}}\big(-e^2\mathbf{i}+(1+e^2)\mathbf{j}\big).$$

Kildesett: course=TMA4135 term=host year=2010 problem=3 file=tma4135_10h.pdf
