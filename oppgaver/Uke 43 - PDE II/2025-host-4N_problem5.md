### **Problem 5** **Wave equation and Heat equation (10 points)**

a) Consider the function

$$u(x,t)=\sin(2t)\cos(x)$$

and verify that it is a solution to the wave equation

$$u_{tt}=4u_{xx}.$$

b) Let $c_1,\dots,c_n$ denote real constants and consider the modified wave equation

$$u_{tt}=\sum_{i=1}^{n}c_i^2u_{x_ix_i}.\tag{1}$$

Let $F$ be an arbitrary twice continuously differentiable function, meaning its second derivative exists and is continuous. Show that for an arbitrary vector $a=(a_1,\dots,a_n)$ the function $u(x,t)=u(x_1,\dots,x_n,t)$

$$u(x,t)=F(a\cdot x-\lambda t)$$

is a solution of (1) if

$$\lambda^2-\sum_{i=1}^{n}c_i^2a_i^2=0$$

c) Find the solution to the boundary value problem

$$u_t(x,t)-u_{xx}(x,t)=0,\quad 0<x<\pi,\quad t>0$$

$$\begin{aligned}\text i)\ &u(0,t)=0=u(\pi,t),\quad t>0\\ \text{ii})\ &u(x,0)=100,\quad 0<x<\pi.\end{aligned}$$

Note: Here you can use the formula for the solution of the heat equation derived in the lecture:

$$u(x,t)=\sum_{n=1}^{\infty}b_ne^{-\lambda_n^2t}\sin\left(\frac{n\pi}{L}x\right),\tag{2}$$

where

$$b_n=\frac{2}{L}\int_0^Lf(x)\sin\left(\frac{n\pi}{L}x\right)dx,\qquad\lambda_n=c\frac{n\pi}{L},\qquad n=1,2,\dots\tag{3}$$

You do \underline{not} need to derive the formula yourself, but you need to apply it.

Kildesett: course=TMA4130 term=host year=2025 problem=5 points=10 file=exam_math_4n_4d_tma4130_35-21.pdf
