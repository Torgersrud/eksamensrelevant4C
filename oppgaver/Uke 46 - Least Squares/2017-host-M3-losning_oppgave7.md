### **Løsning til Oppgave 7**

*Solution for 7a).* A linear transformation is a function $T:V\to W$ between two vector spaces such that every $a,b\in\mathbb{R}$ and $\mathbf{v}_1,\mathbf{v}_2\in V$ satisfies

$$T(a\mathbf{v}_1+b\mathbf{v}_2)=aT\mathbf{v}_1+bT\mathbf{v}_2.$$

*Solution for 7b).* Every $a,b\in\mathbb{R}$ and $\mathbf{v}_1,\mathbf{v}_2\in\mathbb{R}^3$ satisfies

$$\mathrm{proj}_{\mathbf{u}}(a\mathbf{v}_1+b\mathbf{v}_2)=\frac{(a\mathbf{v}_1+b\mathbf{v}_2)\cdot\mathbf{u}}{\mathbf{u}\cdot\mathbf{u}}\mathbf{u}=a\frac{\mathbf{v}_1\cdot\mathbf{u}}{\mathbf{u}\cdot\mathbf{u}}\mathbf{u}+b\frac{\mathbf{v}_2\cdot\mathbf{u}}{\mathbf{u}\cdot\mathbf{u}}\mathbf{u}=a\mathrm{proj}_{\mathbf{u}}\mathbf{v}_1+b\mathrm{proj}_{\mathbf{u}}\mathbf{v}_2.$$

*Solution for 7c).* We know that

$$A=[T\mathbf{e}_1,T\mathbf{e}_2,T\mathbf{e}_3]$$

where

$$\mathbf{e}_1=\begin{pmatrix}1\\ 0\\ 0\end{pmatrix},\ \mathbf{e}_2=\begin{pmatrix}0\\ 1\\ 0\end{pmatrix},\ \mathbf{e}_3=\begin{pmatrix}0\\ 0\\ 1\end{pmatrix}$$

is the standard basis. We thus compute $\mathrm{proj}_{\mathbf{u}}\mathbf{e}_1,\mathrm{proj}_{\mathbf{u}}\mathbf{e}_2,\mathrm{proj}_{\mathbf{u}}\mathbf{e}_3$:

$$\frac{\mathbf{e}_1\cdot\mathbf{u}}{\mathbf{u}\cdot\mathbf{u}}\mathbf{u},\qquad\frac{\mathbf{e}_2\cdot\mathbf{u}}{\mathbf{u}\cdot\mathbf{u}}\mathbf{u},\qquad\frac{\mathbf{e}_3\cdot\mathbf{u}}{\mathbf{u}\cdot\mathbf{u}}\mathbf{u},$$

which give the vectors

$$\frac{1}{30}\begin{pmatrix}4\\ -10\\ 2\end{pmatrix},\qquad\frac{1}{30}\begin{pmatrix}-10\\ 25\\ -5\end{pmatrix},\qquad\frac{1}{30}\begin{pmatrix}2\\ -5\\ 1\end{pmatrix}.$$

Therefore

$$A=\frac{1}{30}\begin{bmatrix}4&-10&2\\ -10&25&-5\\ 2&-5&1\end{bmatrix}.$$

*Kjeldevarsel: det publiserte løysingsarkivet for 2017h finst berre på engelsk (`tma4110-2017h-lf.pdf`, «Problem 7», side 11–12), og løysinga er difor skriven ordrett på engelsk. Provensfoten peikar på eksamensarket, jf. OPEN-1. Projeksjonsmatrisa er kontrollrekna med sympy: $A=\mathbf{u}\mathbf{u}^T/\|\mathbf{u}\|^2$.*

Kildesett: course=TMA4110 term=host year=2017 problem=7 file=tma4110-2017h-nb.pdf
