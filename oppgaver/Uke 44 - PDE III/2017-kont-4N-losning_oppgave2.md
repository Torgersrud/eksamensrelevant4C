### **Løsning til Oppgave 2**

**a)** Med rutenettet $u_{ij}=u(i\cdot h,j\cdot k)$, $h=k=\frac{1}{2}$, er dei tre indre punkta $u_{11}$, $u_{21}$ og $u_{31}$ i raden $y=\frac{1}{2}$.

[Figur: Rutenettsskisse med randverdiane $-1$, $0$, $1$ langs topplinja (over $x=\frac{1}{2}$, $1$, $\frac{3}{2}$), $0$ langs botnkanten og $0$ langs sidesidene, og dei ukjende $u_{11}$, $u_{21}$, $u_{31}$ på indre rutenettspunkt.]

then use

$$h^2\nabla^2u_{ij}\approx\ \text{(stjernelapp med } -4 \text{ i sentrum og } 1 \text{ i dei fire nabopunkta)}\qquad (h^2={\textstyle\frac{1}{4}})$$

boundary at top: $u(x)=\sin{(\pi x)}\cos{(2\pi x)}$

$$u({\textstyle\frac{1}{2}})=\sin\frac{\pi}{2}\cos\pi=-1,\qquad u(1)=0,\qquad u({\textstyle\frac{3}{2}})=\sin\frac{3\pi}{2}\cos 3\pi=1$$

node at $u_{11}$: $-4u_{11}+u_{21}-1=0$

" $u_{21}$: $u_{11}-4u_{21}+u_{31}=0$

" $u_{31}$: $u_{21}-4u_{31}+1=0$

ie

$$\left(\begin{array}{rrr}-4&1&0\\ 1&-4&1\\ 0&1&-4\end{array}\right)\left(\begin{array}{c}u_{11}\\ u_{21}\\ u_{31}\end{array}\right)=\left(\begin{array}{c}1\\ 0\\ -1\end{array}\right)$$

**b)** $u_{xx}+u_{yy}=0$

$u=F(x)\,G(y)\ \Rightarrow\ u_{xx}=F''G$, $u_{yy}=FG''$

$$F''G+FG''=0\quad\Rightarrow\quad\frac{F''}{F}+\frac{G''}{G}=0$$

ie.

$$\frac{F''}{F}=k,\qquad\frac{G''}{G}=-k,\qquad k\ \text{constant.}$$

boundary condition: $F(0)=F(2)=G(0)=0$

first solve ①: $F''-kF=0$, $F(0)=F(2)=0$

$k=-p^2<0\ \Rightarrow\ F=A\cosh{px}+B\sinh{px}$

$$F(0)=0\ \Rightarrow A=0$$
$$F(2)=0\ \Rightarrow B=0,\quad\text{ie only trivial solutions}$$

$k=0\ \Rightarrow\ F=Ax+B$

$$F(0)=0\ \Rightarrow B=0,\quad F(2)=0\ \Rightarrow A=0$$

again, only trivial solution.

$k=p^2>0\ \Rightarrow\ F=A\cos{px}+B\sin{px}$

$$F(0)=0\ \Rightarrow\ A=0$$

ie $F=B\sin px$, $F(2)=0\Rightarrow p=\frac{n\pi}{2}$

now solve ②: $G''+kG=0$, $k=p^2$, $p=\frac{n\pi}{2}$

$$G=A\cosh\frac{n\pi y}{2}+B\sinh\frac{n\pi y}{2}$$

$G(0)=0\Rightarrow A=0$

$$\Rightarrow\ u(x,y)=\sum_{n=1}^{\infty}A_n\sin\frac{n\pi x}{2}\sinh\frac{n\pi y}{2}$$

*Kjeldevarsel (losningsfila): To feil i løysingsmanuset, begge i forteiknsmerkinger. (1) Merkingsa for separasjonskonstanten er bytta om: sidan likninga er $F''-kF=0$, høyrer $F=A\cosh px+B\sinh px$ til tilfellet $k=p^2>0$ og $F=A\cos px+B\sin px$ til $k=-p^2<0$; tilsvarande høyrer $G=A\cosh\frac{n\pi y}{2}+B\sinh\frac{n\pi y}{2}$ til $G''-kG=0$ med $k=p^2$. (2) I tilfellet $k=0$ står det $F(2)=0\Rightarrow B=0$; det skal vera $A=0$ (allereie retta over). Resten av løysinga — eigenverdiane $p=\frac{n\pi}{2}$ og det endelege svaret — er korrekt som skriven.*

**c)** use $u(x,1)=\sin\pi x\cos 2\pi x$

$$=\frac{1}{2}\left(\sin 3\pi x-\sin\pi x\right)$$

$$\text{eg}\quad A_n=\left\{\begin{array}{ll} -1/2\,\left/\sinh\pi\right., & n=2\\[6pt] 1/2\,\left/\sinh 3\pi\right., & n=6\\[6pt] 0 & \text{other } n \end{array}\right.$$

$$u(x,y)=\frac{-\sin\pi x\,\sinh\pi y}{2\sinh\pi}+\frac{\sin 3\pi x\,\sinh 3\pi y}{2\sinh 3\pi}$$

Kildesett: course=TMA4125 term=kont year=2017 problem=2 file=kont_bok.pdf
