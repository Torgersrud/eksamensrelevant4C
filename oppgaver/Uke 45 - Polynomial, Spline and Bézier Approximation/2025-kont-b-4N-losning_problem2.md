### **Solution to Problem 2** **Interpolation (10 points)**

a) We are given data points $(x_i,y_i)$ for $i=1,2,3,4$:
$$(1,2),\qquad(2,8),\qquad(3,18),\qquad(4,32).$$

The Lagrange interpolant of degree at most 3 is
$$P(x)=\sum_{i=1}^{4}y_i\,\ell_i(x),\qquad\ell_i(x)=\prod_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{4}\frac{x-x_j}{x_i-x_j}.$$

With nodes $x_1=1$, $x_2=2$, $x_3=3$, $x_4=4$, the basis polynomials are
$$\begin{aligned}\ell_1(x)&=\frac{(x-2)(x-3)(x-4)}{(1-2)(1-3)(1-4)}=\frac{(x-2)(x-3)(x-4)}{-6},\\ \ell_2(x)&=\frac{(x-1)(x-3)(x-4)}{(2-1)(2-3)(2-4)}=\frac{(x-1)(x-3)(x-4)}{2},\\ \ell_3(x)&=\frac{(x-1)(x-2)(x-4)}{(3-1)(3-2)(3-4)}=\frac{(x-1)(x-2)(x-4)}{-2},\\ \ell_4(x)&=\frac{(x-1)(x-2)(x-3)}{(4-1)(4-2)(4-3)}=\frac{(x-1)(x-2)(x-3)}{6}.\end{aligned}$$

Thus
$$p(x)=2\ \ell_1(x)+8\ \ell_2(x)+18\ \ell_3(x)+32\ \ell_4(x).$$

Expanding and simplifying gives
$$p(x)=2x^2.$$
(Indeed, the data satisfy $y=2x^2$ at $x=1,2,3,4$.)

b) Estimate at $x=2.5$:
$$f(2.5)\approx P(2.5)=2(2.5)^2=2\cdot6.25=12.5.$$

c) Existence and Uniqueness: For distinct nodes $x_1,\ldots,x_4$, there exists a unique polynomial of degree $\leq3$ that interpolates the data according to the lectures. The uniqueness theorem applies whenever the interpolation nodes are distinct. If two nodes coincide with different function values, no interpolating polynomial exists. (This is enough for two points.)

Note: If $q$ were another such polynomial, then $r=p-q$ would be a nonzero polynomial of degree $\leq3$ with four distinct roots $x_1,\ldots,x_4$, which is impossible. Hence $p$ is unique.

Grading manual: a) 7 points b) 1 point c) 2 points

Kildesett: course=TMA4130 term=kont year=2025 problem=2 points=10 file=exam_math_4n_4d_tma4130_35-15.pdf
