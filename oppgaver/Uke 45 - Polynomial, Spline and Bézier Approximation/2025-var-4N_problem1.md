### **Problem 1** **Interpolation (10 points)**

The following interpolation points $(x_i,y_i)$, $i=0,\dots,3$ are provided

$$\begin{array}{|c|c|c|c|c|}\hline i&0&1&2&3\\\hline x_i&0&1&2&3\\\hline y_i&3&0&-3&0\\\hline\end{array}$$

We aim to investigate the interpolation polynomial $p(x)$ with $p(x_i)=y_i$, $i=0,\dots,3$.

a) Compute all Lagrange polynomials necessary for the interpolation.

b) What is the degree $k$ of the interpolation polynomial interpolating the data at most?

c) The interpolation polynomial has the general form
$$p(x)=\sum_{i=0}^{k}a_i x^i,$$
where $k$ is the answer from task b). Compute the coefficient with this highest index $a_k$.

d) We get the additional point to interpolate $(x_4,y_4)=(4,15)$. In order to compute the interpolation polynomial $\tilde p$ that also includes this point, what do we have to update if we want to reuse the results from before? (you do not have to compute the update nor $\tilde p(x)$)

Kildesett: course=TMA4125 term=var year=2025 problem=1 points=10 file=math4n-2025v-en-lf.pdf
