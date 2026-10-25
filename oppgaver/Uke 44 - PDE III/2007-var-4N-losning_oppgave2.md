### **Løsning til Oppgave 2**

*Problem 2*

Gitt den partielle differensialligningen

$$(*)\qquad\frac{\partial u}{\partial t}-\frac{\partial^{2}u}{\partial x^{2}}+2u=0,\qquad 0<x<\pi,\quad t>0$$

*a.* Finn alle løsninger av formen $u(x,t)=X(x)T(t)$ av (*) som tilfredsstiller randbetingelsene

$$(1)\qquad u_{x}(0,t)=0,\qquad u_{x}(\pi,t)=0,\quad t>0$$

*b.* Finn løsninger av (*) som tilfredsstiller randbetingelsene (1) og også initialbetingelsen

$$(2)\qquad u(x,0)=\sin^{2}{x}+2\cos{x},\qquad 0<x<\pi$$

**(a)** $u(x,t)=X(x)T(t)\Rightarrow\dfrac{X^{\prime\prime}}{X}=\dfrac{\dot{T}}{T}+2=p$

$$\Rightarrow\ X^{\prime\prime}-pX=0,\quad 0<x<\pi,\quad X^{\prime}(0)=0,\ \ X^{\prime}(\pi)=0\quad\Bigl\}\Rightarrow$$

$$p=-k^{2},\quad k=0,1,2,\ldots$$

$$X_{0}(x)=C$$

$$X_{k}(x)=\cos{kx},\quad k=1,2,\ldots$$

$$\frac{\dot{T}(t)}{T(t)}=-k^{2}-2\ \Rightarrow\quad T_{k}(t)=e^{-(2+k^{2})t}$$

General solution: $u_{0}(x,t)=Ce^{-2t}$,

$$u_{k}(x,t)=C_{k}\cos{kx}\cdot e^{-(2+k^{2})t},\quad k>0.$$

**(b)** $\sin^{2}{x}=\dfrac{1}{2}-\dfrac{1}{2}\cos{2x}$

$$(2)\Rightarrow\ u(x,0)=\frac{1}{2}+2\cos{x}-\frac{1}{2}\cos{2x}$$

$$\Rightarrow u(x,t)=\frac{1}{2}e^{-2t}+2\cos{x}\ e^{-3t}-\frac{1}{2}\cos{2x}\ e^{-6t}$$

*Kjeldevarsel: LF er handskriven (s. 9–10 i PDF-en), delvis på engelsk («General solution»), og er transkribert ordrett; overstreka utkast er utelne (eit overstreka ledd i framstillinga av general solution). Alle tal er kontrollreikna med sympy: $u_{k}=e^{-(2+k^{2})t}\cos kx$ løyser (*) og $u_{x}(0,t)=u_{x}(\pi,t)=0$ for heiltal $k\geq 0$, og sluttløysinga $u=\frac{1}{2}e^{-2t}+2\cos x\,e^{-3t}-\frac{1}{2}\cos 2x\,e^{-6t}$ løyser likninga, randvilkåra og initialkravet $\sin^{2}x+2\cos x$ eksakt.*

Kildesett: course=TMA4123 term=var year=2007 problem=2 file=TMA4123_v07.pdf
