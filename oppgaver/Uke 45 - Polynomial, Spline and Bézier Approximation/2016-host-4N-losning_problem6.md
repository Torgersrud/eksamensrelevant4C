### **Solution to Problem 6**

Using Newton interpolation¹, we obtain

$$\begin{array}{r||c@{\qquad}c@{\qquad}c@{\qquad}c@{\qquad}c}
-2&1\\
&&1\\
-1&2&&1\\
&&3&&-1\\
0&5&&-2&&1/3\\
&&-1&&1/3\\
1&4&&-1\\
&&-3\\
2&1
\end{array}$$

¹Lagrange interpolation would be fine as well

Then the polynomial is of the form

$$p(x)=\frac{1}{3}(x-1)x(x+1)(x+2)-x(x+1)(x+2)+(x+1)(x+2)+(x+2)+1$$

Then the estimate of $f(3)$ can be done with $p(3)=6$.

Kildesett: course=TMA4130 term=host year=2016 problem=6 file=n16h.pdf
