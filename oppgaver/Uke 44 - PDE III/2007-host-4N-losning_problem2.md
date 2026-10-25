### **Solution to Problem 2**

**a.** Let a function $f(x)$, $x\in(0,2\pi)$ be defined by the relation

$$f(x)=\begin{cases}x, & \text{if } 0\leq x\leq\pi;\\ 2\pi-x, & \text{if } \pi\leq x\leq 2\pi.\end{cases}$$

Find the sine Fourier series of $f$.

*Solution.* The general formula has the form

$$b_{n}=\frac{2}{L}\int_{0}^{L}f(x)\sin\frac{n\pi}{L}x\ \,dx.$$

In the our case $L=2\pi$ and

$$b_{n}=\frac{1}{\pi}\int_{0}^{\pi}x\sin\frac{n}{2}x\ \,dx+\frac{1}{\pi}\int_{\pi}^{2\pi}(2\pi-x)\sin\frac{n}{2}x\ \,dx=I_{1}+I_{2}.$$

A direct evaluation of the integrals gives

$$I_{1}=-\frac{1}{\pi}\cos\frac{n\pi}{2}+\frac{4}{\pi n^{2}}\sin\frac{n\pi}{2},\quad I_{2}=\frac{1}{\pi}\cos\frac{n\pi}{2}+\frac{4}{\pi n^{2}}\sin\frac{n\pi}{2},$$

and

$$b_{n}=I_{1}+I_{2}=\frac{8}{\pi n^{2}}\sin\frac{n\pi}{2}=\begin{cases}0, & \text{if } n=2k;\\ (-1)^{k}\frac{8}{\pi(2k+1)^{2}}, & \text{if } n=2k+1.\end{cases}$$

Finally

$$f(x)\sim\frac{8}{\pi}\sum_{k=0}^{\infty}\frac{(-1)^{k}}{(2k+1)^{2}}\sin\frac{2k+1}{2}x \tag{2}$$

**b.** Find all solutions of the form $u(x,t)=X(x)T(t)$ for the problem

$$\frac{\partial u}{\partial t^{2}}=\frac{\partial^{2}u}{\partial t^{2}}+u,\quad 0<x<2\pi,\ t>0, \tag{3}$$

which satisfy the boundary conditions

$$u(0,t)=0,\ u(2\pi,t)=0,\quad t>0. \tag{4}$$

*Solution.* Substituting a function $u$ of the form $u(x,t)=X(x)T(t)$ we obtain

$$\frac{T^{\prime}(t)}{T(t)}-1=\frac{X^{\prime\prime}(x)}{X(x)}=k.$$

This is a constant because it is independent both of $t$ and $x$. Taking into account the boundary conditions (4) we obtain an equation with respect to $X$:

$$X^{\prime\prime}(x)-kX(x)=0,\ 0>x<2\pi,\quad \text{and } X(0)=0,\ X(2\pi)=0. \tag{5}$$

and an equation with respect to $T$:

$$T^{\prime}(t)-(k+1)T(t)=0,\ t>0. \tag{6}$$

The standard analysis shows that the only possible $k$'s for which the problem (5) has non-trivial solutions are of the form

$$k_{n}=-\Bigl(\frac{n}{2}\Bigr)^{2},\ n=1,2,\ldots.$$

The corresponding solutions of (5) are of the form

$$X_{n}(x)=A_{n}\sin\frac{n}{2}x,\ n=1,2,\ldots\quad.$$

For each $k_{n}$ equation (6) takes now the form

$$T_{n}^{\prime}(t)-\Bigl(1-(\frac{n}{2})^{2}\Bigr)T_{n}(t)=0.$$

These equations have solutions

$$T_{n}(t)=C_{n}e^{1-(\frac{n}{2})^{2}t}.$$

Finally we obtain

$$\underline{u_{n}(x,t)=B_{n}e^{1-(\frac{n}{2})^{2}t}\sin\frac{n}{2}x},\ n=1,2,\ldots\quad.$$

**c.** Find the solution of the problem (3), (4) formulated in section **b**, which in addition satisfies the initial condition

$$u(x,0)=f(x),\ 0<x<2\pi,$$

here the function $f$ is defined in section **a**.

*Answer:*

$$u(x,t)=\underline{\frac{8}{\pi}\sum_{k=0}^{\infty}\frac{(-1)^{k}}{(2k+1)^{2}}e^{-(k^{2}+k-3/4)t}\sin\frac{2k+1}{2}x}$$

*Kjeldevarsel: LF er på engelsk og er transkribert ordrett. Attmerkingar: (i) i LF si omforming av oppgåva i a) er ulikskapene skrivne med $\leq$ i staden for $<$ som i eksamensarket — verdien i skiljepunktet påverkar ikkje rekkja; (ii) i (3) er likninga trykt $\frac{\partial u}{\partial t^{2}}=\frac{\partial^{2}u}{\partial t^{2}}+u$ — etter eksamensarket skal det lesast $\frac{\partial u}{\partial t}=\frac{\partial^{2}u}{\partial x^{2}}+u$; (iii) i (5) står det trykt $0>x<2\pi$ for $0<x<2\pi$; (iv) «In the our case» og «independent both of $t$ and $x$» er LF si eiga setningsforming; (v) i $T_{n}$- og $u_{n}$-formlane er eksponenten trykt $1-(\frac{n}{2})^{2}t$ utan klammer rundt brøken. Alt er kontrollreikna med sympy: $b_{n}=\frac{8}{\pi n^{2}}\sin\frac{n\pi}{2}$ for $n=1,\ldots,6$ mot direkte integrasjon, $u_{n}=e^{(1-(n/2)^{2})t}\sin\frac{n}{2}x$ løyser likninga og randvilkåra for heiltal $n$, exponenten i svaret i c) er $1-\bigl(\frac{2k+1}{2}\bigr)^{2}=-\bigl(k^{2}+k-\tfrac34\bigr)$, og rekkja i c) konvergerer mot $f(\pi)=\pi$ for $t=0$ (summen $\frac{8}{\pi}\sum\frac{1}{(2k+1)^{2}}=\pi$).*

Kildesett: course=TMA4130 term=host year=2007 problem=2 file=exam-en_2007.pdf
