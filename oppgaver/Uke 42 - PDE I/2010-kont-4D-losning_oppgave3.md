### **Løsning til Oppgave 3**

a)  Vi setter $u(x,y)=F(x)G(y)$ inn i differensialligningen og får

$$F''G+4FG''=0$$

som gir

$$\frac{F''}{F}+4\frac{G''}{G}=0$$

som igjen gir

$$\frac{F''}{F}=k\quad\text{og}\quad\frac{G''}{G}=-\frac{k}{4}.$$

Randbetingelsene gir oss at $k=-n^2$ for $n=1,2,3,\ldots$. Dette gir

$$F_n(x)=\sin nx\qquad\text{og}\qquad G_n(y)=A_n\cosh\frac{n}{2}y+B_n\sinh\frac{n}{2}y,$$

og følgelig er

$$u_n(x,y)=\sin nx\left(A_n\cosh\frac{n}{2}y+B_n\sinh\frac{n}{2}y\right).$$

b)  Siden ligningen (I) og randbetingelsene (II) er homogene kan vi benytte superposisjonsprinsippet. En funksjon som tilfredsstiller både (I), (II) og (III) er av formen $u(x,y)=\sum_{n=1}^{\infty}u_n(x,y)$.

Setter vi $y=0$ finner vi $0=\sum_{n=1}^{\infty}A_n\sin nx$, som viser at $A_n=0$ for alle $n$.

Ved å sette inn $y=2$ finner vi $x(\pi-x)=\sum_{n=1}^{\infty}B_n\sin nx\sinh n$, som viser at $B_n\sinh n=b_n$ for alle $n$. Altså er

$$u(x,y)=\sum_{n=1}^{\infty}\frac{b_n}{\sinh n}\sin nx\sinh\left(\frac{n}{2}y\right).$$

Kildesett: course=TMA4135 term=kont year=2010 problem=3 file=tma4135_10k.pdf
