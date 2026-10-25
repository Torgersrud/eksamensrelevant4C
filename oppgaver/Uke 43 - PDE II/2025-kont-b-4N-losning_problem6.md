### **Solution to Problem 6** **Heat Equation (10 points)**

a) Assume $u(x,t)=X(x)T(t)$. Then
$$\frac{T'}{6T}=\frac{X''}{X}=-\lambda.$$

So $X''+\lambda X=0$ with $X(0)=X(\pi)=0$. We only find nontrivial solutions when $\lambda=n^2$ and these are $X_n(x)=\sin(nx)$. This gives the equation
$$T'=-6n^2T,$$
which has general solution $T_n(t)=e^{-6n^2t}$. This gives the eigenfunctions
$$u_n(x,t)=X_n(x)T_n(t)=\sin(nx)e^{-6n^2t}.$$

b) The solution is a series of eigenfunctions
$$u(x,t)=\sum_{n=1}^{\infty}b_nu_n(x,t)=\sum_{n=1}^{\infty}b_n\sin(nx)e^{-6n^2t}.$$

From the initial condition we see that $b_1=3$, $b_2=2$, $b_3=1$. So the general solution is
$$u(x,t)=3e^{-6t}\sin x+2e^{-24t}\sin(2x)+e^{-54t}\sin(3x).$$

c) We find that
$$\lim_{t\to0}u(x,t)=0,$$
which is consistent with the interpretation of the boundary conditions that the rod is in contact with some heat conducting material with temperature held fixed at 0 at the endpoints $x=0$ and $x=\pi$. In such a physical system the rod will eventually reach thermodynamic equilibrium with the exterior and attain the temperature 0 uniformly.

**Grading manual**

a) (5p)

b) (3p)

c) (2p)

Kildesett: course=TMA4130 term=kont year=2025 problem=6 points=10 file=exam_math_4n_4d_tma4130_35-15.pdf
