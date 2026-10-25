### **Problem 6** **Wave Equation [10 pts]**

a) Verify by explicit computations that the function:

$$\hat u(x,t)=\sin(\frac{m\pi}{L}x)\cos(c\frac{m\pi}{L}t)$$

and the function

$$\tilde u(x,t)=\frac{1}{2}\bigg(\sin\Big(\frac{m\pi}{L}(x-ct)\Big)+\sin\Big(\frac{m\pi}{L}(x+ct)\Big)\bigg)$$

are both solutions of the 1-D wave equation

$$u_{tt}=c^2u_{xx},$$

with initial conditions conditions (initial shape) $u(x,0)=f(x)=\sin(\frac{m\pi}{L}x)$ and (vibration from rest) $u_t(x,0)=g(x)=0$.

b) Show that $\hat u=\tilde u$.

Hint: Use a trigonometric identity.

c) Suppose that the functions $f$ and $g$ have the following symmetry properties for $0\le x\le L$: $f(L-x)=f(x)$ and $g(L-x)=g(x)$, i.e., both are symmetric around $2x=L$. Use d'Alembert's solution of the 1-D wave equation

$$u(x,t)=\frac{1}{2}\bigg(f^*(x+ct)+f^*(x-ct)+\frac{1}{c}\int_{x-ct}^{x+ct}g^*(s)ds\bigg),$$

where $f^*$ and $g^*$ are the (2L-periodic) odd extensions of $f$ respectively $g$, to show for all $0<x<L$ and $t>0$ that

$$u(x,t+\frac{L}{c})=-u(x,t).$$

Kildesett: course=TMA4135 term=host year=2024 problem=6 points=10 file=exam_math_4n_4d_tma4130_35-8.pdf
