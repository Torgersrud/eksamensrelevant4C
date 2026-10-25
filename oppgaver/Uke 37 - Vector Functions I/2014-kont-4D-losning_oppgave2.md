### **Løsning til Oppgave 2**

Vi ser på ligningssystemet

$$\mathbf{f}(\mathbf{x})=\begin{pmatrix}f_1(x_1,x_2)\\ f_2(x_1,x_2)\end{pmatrix}=\begin{pmatrix}\cos x_1+e^{-x_2}-2\\ x_1+(x_2+3)^2-4\end{pmatrix}=\mathbf{0},$$

der

$$\mathbf{f}(\mathbf{x}^{(0)})=\mathbf{f}(0,0.5)=\begin{pmatrix}e^{-0.5}-1\\ 33/4\end{pmatrix}\approx\begin{pmatrix}-0.3935\\ 8.2500\end{pmatrix}.$$

Jacobimatrisen til $\mathbf{f}$ er gitt ved

$$J(\mathbf{x})=\begin{pmatrix}\frac{\partial f_1}{\partial x_1}&\frac{\partial f_1}{\partial x_2}\\ \frac{\partial f_2}{\partial x_1}&\frac{\partial f_2}{\partial x_2}\end{pmatrix}=\begin{pmatrix}-\sin x_1&-e^{-x_2}\\ 1&2(x_2+3)\end{pmatrix},$$

som gir

$$J^{(0)}=J(\mathbf{x}^{(0)})=\begin{pmatrix}0&-e^{-0.5}\\ 1&7\end{pmatrix}.$$

Én iterasjon med Newtons metode gir

$$\mathbf{x}^{(1)}=\mathbf{x}^{(0)}+\Delta\mathbf{x}^{(0)},$$

hvor

$$J^{(0)}\Delta\mathbf{x}^{(0)}=\begin{pmatrix}0&-e^{-0.5}\\ 1&7\end{pmatrix}\begin{pmatrix}\Delta x_1^{(0)}\\ \Delta x_2^{(0)}\end{pmatrix}=\begin{pmatrix}1-e^{-0.5}\\ -33/4\end{pmatrix}=-\mathbf{f}(\mathbf{x}^{(0)}),$$

som har løsning

$$\Delta x_1^{(0)}\approx-3.7090\qquad\text{og}\qquad\Delta x_2^{(0)}=1-e^{0.5}\approx-0.6487.$$

Altså er

$$\mathbf{x}^{(1)}=\mathbf{x}^{(0)}+\Delta\mathbf{x}^{(0)}\approx\begin{pmatrix}-3.7090\\ -0.1487\end{pmatrix}.$$

Kildesett: course=TMA4135 term=kont year=2014 problem=2 file=tma4135_14k.pdf
