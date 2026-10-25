### **Solution to Problem 3** **Numerics for Nonlinear Equations [10 pts]**

a) This is the implicit Euler method.

b) Newton's method for this equation will be

$$x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}=x_k+\frac{\cos x_k-2x_k}{\sin x_k+2}$$

Therefore, we have

$$i)\;\;x_1=0+\frac{\cos 0-2\times 0}{\sin 0+2}=0.5$$

$$ii)\;\;x_2=0.5+\frac{\cos(0.5)-2\times 0.5}{\sin(0.5)+2}\approx 0.4506$$

$$iii)\;\;x_3\approx 0.4506+\frac{\cos(0.4506)-2\times 0.4506}{\sin(0.4506)+2}\approx 0.4502$$

Since $|x_3-x_2|\approx 0.4\times 10^{-3}$, we need not iterate any further.

**Grading manual** (2p) for **a)**, (8p) for **b)**. Out of those 8p, give

- 5p for writing the correct expression for the iterations (with a generic $x_k$)
- 1p for each correct iteration.

Kildesett: course=TMA4135 term=host year=2023 problem=3 points=10 file=tma4130_2023h_exam.pdf
