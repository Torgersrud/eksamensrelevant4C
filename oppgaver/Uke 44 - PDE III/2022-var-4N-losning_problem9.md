### **Solution to Problem 9** (Separation of Variables, 8 points)

a) We use the Ansatz $u(x,t)=F(x)G(t)$ to obtain

$$\frac{\partial^{2}}{\partial t^{2}}u(x,t)=F(x)G^{\prime\prime}(t)=-F^{(4)}(x)G(t)=-\frac{\partial^{4}}{\partial x^{4}}u(x,t)$$

which we rearrange to (1 P.)

$$\frac{G^{\prime\prime}(t)}{G(t)}=-\frac{F^{(4)}(x)}{F(x)}=-k$$

where $k$ is a constant. We obtain the two ODEs (1 P.)

$$\begin{aligned}F^{(4)}(x)-kF(x)&=0\\ G^{\prime\prime}(t)+kG(t)&=0\end{aligned}$$

b) In the Ansatz from a) the boundary conditions yield that a solution to the ODE w.r.t. $F$ has to fulfil

$$u(0,t)=F(0)G(t)=F(1)G(t)=u(1,t)=0$$

for all $t>0$. Hence $F(0)=F(1)=0$.

Similarly the other boundary conditions yield that $F^{\prime\prime}(0)=F^{\prime\prime}(1)=0$. (1 P.)

We first verify that the given form fulfils the ODE. We have

$$\begin{aligned}F^{\prime}(x)&=A\beta\cos(\beta x)-B\beta\sin(\beta x)\\ F^{\prime\prime}(x)&=-A\beta^{2}\sin(\beta x)-B\beta^{2}\cos(\beta x)\\ F^{(3)}(x)&=-A\beta^{3}\cos(\beta x)+B\beta^{3}\sin(\beta x)\\ F^{(4)}(x)&=A\beta^{4}\cos(\beta x)+B\beta^{4}\cos(\beta x)=\beta^{4}F(x)\end{aligned}$$

Hence it fulfils the ODE for $F$. (1 P.)

For the boundary conditions, we obtain

$$0=F(0)=A\cdot 0+B\cdot 1=0\Rightarrow B=0$$

So we can continue with just functions of the form $F(x)=A\sin(\beta x)$. From the second boundary condition we obtain (1 P.)

$$0=F(1)=A\sin(\beta)\Rightarrow\beta=n\pi.$$

The third and fourth boundary conditions read (1 P.)

$$0=F^{\prime\prime}(0)=-A\beta^{2}\sin(0)\qquad\text{and}\qquad 0=F(1)=-A\beta^{2}\sin(\beta)$$

The first is true for any $\beta$, the second holds for the already found $\beta=n\pi$, $\beta\in\mathbb{N}$.

c) We need two initial conditions. (1 P.)

An example would be ok as well, we usually need something like

$$\begin{cases}u(x,0)=0\\ \displaystyle\frac{\partial}{\partial t}u(x,0)=0\end{cases}$$

to get a unique solution (for each $\beta=n\pi$, $n\in\mathbb{N}$ or in other words $k=(n\pi)^{4}$ from b)) in the ODE for $G$.

d) For example $C\mathrm{e}^{\pm\beta x}$, $\beta>0$ fulfils the ODE with $k=\beta^{4}$ as well, or phrased differently, $D\sinh(\beta x)$ and $E\cosh(\beta x)$ do. (1 P.)

Kildesett: course=TMA4125 term=var year=2022 problem=9 points=8 file=TMA4125-Matematikk-4N-2022v_lf.pdf
