### **Løsning til Oppgave 5**

Fra ligningssystemet ser vi at

$$y=e^x\quad\text{og}\quad x=\frac{1}{6}y^2-\frac{2}{3}.$$

[Figur: Skissert koordinatsystem med $x$-akse fra $-1$ til $4$ og $y$-akse fra $-2$ til $5$. Eksponentialkurven $y=e^x$ og parabelen $x=\frac{1}{6}y^2-\frac{2}{3}$ er tegnet; de skjærer hverandre i to punkter, ett nær $(0,2)$-regionen ved $x\approx-0{,}6$ (liten $y$) og ett nær $(1{,}2,\ 3{,}4)$. Figurtekst: "Figur 1: Skissé av ligningssystemet".]

Fra figur 1 er det klart at ligningssystemet har to løsninger.

Jacobi-matrisen til ligningssystemet er gitt ved

$$J(x,y)=\left[\begin{array}{cc}\displaystyle\frac{\partial}{\partial x}(e^x-y)&\displaystyle\frac{\partial}{\partial y}(e^x-y)\\[3mm]\displaystyle\frac{\partial}{\partial x}(y^2-6x-4)&\displaystyle\frac{\partial}{\partial y}(y^2-6x-4)\end{array}\right]=\left[\begin{array}{cc}e^x&-1\\ -6&2y\end{array}\right],$$

slik at

$$J^{(0)}=J\left(x^{(0)},y^{(0)}\right)=J(1,3)=\left[\begin{array}{cc}e&-1\\ -6&6\end{array}\right].$$

Vi har ved Newtons metode for system av ikke-lineære ligninger at

$$\mathbf{x}^{(1)}=\mathbf{x}^{(0)}+\Delta\mathbf{x}^{(0)},$$

der $J^{(0)}\Delta\mathbf{x}^{(0)}=-\mathbf{f}\big(\mathbf{x}^{(0)}\big)$.

I vårt tilfelle er

$$\mathbf{f}(\mathbf{x})=\left[\begin{array}{c}e^x-y\\ y^2-6x-4\end{array}\right],\quad\text{der}\quad\mathbf{x}=\left[\begin{array}{c}x\\ y\end{array}\right].$$

Dette gir følgende ligningssystem med hensyn på $\Delta\mathbf{x}^{(0)}$

$$\left[\begin{array}{cc}e&-1\\ -6&6\end{array}\right]\left[\begin{array}{c}\Delta x^{(0)}\\ \Delta y^{(0)}\end{array}\right]=-\left[\begin{array}{c}e-3\\ 9-6-4\end{array}\right]=\left[\begin{array}{c}3-e\\ 1\end{array}\right],$$

som har løsning

$$\Delta\mathbf{x}^{(0)}=\left[\begin{array}{c}\displaystyle\frac{19-6e}{6(e-1)}\\[3mm]\displaystyle\frac{1}{6}+\frac{19-6e}{6(e-1)}\end{array}\right]\approx\left[\begin{array}{c}0,2610\\ 0,4276\end{array}\right].$$

Altså er

$$\mathbf{x}^{(1)}=\mathbf{x}^{(0)}+\Delta\mathbf{x}^{(0)}\approx\left[\begin{array}{c}1,2610\\ 3,4276\end{array}\right].$$

Kildesett: course=TMA4135 term=kont year=2011 problem=5 file=tma4135_11k.pdf
