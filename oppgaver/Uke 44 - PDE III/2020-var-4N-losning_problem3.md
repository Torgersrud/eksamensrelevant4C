### **Solution to Problem 3** (heat equation)

**a)** Find all solutions of the heat equation which are of the form $u(x,t) = F(x)G(t)$ and satisfy the given boundary conditions. (10 pts)
**b)** Find the solution which also satisfies the initial condition. (5 pts)

**a)**
- Separation of variables. Ansatz: $u(x,t) = F(x)G(t)$, then

  $$\partial_t u = G'(t) F(x) = c^2 G(t) F''(x)$$

  Sorting terms,

  $$\frac{G'(t)}{c^2 G(t)} = \frac{F''(x)}{F(x)} \qquad (1 \text{ pt})$$

  (left-hand side a *function in $t$*, right-hand side a *function in $x$*). Since $x$ and $t$ can vary independent of each other, we must have that

  $$\frac{G'(t)}{c^2 G(t)} = E = \frac{F''(x)}{F(x)}$$

  for some constant $E$ which we don't know yet. Thus we get

  $$\begin{aligned} F''(x) + E F(x) &= 0 \\ G'(t) + c^2 E\, G(t) &= 0 \end{aligned} \qquad (1 \text{ pt})$$

  Let's have a look at $E$ and $F$ first.

  - [?] The scheme works with the PDE $\partial_t u = c^2 \partial_{xx} u$ and general interval length $L$, specializing to $c = 1$, $L = 4$ at the end; and the constant $E$ is introduced with the sign convention of the two ODEs above (i.e. the shared value of the two quotients is $-E$).

- **Case $E = 0$:** Then $F''(x) = 0 \Rightarrow F(x) = A + Bx$ for some constants $A, B$. B.c. gives $F(0)G(t) = 0$ so either $G(t) = 0 \ \forall t$ (which is uninteresting since $u(x,t) = 0 \ \forall x,t$) or $F(0) = 0$. If $F(0) = 0 \Rightarrow A = 0$. Second b.c gives $F(L)G(t) = 0$, same reasoning as before gives $F(L) = BL = 0 \Rightarrow 0$, so $F(x) = 0$ if $L \neq 0$. That is dull. :) (2 pts (1 pt for the trivial answer))

- **Case $E < 0$:** Then $F'' + EF$ has the general solution

  $$F(x) = A e^{\sqrt{-E}\,x} + B e^{-\sqrt{-E}\,x}.$$

  Using our boundary conditions again and excluding $G(t) \equiv 0$, we get that

  $$\begin{aligned} F(0) &= A + B = 0 \\ F(L) &= A e^{\sqrt{-E}\,L} + B e^{-\sqrt{-E}\,L} = 0 \end{aligned} \iff \underbrace{\begin{pmatrix} 1 & 1 \\ e^{\sqrt{-E}\,L} & e^{-\sqrt{-E}\,L} \end{pmatrix}}_{=: C} \begin{pmatrix} A \\ B \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

  $$\det C = e^{-\sqrt{-E}\,L} - e^{\sqrt{-E}\,L} \begin{cases} = 0 & \text{if } E = 0 \\ < 0 & \text{if } E < 0. \end{cases}$$

  So for $E < 0$, matrix $C$ is invertible $\Rightarrow A = B = 0$. This is a very unexciting solution. (2 pts (1 pt for trivial answer))

- **Case $E > 0$:** Still our general solution is

  $$F(x) = \tilde{A} e^{\sqrt{-E}\,x} + \tilde{B} e^{-\sqrt{-E}\,x} = \tilde{A} e^{i\sqrt{E}\,x} + \tilde{B} e^{-i\sqrt{E}\,x} \quad \text{but now}$$

  so in general our solution $F$ can now written as

  $$F(x) = A \cos \sqrt{E}\, x + B \sin \sqrt{E}\, x. \qquad (1 \text{ pt for identifying general solution of } F)$$

  - Using b.c. $u(0,t) = 0$ we get $F(0) = A = 0$.
  - Using b.c. $u(L,t) = 0$ we get

    $$F(L) = B \sin \sqrt{E}\, L = 0$$

    This we can satisfy for some non-trivial $B$ if $\sqrt{E}\, L$ is some integer multiple of $\pi$:

    $$\sqrt{E}\, L = n\pi \iff E = \left( \frac{n\pi}{L} \right)^2. \qquad (1 \text{ pt for identifying condition on } E)$$

  - Enough to consider $n > 0$, otherwise $\sin$ just changes sign and can be incorporated into $B$.

- Now we can turn to $G(t)$:

  $$G'(t) + c^2 E\, G(t) = 0$$

  For each $n$ will we get an equation

  $$G_n'(t) + \left( \frac{c\,n\pi}{L} \right)^2 G(t) = 0 \ \Rightarrow\ G_n(t) = A_n e^{-\left( \frac{cn\pi}{L} \right)^2 t} = A_n e^{-\left( \frac{n\pi}{4} \right)^2 t} \qquad (1 \text{ pt})$$

  (where $c = 1$, $L = 4$.)

So starting from the separation of variables ansatz and incorporating b.c. and ignoring trivial/uninteresting solutions we get possible solution functions of the form

$$\begin{aligned} u_n(x,t) = F(x) G_n(t) &= A_n e^{-\left( \frac{cn\pi}{L} \right)^2 t} \sin\left( \frac{n\pi}{L}\, x \right) \qquad (1 \text{ pt}) \\ &= A_n e^{-\left( \frac{n\pi}{4} \right)^2 t} \sin\left( \frac{n\pi}{4}\, x \right). \end{aligned}$$

**b)** Superimposition of $u_n$:

$$u(x,t) = \sum_{n=1}^{\infty} A_n e^{-\left( \frac{cn\pi}{L} \right)^2 t} \sin\left( \frac{n\pi}{L}\, x \right) \qquad (\text{Superimposition, } 1 \text{ pt})$$

- Use initial condition to determine $A_n$. (Initial condition)

  $$f(x) = u(x,0) = \sum_{n=1}^{\infty} A_n \sin\left( \frac{n\pi}{L}\, x \right) \qquad (1 \text{ pt})$$

  Thus $A_n$ are the coefficients of the sin serie's of the odd extension of $f$.

- Now $f(x) = 2\sin(3\pi x) = 2\sin\left( \frac{12\pi}{L}\, x \right)$ with $L = 4$, so the sin series of the odd extension of $f$ is just $f$ itself and thus (Finding $A_n$, 2 pts)

  $$A_n = \begin{cases} 2 & \text{if } n = 12 \\ 0 & \text{else.} \end{cases}$$

Thus

$$u(x,t) = 2 e^{-\left( 3\pi \right)^2 t} \sin(3\pi x). \qquad (\text{Final solution, } 1 \text{ pt})$$

Kildesett: course=TMA4125 term=var year=2020 problem=3 file=exam_v20_short.pdf
