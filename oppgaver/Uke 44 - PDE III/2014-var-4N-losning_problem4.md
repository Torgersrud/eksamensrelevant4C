### **Solution to Problem 4**

**a)** We begin by inserting the assertion $u(t,x)=G(t)F(x)$ in the PDE to obtain that

$$G^{\prime}(t)F(x)-tG(t)F^{\prime\prime}(x)=0.$$

By dividing by $tG(t)F(x)$, we obtain that

$$\frac{G^{\prime}(t)}{tG(t)}=\frac{F^{\prime\prime}(x)}{F(x)}=k-\text{constant}.$$

Hence, we have the following two ODEs:

$$\begin{gathered}G^{\prime}(t)-ktG(t)=0,\\ F^{\prime\prime}(x)-kF(x)=0.\end{gathered}$$

The second ODE will have two different types of solutions according to the sign of $k$. If $k>0$, then $F$ will be of the form $F(x)=Ae^{\sqrt{k}x}+Be^{-\sqrt{k}x}$. However, this cannot satisfy the boundary conditions. That is, $F(0)=0$ and $F(1)=0$ can only happen if $F(x)\equiv 0$ when $k>0$. Hence, we must have that $k<0$.

For convenience, let us now write $k=-\lambda^{2}$. Then, the solutions to the above ODEs are

$$G(t)=Ce^{-\lambda^{2}t^{2}},\qquad F(x)=A\cos(\lambda x)+B\sin(\lambda x).$$

To satisfy boundary conditions, we need that $F(0)=0$ and $F(1)=0$. For the first requirement, we see that

$$F(0)=A\quad\Rightarrow\quad A=0.$$

For the second requirement, we see that

$$F(1)=B\sin(\lambda)\quad\Rightarrow\quad\lambda=n\pi.$$

Hence, for any choice of constants $C$ and $B$ and any integer $n$, we have found that

$$G(t)F(x)=CBe^{-n^{2}\pi^{2}t^{2}}\sin(nx),$$

solves the PDE with the given boundary conditions. Hence, all non-trivial solution can be obtained by summing over all possible choices of constants $C$, $B$, and frequencies $n$ yielding

$$u(t,x)=\sum_{n=0}^{\infty}B_{n}e^{-(n\pi)^{2}t^{2}}\sin(nx).$$

(Since $C$ and $B$ only appear as $CB$ this only provides one degree of freedom which we denote by $B_{n}$).

**b)** We are now to determine the coefficients $B_{n}$ in $u(t,x)$ to satisfy the given initial value. That is, find $B_{n}$ such that

$$u(0,x)=\sum_{n=0}^{\infty}B_{n}\sin(nx)=2\sin(\pi x)+\frac{5}{3}\sin(30\pi x)+\frac{1}{7}\sin(11\pi x).$$

We readily see that,

$$B_{1}=2,\quad B_{30}=\frac{5}{3},\quad B_{11}=\frac{1}{7},\quad B_{n}=0,\quad\forall n\neq 1,11,30.$$

Hence, the solution $u(t,x)$ is given by

$$u(t,x)=2e^{-\pi^{2}t^{2}}\sin(\pi x)+\frac{1}{7}e^{-(11)^{2}\pi^{2}t^{2}}\sin(11\pi x)+\frac{5}{3}e^{-(30)^{2}\pi^{2}t^{2}}\sin(30\pi x).$$

*Kjeldevarsel: Eksponenten i $G(t)$ og i rekkjene i a) og b) er trykt som $-\lambda^{2}t^{2}$ og $-(n\pi)^{2}t^{2}$, men separasjon av $G^{\prime}=ktG$ gjev $G=Ce^{-\lambda^{2}t^{2}/2}$: set ein $u=e^{-(n\pi)^{2}t^{2}}\sin(n\pi x)$ inn i $u_{t}=t\,u_{xx}$ står att residual $-\pi^{2}n^{2}t\cdot u$ (kontrollrekna med sympy), medan $u=e^{-(n\pi)^{2}t^{2}/2}\sin(n\pi x)$ løyser PDE-en nøyaktig. Heile LF-en følgjer den factor-2-for-lille eksponenten konsekvent; elles er reknegangen korrekt.*

Kildesett: course=TMA4123 term=var year=2014 problem=4 file=v14-english.pdf
