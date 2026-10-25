### **Solution to Problem 10**

a) We start with choosing $M\in\mathbb{N}$ and setting $\Delta x=1/M$ and $x_i=i\Delta x$ for $i=0,\ldots,M$. Using central differences for the approximation of the derivatives on the right hand side, we then obtain at the interior grid points the equations

$$\frac{\partial u}{\partial t}(x_i,t)=\frac{u(x_i-\Delta x,t)-2u(x_i,t)+u(x_i+\Delta x,t)}{\Delta x^2}$$

$$+x_i\frac{u(x_i+\Delta x,t)-u(x_i-\Delta x,t)}{2\Delta x}+\mathcal{O}(\Delta x^2).$$

Approximating $U_i(t)\approx u(x_i,t)$ and ignoring the error term yields

$$U_i'(t)=\frac{U_{i-1}(t)-2U_i(t)+U_{i+1}(t)}{\Delta x^2}+x_i\frac{U_{i+1}(t)-U_{i-1}(t)}{2\Delta x}$$

for $i=1,\ldots,M-1$. In addition, we have the initial condition

$$U_i(0)=x_i^2\qquad\text{for }i=1,\ldots,M-1,$$

and the boundary values

$$U_0(t)=t\qquad\text{and}\qquad U_M(t)=1.$$

b) We now choose a time step $\Delta t$ and approximate $U_i^n\approx u(x_i,t_n)$ with $t_n=n\Delta t$. Then the trapezoidal rule (or the Crank-Nicolson method) reads as

$$U_i^{n+1}=U_i^n+\frac{\Delta t}{2}\Big(\frac{U_{i-1}^n-2U_i^n+U_{i+1}^n}{\Delta x^2}+x_i\frac{U_{i+1}^n-U_{i-1}^n}{2\Delta x}$$

$$+\frac{U_{i-1}^{n+1}-2U_i^{n+1}+U_{i+1}^{n+1}}{\Delta x^2}+x_i\frac{U_{i+1}^{n+1}-U_{i-1}^{n+1}}{2\Delta x}\Big)$$

for $i=1,\ldots,M-1$ and $n\geq 0$. In addition, we have

$$U_0^n=t_n=n\Delta t\qquad\text{and}\qquad U_M^n=1,$$

and

$$U_i^0=x_i^2\qquad\text{for }i=1,\ldots,M-1.$$

For the specific case of $M=2$ and $\Delta x=1/2$, the only unknown is $U_1^{n+1}$. If we insert the boundary values $U_0^n=t_n$ and $U_2^n=1$, as well as $x_1=1/2$, we end up with the equation

$$U_1^{n+1}=U_1^n+\frac{\Delta t}{2}\Big(4(t_n-2U_1^n+1)+\frac{1}{2}(1-t_n)+4(t_{n+1}-2U_1^{n+1}+1)+\frac{1}{2}(1-t_{n+1})\Big).$$

This can be solved explicitly for $U_1^{n+1}$ and we obtain

$$U_1^{n+1}=\frac{1}{1+4\Delta t}\Big((1-4\Delta t)U_1^n+\frac{9\Delta t}{2}+\frac{7\Delta t}{4}(t_n+t_{n+1})\Big)$$

For the specific case $\Delta t=1/2$ and $t_n=n/2$, this results in

$$U_1^{n+1}=\frac{1}{3}\Big(-U_1^n+\frac{9}{4}+\frac{7}{8}\Big(n+\frac{1}{2}\Big)\Big)=\frac{1}{3}\Big(-U_1^n+\frac{43}{16}+\frac{7n}{8}\Big).$$

With the initial value $U_1^0=1/4$, we thus obtain that

$$U_1^1=\frac{1}{3}\Big(-\frac{1}{4}+\frac{43}{16}\Big)=\frac{13}{16}$$

and

$$U_1^2=\frac{1}{3}\Big(-\frac{13}{16}+\frac{43}{16}+\frac{7}{8}\Big)=\frac{7}{8}.$$

Kildesett: course=TMA4135 term=host year=2020 problem=10 points=12 file=completeexam_nosolutions.pdf
