### **Løsning til Oppgave 5**

**a)** [Figur: Gitter over rektangelet med $x$-punkter $x_0=0$, $x_1,\ldots,x_7$, $2$ og $y$-punkter $y_0,\ldots,y_4=1$, det vil si $8\cdot 5$ gitterpunkter med $h=0.25$.] Fig. 1: En approksimasjon til $u_{ij}=u(x_i,y_j)$ er gitt ved at

$$u_{xx}+u_{yy}=0\approx\frac{1}{4h^2}\left[\bar{u}_{ij}-u_{ij}\right]$$

da er

$$u_{ij}=\bar{u}_{ij}=\frac{1}{4}\left[u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}\right]$$

det vil si $u_{ij}$ = middelvei av verdien på nabopunktene. Dette gir $3\times 7$ ligninger for de $21$ ukjente. Kan løses f.eks. med Gauss eliminasjon. Randbetingelsen ved $y=1$ sørger for løsning $\neq 0$.

**b)** Antall $x$-punkter $=\frac{2}{h}-1$, antall $y$-punkter $=\frac{1}{h}-1$,

$$\text{antall ukjente}=\left(\frac{2}{h}-1\right)\cdot\left(\frac{1}{h}-1\right)=\frac{1}{h^2}\cdot(2-h)\cdot(1-h)$$

Sjekk: $h=0.25$ gir $3\cdot 7=21$.

**c)** $u_{xx}=F''G$, $u_{yy}=F\cdot G''$

$$0=u_{xx}+u_{yy}=F''G+F\cdot G''=\frac{F''}{F}+\frac{G''}{G}$$

$$F''/F=-k_n^2\quad\text{via drøfting}$$

$$F=A_n\cos k_nx+B_n\sin k_nx$$

$$k_n\cdot 2=\pi n\ \Rightarrow\ k_n=\pi n/2$$

fordi $F(0)=F(2)=0$

$$G''/G=k_n^2;\quad G_n=\frac{1}{2}\left(e^{k_ny}-e^{-k_ny}\right)$$

$$u_n(x,y)=B_n\cdot\sinh(k_ny)\cdot\sin(k_nx)$$

**d)**

$$u(x,1)=\sin(\pi x)\cdot\cos(2\pi x)=\sum_{n=1}^{\infty}B_n\cdot\sinh(k_n)\cdot\sin(k_nx)$$

= Fourier sinus coeff. til $u(x,1)$.

$$\left(e^{i2\pi x}+e^{-i2\pi x}\right)\frac{1}{2}\cdot\frac{1}{2i}\left(e^{i\pi x}-e^{-i\pi x}\right)=\frac{1}{4i}\cdot\left[e^{i3\pi x}-e^{i\pi x}+e^{-i\pi x}-e^{-i3\pi x}\right]$$

det vil si

$$\cos2\pi x\cdot\sin\pi x=\frac{1}{2}\left[\sin3\pi x-\sin\pi x\right]$$

det vil si kun $2$ coeff. ulik $0$:

$$B_2\cdot\sinh(\pi)=-\frac{1}{2}$$

$$B_6\cdot\sinh(3\pi)=\frac{1}{2}$$

det vil si

$$u(x,y)=-\frac{1}{2}\ \frac{\sinh\pi y}{\sinh\pi}\cdot\sin\pi x\quad+\frac{1}{2}\ \frac{\sinh3\pi y}{\sinh3\pi}\cdot\sin3\pi x$$

Alternativt kan Fourier sinus coeff. regnes ut ved integralformel.

Kildesett: course=TMA4135 term=kont year=2017 problem=5 file=tma4135_17k.pdf
