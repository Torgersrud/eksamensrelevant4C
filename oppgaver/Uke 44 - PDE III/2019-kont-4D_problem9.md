### **Problem 9**

We will solve the heat equation

$$u_t=u_{xx},$$

for $0\leq x\leq 1$ and $t\geq 0$ with boundary conditions

$$u(0,t)=u(1,t)=0$$

and initial conditions

$$u(x,0)=x-x^2$$

Write down a complete algorithm that solves the problem with an explicit scheme for $t\in[0,1]$. Use step sizes $h=1/M$ and $k=1/N$ in $x-$ and $t-$directions, respectively.

Let $h=0.2$ and $k=0.02$ and find an approximation to $u(0.4,0.02)$.

Assume you run your algorithm for $h=k$. What kind behaviour will you expect from the numerical solution?

Kildesett: course=TMA4135 term=kont year=2019 problem=9 file=exam_in_english.pdf
