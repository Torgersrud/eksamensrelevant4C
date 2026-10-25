### **Løsning til Oppgave 6**

**a)** Vi stapper $u(x,t)=F(x)G(t)$ inn i varmeligningen og får

$$F''-kF=0$$

og

$$G'-kG=0.$$

På grunn av den vanlige prosedyren med randkravene ser vi at $k=-p^2<0$. Den første ligningen har løsning

$$F(x)=A\cos px+B\sin px,$$

og bruker vi randkravene $F(0)=0$ og $F(3)=0$, får vi $A=0$ og

$$\sin 3p=0,\quad\text{slik at}\quad p=\frac{n\pi}{3},\quad n=1,2,\ldots$$

Vi trenger ikke $B$, så den setter vi til 1. Den andre ligningen løses av

$$G_n(t)=B_ne^{-\left(\frac{n\pi}{3}\right)^2t}.$$

slik at alle løsninger er

$$u_n(x,t)=F(x)G_n(t)=B_n\sin\frac{n\pi x}{3}\,e^{-\left(\frac{n\pi}{3}\right)^2t}.$$

**b)** Vi summerer alle funksjonene

$$u(x,t)=\sum_{n=1}^{\infty}B_n\sin\frac{n\pi x}{3}\,e^{-\left(\frac{n\pi}{3}\right)^2t}.$$

Når vi setter

$$u(x,0)=\sum_{n=1}^{\infty}B_n\sin\frac{n\pi x}{3}=2\sin\left(\frac{\pi x}{3}\right),$$

går dette i orden dersom $B_n$ er fourierkoeffisientene til $f$. De er trivielle å beregne, siden $f$ er en sinusfunksjon. Vi får

$$B_n=0\quad\text{for }n\neq 1,\qquad B_1=2,$$

slik at

$$u(x,t)=2\sin\left(\frac{\pi x}{3}\right)e^{-(\pi/3)^2t}.$$

**c)** Crank-Nicolson er gitt ved

$$(2+2r)u_{i,j+1}-r(u_{i+1,j+1}+u_{i-1,j+1})=(2-2r)u_{ij}+\frac{1}{2}(u_{i+1,j}+u_{i-1,j}).$$

der $r=k/h^2=1/2$, så vi får

$$3u_{i,j+1}-\frac{1}{2}(u_{i+1,j+1}+u_{i-1,j+1})=u_{ij}+\frac{1}{2}(u_{i+1,j}+u_{i-1,j})$$

Vi vil finne $u_{11}\approx u(1,0.5)$, som er ett tidssteg opp fra $t=0$. Bruker vi initialkravet, får vi $u_{10}=u_{20}=1.7321$ og $u_{00}=u_{30}=0$ og . Ligningsystemet blir

$$3u_{11}-\frac{1}{2}u_{21}=2.5982$$

$$3u_{21}-\frac{1}{2}u_{11}=2.5982$$

Når dette løses på gamlemåten, får vi

$$u_{11}=u_{21}=1.0393$$

slik at

$$u(1,0.5)\approx 1.0393.$$

Kildesett: course=TMA4135 term=host year=2017 problem=6 file=tma4135_eksamen_h17.pdf
