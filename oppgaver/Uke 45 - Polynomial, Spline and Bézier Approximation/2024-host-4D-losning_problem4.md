### **Solution to Problem 4** **Interpolation [10 pts]**

a) We calculate the cardinal functions:

$$\begin{aligned}\ell_0&=\frac{(x-x_1)(x-x_2)}{(x_0-x_1)(x_0-x_2)}=\frac{(x-2)(x-4)}{(-2)(-4)}=\frac{x^2-6x+8}{8}\\
\ell_1&=\frac{(x-x_0)(x-x_2)}{(x_1-x_0)(x_1-x_2)}=\frac{x(x-4)}{2\cdot 2}=\frac{x^2-4x}{4}\\
\ell_2&=\frac{(x-x_0)(x-x_1)}{(x_2-x_0)(x_2-x_1)}=\frac{x(x-2)}{4\cdot 2}=\frac{x^2-2x+8}{8}\end{aligned}$$

Note that $\ell_1$ does not need to be computed, as $y_1=0$. We get

$$p_2(x)=\underbrace{y_0}_{=1}\cdot\ell_0+\underbrace{y_1}_{=0}\cdot\ell_1+\underbrace{y_2}_{=1}\cdot\ell_2=\frac{x^2-6x+8}{8}+\frac{x^2-2x+8}{8}=\frac{1}{4}x^2-x+1.$$

b) We have

$$\begin{aligned}f[x_0,x_1]&=\frac{f(x_1)-f(x_0)}{x_1-x_0}=-\frac{1}{2}\\
f[x_1,x_2]&=\frac{f(x_2)-f(x_1)}{x_2-x_1}=\frac{1}{2}\\
f[x_0,x_1,x_2]&=\frac{f[x_1,x_2]-f[x_0,x_1]}{x_2-x_0}=\frac{1}{4}.\end{aligned}$$

The table reads

$$\begin{array}{c|ccc}x_i&y_i&&\\\hline 0&1&&\\ 2&0&-\frac{1}{2}&\\ 4&1&\frac{1}{2}&\frac{1}{4}\end{array}$$

The interpolating polynomial becomes

$$p_2(x)=f[x_0,x_1,x_2]\cdot(x-x_0)\cdot(x-x_1)+f[x_0,x_1]\cdot(x-x_0)+f[x_0]=\frac{1}{4}x(x-2)-\frac{1}{2}x+1.$$

c) We have

$$p_2(x)=\frac{1}{4}x(x-2)-\frac{1}{2}x+1=\frac{1}{4}(x^2-2x)-\frac{1}{2}x+1=\frac{1}{4}x^2-x+1.$$

d) An approximation to $f(1)$ is

$$p(1)=\frac{1}{4}-\frac{1}{2}-\frac{1}{2}+1=\frac{1}{4}.$$

**Grading manual**

a) (4p)

b) (4p)

c) (1p)

d) (1p)

Kildesett: course=TMA4135 term=host year=2024 problem=4 points=10 file=exam_math_4n_4d_tma4130_35-8.pdf
