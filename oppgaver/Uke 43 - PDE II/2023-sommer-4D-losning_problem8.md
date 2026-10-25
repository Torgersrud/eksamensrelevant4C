### **Solution to Problem 8**

Inserting $t = 0$ into the general solution, we obtain that

$$u(x, 0) = \sum_{n=1}^\infty A_n \sin(nx).$$

Now the initial condition states that this should be equal to

$$u(x, 0) = \sin(x).$$

By comparing the coefficients in front of the sine functions, we see that

$$A_1 = 1, \quad \text{and } A_n = 0 \text{ else}.$$

Next we differentiate the general solution with respect to $t$, which gives

$$\frac{\partial u}{\partial t}(x, t) = \sum_{n=1}^\infty \sin(nx) \left( -A_n \sqrt{7 + n^2} \sin\left( t \sqrt{7 + n^2} \right) + B_n \sqrt{7 + n^2} \cos\left( t \sqrt{7 + n^2} \right) \right)$$

In particular, we obtain for $t = 0$ that

$$\frac{\partial u}{\partial t}(x, 0) = \sum_{n=1}^\infty B_n \sqrt{7 + n^2} \sin(nx).$$

The second initial condition states that this should be equal to

$$\frac{\partial u}{\partial t}(x, 0) = 2 \sin(3x).$$

Again, we have to compare the coefficients in front of the sine functions. For $n = 3$ we obtain the equation

$$B_3 \sqrt{7 + 3^2} = 2,$$

which simplifies to

$$B_3 = \frac{1}{2},$$

and all other coefficients are equal to 0.

Thus the solution with these initial conditions reads

$$u(x, t) = \sin(x) \cos(\sqrt{8} t) + \frac{1}{2} \sin(3x) \sin(4t).$$

Kildesett: course=TMA4135 term=sommer year=2023 problem=8 file=tma4125-30-35-matematikk4n-d-2023s_lf_correct.pdf
