### **Solution to Problem 6** **Wave Equation [10 pts]**

a)

$$\begin{aligned}\hat u_t&=-c\frac{m\pi}{L}\sin(\frac{m\pi}{L}x)\sin(c\frac{m\pi}{L}t)\\
\hat u_{tt}&=-c^2\frac{m^2\pi^2}{L^2}\sin(\frac{m\pi}{L}x)\cos(c\frac{m\pi}{L}t)\\
\hat u_x&=\frac{m\pi}{L}\cos(\frac{m\pi}{L}x)\cos(c\frac{m\pi}{L}t)\\
\hat u_{xx}&=-\frac{m^2\pi^2}{L^2}\sin(\frac{m\pi}{L}x)\cos(c\frac{m\pi}{L}t)\end{aligned}$$

We see that $\hat u_{tt}=c^2\hat u_{xx}$.

$$\begin{aligned}\tilde u_t&=\frac{1}{2}\Big(-c\frac{m\pi}{L}\cos\Big(\frac{m\pi}{L}(x-ct)\Big)+c\frac{m\pi}{L}\cos\Big(\frac{m\pi}{L}(x+ct)\Big)\Big)\\
\tilde u_{tt}&=\frac{1}{2}\Big(-c^2\frac{m^2\pi^2}{L^2}\sin\Big(\frac{m\pi}{L}(x-ct)\Big)-c^2\frac{m^2\pi^2}{L^2}\sin\Big(\frac{m\pi}{L}(x+ct)\Big)\Big)\\
\tilde u_x&=\frac{1}{2}\Big(\frac{m\pi}{L}\cos\Big(\frac{m\pi}{L}(x-ct)\Big)+\frac{m\pi}{L}\cos\Big(\frac{m\pi}{L}(x+ct)\Big)\Big)\\
\tilde u_{xx}&=\frac{1}{2}\Big(-\frac{m^2\pi^2}{L^2}\sin\Big(\frac{m\pi}{L}(x-ct)\Big)-\frac{m^2\pi^2}{L^2}\sin\Big(\frac{m\pi}{L}(x+ct)\Big)\Big)\end{aligned}$$

We see that $\tilde u_{tt}=c^2\tilde u_{xx}$.

b) Use trigonometric identity

$$2\sin(x)\cos(y)=\sin(x+y)+\sin(x-y).$$

c) Recall D'Alembert's solution of the 1-D wave equation

$$u(x,t)=\frac{1}{2}\bigg(f^*(x+ct)+f^*(x-ct)+\frac{1}{c}\int_{x-ct}^{x+ct}g^*(s)ds\bigg).$$

Here $f^*$ and $g^*$ are odd and 2L-periodic. Then

c1)

$$u(x,t+\frac{L}{c})=\frac{1}{2}\bigg(f^*(x+ct+L)+f^*(x-ct-L)+\frac{1}{c}\int_{x-ct-L}^{x+ct+L}g^*(s)ds\bigg).$$

Properties of $f^*$ and $g^*$ imply:

c2) (1p)

$$f^*(x+ct+L)=f^*(x+ct+L-2L)=-f^*(L-x-ct)=-f^*(x+ct)$$

and

c2) (1p)

$$f^*(x-ct-L)=-f^*(L-x+ct)=-f^*(L-(x-ct))=-f^*(x-ct)$$

and

c2) (1p)

$$g^*(s+L)=-g^*(-s-L)=-g^*(-s-L+2L)=-g^*(L-s)=-g^*(s).$$

A change of variables then gives

$$\begin{aligned}\frac{1}{c}\int_{x-ct-L}^{x+ct+L}g^*(s)ds&\stackrel{c3)}{=}\frac{1}{c}\int_{x-ct}^{x+ct}g^*(s+L)ds\\
&\stackrel{c4)}{=}\frac{-1}{c}\int_{x-ct}^{x+ct}g^*(s)ds.\end{aligned}$$

Adding these identities up yields the statement

c5)

$$u(x,t+\frac{L}{c})=-u(x,t).$$

**Grading manual**

a) (1p)

b) (2p)

c) (7p):

c1) (1p), c2) (1p)+(1p)+(1p), c3) (1p), c4) (1p), c5) (1p)

Kildesett: course=TMA4135 term=host year=2024 problem=6 points=10 file=exam_math_4n_4d_tma4130_35-8.pdf
