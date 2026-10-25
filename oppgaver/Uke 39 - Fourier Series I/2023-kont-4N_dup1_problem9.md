### **Problem 9** **Numerical integration [10 pts]**

The function $f(x)=\sin(\cos(\pi x))$ is 2-periodic, but most of its Fourier coefficients can only be computed numerically. Using the Gauss–Legendre quadrature described below for $\xi\in[-1,1]$, approximate the coefficient $a_1$.

$$\begin{array}{ccc}i&\xi_i&w_i\\\hline 1&-\sqrt{3/5}&5/9\\ 2&0&8/9\\ 3&\sqrt{3/5}&5/9\end{array}$$

Remark: The Gauß Legendre quadrature formula of a function $g:[-1,1]\to\mathbb{R}$ is given by $Q[g]=\sum_{i=1}^3 w_ig(\xi_i)$.

Kildesett: course=TMA4135 term=kont year=2023 problem=9 points=10 file=tma4130_2023h_exam-19.pdf
