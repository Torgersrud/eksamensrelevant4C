### **Solution to Problem 2**

Using Newton interpolation¹, we obtain

$$\begin{array}{r||c@{\qquad}c@{\qquad}c@{\qquad}c@{\qquad}c}
-2&2\\
&&2\\
-1&4&&-3\\
&&-4&&&1\\
0&0&&0&&1/4\\
&&-4&&&2\\
1&-4&&6\\
&&8\\
2&4
\end{array}$$

¹Lagrange interpolation would be fine as well

Thus the interpolation polynomial in Newton form reads

$$\begin{array}{l}\displaystyle p(x)=2+2(x+2)-3(x+2)(x+1)+(x+2)(x+1)x+\frac{1}{4}(x+2)(x+1)x(x-1)\\[10pt]
\displaystyle\qquad=2+2(x+2)-3(x^2+3x+2)+x^3+3x^2+2x+\frac{1}{4}(x^4+2x^3-x^2-2x)\\[10pt]
\displaystyle\qquad=\frac{1}{4}x^4+\frac{3}{2}x^3-\frac{1}{4}x^2-\frac{11}{2}x.\end{array}$$

Kildesett: course=TMA4125 term=kont year=2016 problem=2 file=english.pdf
