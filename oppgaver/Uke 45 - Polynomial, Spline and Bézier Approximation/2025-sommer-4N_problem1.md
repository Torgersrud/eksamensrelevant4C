### **Problem 1** **Interpolation (10 points)**

The following interpolation points $(x_i,y_i)$, $i=0,1,2$ are provided

$$\begin{array}{|c|c|c|c|}\hline i&0&1&2\\\hline x_i&0&1&2\\\hline y_i&2&0&3\\\hline\end{array}$$

We aim to investigate the interpolation polynomial $p(x)$ with $p(x_i)=y_i$, $i=0,1,2$.

a) Compute all Lagrange polynomials necessary for the interpolation as well as the resulting interpolation polynomial $p(x)$.

b) We additionally get the point $(x_3,y_3)=(4,0)$. What do we have to update in our computations from Item a)?
Perform the necessary updates and compute the new interpolation polynomial $q(x)$ with $q(x_i)=y_i$, $i=0,1,2,3$.

c) If we (hypothetically) get yet another point $(x_4,y_4)=(\frac{1}{2},0)$ to update $q(x)$ yet again. Can we spare computations even though we would use Lagrange interpolation?
How does this affect the degree of the resulting polynomial?

Kildesett: course=TMA4125 term=sommer year=2025 problem=1 points=10 file=math4n-2025s-en-lf.pdf
