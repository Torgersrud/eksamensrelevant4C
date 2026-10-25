### **Solution to Problem 4** **Classification and Verification of PDEs (9 points)**

a) Each PDE has to be classified with respect to linearity, homogenity and its order.

1) nonlinear (due to $u^2$), homogeneous, order 3 (on the left)

*Alternatively* it is ok to write that we only introduced homogeneity for linear PDEs or that this is inhomogeneous, since $cu$ is not a solution if $u$ is a solution due to the last term.

2) linear, inhomogeneous (due to $x+t$), order 4 (first term on the right)

b) We have
$$\frac{\partial^3}{\partial t^3}u=-8e^{-2t}\sin(4x)\quad\text{ and }\quad\frac{\partial^2}{\partial x^2}u=-16e^{-2t}\sin(4x)$$
and hence the PDE holds.

We have at the boundary that $\sin(\pm 4\pi)=0$ such that the BC is fulfilled as well.

The solution is not unique. One can either argue with missing initial conditions or that for example $\tilde u(x,t)=2u(x,t)$ or even $u=0$ is a solution, or any linear combination of these.

**Grading manual**

a) (6p)

b) (3p)

Kildesett: course=TMA4125 term=var year=2024 problem=4 points=9 file=math4n-2024v-en_lf.pdf
