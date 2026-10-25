### **Solution to Problem 4** **Interpolation [10 pts]**

We have $p'(x)=3ax^2+2bx+c$. The system of equations is
$$\begin{gathered}a\cdot0^3+b\cdot0^2+c\cdot0+d=d=1\\a\cdot1^3+b\cdot1^2+c\cdot1+d=a+b+c+d=2\\a\cdot2^3+b\cdot2^2+c\cdot2+d=8a+4b+2c+d=0\\3a\cdot1^2+2b\cdot1+c=3a+2b+c=3.\end{gathered}$$

From the first equation, we get directly that $d=1$. Therefore:
$$\begin{gathered}a+b+c=1\implies a=1-b-c\\8a+4b+2c=-1\implies 8(1-b-c)+4b+2c=8-4b-6c=-1\implies b=\frac{9}{4}-\frac{3}{2}c\\3a+2b+c=3.\end{gathered}$$

Setting in the formulations of $a$ and $b$ in the third equation gives
$$3(1-b-c)+2\left(\frac{9}{4}-\frac{3}{2}c\right)+c=3-3b-3c+\frac{9}{2}-3c+c=\frac{15}{2}-3b-5c=\frac{15}{2}-3\left(\frac{9}{4}-\frac{3}{2}c\right)-5c$$
$$=\frac{15}{2}-\frac{27}{4}+\frac{9}{2}c-5c=\frac{3}{4}-\frac{1}{2}c=3\implies c=-\frac{9}{2}.$$

Then
$$b=\frac{9}{4}-\frac{3}{2}c=b=\frac{9}{4}-\frac{3}{2}\cdot\left(-\frac{9}{2}\right)=\frac{36}{4}=9.$$

Finally,
$$a=1-b-c=1-9+\frac{9}{2}=-\frac{7}{2}.$$

Thus, the polynomial is given as
$$p(x)=-\frac{7}{2}x^3+9x^2-\frac{9}{2}x+1.$$

**Grading manual** 4 points for the system of equations, 1 point for the computation, 4 points for each unknown, 1 point for the polynomial.

Kildesett: course=TMA4130 term=kont year=2025 problem=4 points=10 file=exam_math_4n_4d_tma4130_35-5.pdf
