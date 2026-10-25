### **Solution to Problem 10** (B-Splines, 11 points)

We have to check whether for a function $f$

1. $\left.f\right|_{I_j}\in\mathbb{P}_3$, $I_j=[x_{j-1},x_j]$,
2. $f\in C^{2}[a,b]$,

where we here have $x_j=-1+j$, $j=0,\ldots,4$, and hence $a=x_0=-1$, $b=x_4=3$. We obtain

a) $f_1(x)$ is a cubic polynomial on $[-1,3]$ and hence a spline. (2 P.)

b) $f_2$ is not a polynomial on the interval $[0,1]$ since at $x=\frac{1}{2}$ the function is not differentiable. So either an argument that 1. or that 2. is not fulfilled is enough to conclude that this is not a spline. (2 P.)

c) We first resolve the definitions of $(\cdot)_{+}$ and obtain

$$f_3(x)=\begin{cases}0&\text{for}\ x\in[-1,0),\\ 4x^{2}&\text{for}\ x\in[0,2),\\ 4x^{2}+2(x-2)^{3}&\text{for}\ x\in[2,3]\end{cases}$$

and we see that in every segment we have a polynomial of degree at most 3, so 1. is fulfilled.

It remains to check the inner knots $0,1,2$ to see whether the function is twice continuously differentiable.

We compute the first and second derivative

$$f_3'(x)=\begin{cases}0&\text{for}\ x\in[-1,0),\\ 8x&\text{for}\ x\in[0,2),\\ 8x+6(x-2)^{2}&\text{for}\ x\in[2,3].\end{cases}\quad\text{and}\quad f_3''(x)=\begin{cases}0&\text{for}\ x\in[-1,0),\\ 8&\text{for}\ x\in[0,2),\\ 8+12(x-2)&\text{for}\ x\in[2,3].\end{cases}$$

The first derivative is still continuous, but the second is not, since

$$\left.f_3''(0)\right|_{[-1,0]}=0\neq 8=\left.f_3''(0)\right|_{[0,1]}$$

and we do not have a spline in this case. (3 P.)

d) The dimension of the space is $n+k$, where $n+1$ is the number of nodes (since we denote them by $x_0,\ldots,x_n$), and $k$ is the polynomial degree. Here we have $n+1=5$ nodes so $n=4$ and polynomial degree $k=3$ so the dimension is 7.(2 P.)

e) A spline $s$ is called *natural* if the second derivative vanishes at the boundary, here $s''(-1)=s''(3)=0$. (2 P.)

Kildesett: course=TMA4432 term=test year=2026 problem=10 points=11 file=test-exam-math4c_web.pdf
