### **Solution to Problem 2**

**(1. approach.)** Equivalently, we have to find the best approximation of $f(x)=\sin(\pi x)$ from the closed subspace $M=\mathrm{span}\{1,x,x^2\}$. We use that this is equivalent to finding a $p\in M$ such that $\langle f-p,q\rangle=0$ for all $q\in M$. Since $\{1,x,x^2\}$ is a basis we have to only check this for the monomials:

$$0=\int_0^1(\sin(\pi x)-a-bx-cx^2)\cdot 1\,dx$$
$$0=\int_0^1(\sin(\pi x)-a-bx-cx^2)\cdot x\,dx$$
$$0=\int_0^1(\sin(\pi x)-a-bx-cx^2)\cdot x^2\,dx$$

which gives us a system of equations for the coefficients $a,b,c$. Let us first compute $\int_0^1 x\sin(\pi x)dx$ and $\int_0^1 x\sin(\pi x)dx$ with partial integration.

$$\int_0^1 x\sin(\pi x)dx=\left.\frac{\sin(\pi x)-\pi x\cos(\pi x)}{\pi^2}\right|_0^{\pi}=\frac{1}{\pi}$$

$$\int_0^1 x^2\sin(\pi x)dx=\left.\frac{2\pi x\sin(\pi x)+(2-\pi^2x^2)\cos(\pi x)}{\pi^3}\right|_0^{\pi}=\frac{\pi^2-4}{\pi^3}$$

The coefficients have to satisfy

$$\frac{2}{\pi}=a+\frac{b}{2}+\frac{c}{3}$$
$$\frac{1}{\pi}=\frac{a}{2}+\frac{b}{3}+\frac{c}{4}$$
$$\frac{\pi^2-4}{\pi^3}=\frac{a}{3}+\frac{b}{4}+\frac{c}{5}$$

The solution is given by $a=\frac{12(\pi^2-10)}{\pi^3}$, $b=-\frac{60(\pi^2-12)}{\pi^3}$ and $c=\frac{60(\pi^2-12)}{\pi^3}$.

**(2. approach:)** Replace $\{1,x,x^2\}$ in $(L^2[0,1],\langle.,.\rangle)$ by an orthonormal system, by example using Gram-Schmidt orthogonalization: $e_0(x)=1$, $e_1(x)=2\sqrt{3}(x-\frac{1}{2})$, $e_2(x)=6\sqrt{5}(x^2-x+\frac{1}{6})$. Hence the best approximation of $f(x)=\sin(\pi x)$ by elements from the subspace spanned by $\{1,x,x^2\}$ is thus given by

$$\tilde{f}=\sum_{i=0}^{2}\langle f,e_i\rangle e_i$$

. The Fourier coefficients $\langle f,e_i\rangle$ are

$$\langle f,e_0\rangle=\int_0^1 1\cdot\sin(\pi x)\,dx=\frac{2}{\pi}$$

$$\langle f,e_1\rangle=2\sqrt{3}\int_0^1(x-\tfrac{1}{2})\cdot\sin(\pi x)\,dx=0$$

$$\langle f,e_2\rangle=6\sqrt{5}\int_0^1(x^2-x+\tfrac{1}{6})\cdot\sin(\pi x)\,dx=\frac{2\sqrt{15}(\pi^2-12)}{\pi^3}$$

and which gives $a=\frac{12(\pi^2-10)}{\pi^3}$, $b=-\frac{60(\pi^2-12)}{\pi^3}$ and $c=\frac{60(\pi^2-12)}{\pi^3}$ after rewriting the $e_i's$ in the monomial basis.
Comment: This approach is computationally more involved than the first approach due to the Gram-Schmidt orthogonalization and thus the first approach is to prefer.

Kildesett: course=TMA4145 term=host year=2019 problem=2 file=tma4105eksamen-engelsk.pdf
