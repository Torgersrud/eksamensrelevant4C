### **Løsning til Oppgave 7**

Vi har

$$\mathbf{x}=\begin{pmatrix}x_1\\ x_2\end{pmatrix},\qquad\mathbf{f}(\mathbf{x})=\begin{pmatrix}x_1+x_2-x_1x_2+2\\ x_1e^{-x_2}-1\end{pmatrix},\qquad J(\mathbf{x})=\begin{pmatrix}1-x_2&1-x_1\\ e^{-x_2}&-x_1e^{-x_2}\end{pmatrix}$$

En iterasjon med Newtons metode, med startverdiar $\mathbf{x}^{(0)}=(0.1,0.2)^T$ blir:

Løs

$$\begin{pmatrix}0.8&0.9\\ 0.8187&-0.0819\end{pmatrix}\Delta\mathbf{x}^{(0)}=-\begin{pmatrix}2.28\\ -0.9181\end{pmatrix}\qquad\Rightarrow\qquad\Delta\mathbf{x}^{(0)}=\begin{pmatrix}0.7972\\ -3.2420\end{pmatrix}$$

og

$$x_1^{(1)}=0.1+0.7972=0.8973,\qquad x_2^{(1)}=0.2-3.2420=3.0420.$$

*Kjeldevarsel: forteiknsfeil i siste linje — $0.2-3.2420=-3.0420$, så $x_2^{(1)}=-3.0420$ (ikkje $+3.0420$); utan avrunding gir rekninga $x_2^{(1)}\approx-3.04196$. Dessutan blir $x_1^{(1)}=0.1+0.7972=0.8972$ med avrunda $\Delta x_1$, mot løysingsforslagets $0.8973$.*

Kildesett: course=TMA4135 term=kont year=2012 problem=7 file=tma4135_12k.pdf
