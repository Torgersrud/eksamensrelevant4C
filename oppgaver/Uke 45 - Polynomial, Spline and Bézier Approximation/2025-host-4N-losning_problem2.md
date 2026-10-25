### **Solution to Problem 2** **Interpolation (10 points)**

a) **Using Lagrange:** We are given data points $(x_i,f_i)$ for $i=0,1,2,3$:

$$(0,0),\quad(1,2),\quad(2,6),\quad(3,12).$$

The Lagrange interpolant of degree at most 3 is

$$p(x)=\sum_{i=0}^{3}f_i\,\ell_i(x),\qquad\ell_i(x)=\prod_{\substack{j=0\\ j\neq i}}^{3}\frac{x-x_j}{x_i-x_j}.$$

With nodes $x_0=0,\ x_1=1,\ x_2=2,\ x_3=3$, the basis polynomials are

$$\ell_0(x)=\frac{(x-1)(x-2)(x-3)}{(0-1)(0-2)(0-3)}=-\frac{1}{6}(x-1)(x-2)(x-3),$$

$$\ell_1(x)=\frac{x(x-2)(x-3)}{(1-0)(1-2)(1-3)}=\frac{1}{2}x(x-2)(x-3),$$

$$\ell_2(x)=\frac{x(x-1)(x-3)}{(2-0)(2-1)(2-3)}=-\frac{1}{2}x(x-1)(x-3),$$

$$\ell_3(x)=\frac{x(x-1)(x-2)}{(3-0)(3-1)(3-2)}=\frac{1}{6}x(x-1)(x-2).$$

Thus

$$p(x)=0\cdot\ell_0(x)+2\,\ell_1(x)+6\,\ell_2(x)+12\,\ell_3(x).$$

Expanding and simplifying gives

$$\boxed{\,p(x)=x^2+x\,}$$

**Using Newton:**

We use Newton's divided difference method.

Since four interpolation points are given, we are \underline{a priori} looking for an interpolating polynomial of degree at most 3.

Zeroth-order divided differences:

$$f[x_0]=0,\quad f[x_1]=2,\quad f[x_2]=6,\quad f[x_3]=12.$$

First-order divided differences:

$$f[x_0,x_1]=\frac{2-0}{1-0}=2,\quad f[x_1,x_2]=\frac{6-2}{2-1}=4,\quad f[x_2,x_3]=\frac{12-6}{3-2}=6.$$

Second-order divided differences:

$$f[x_0,x_1,x_2]=\frac{4-2}{2-0}=1,\quad f[x_1,x_2,x_3]=\frac{6-4}{3-1}=1.$$

Third-order divided difference:

$$f[x_0,x_1,x_2,x_3]=\frac{1-1}{3-0}=0.$$

Since the third-order divided difference is zero, the interpolating polynomial has degree at most 2.

The Newton form of the interpolating polynomial is therefore

$$\begin{aligned}p_3(x)={}&f[x_0]+f[x_0,x_1](x-x_0)+f[x_0,x_1,x_2](x-x_0)(x-x_1)\\ &+f[x_0,x_1,x_2,x_3](x-x_0)(x-x_1)(x-x_2).\end{aligned}$$

Substitute the computed values:

$$p(x)=0+2(x-0)+1(x-0)(x-1).$$

Simplify:

$$p(x)=2x+x(x-1)=2x+x^2-x=x^2+x.$$

Thus, the interpolating polynomial is:

$$\boxed{\,p(x)=x^2+x\,}$$

**Using the direct approach:**

Let us consider a quadratic polynomial

$$p(x)=ax^2+bx+c,$$

and determine $a,b,c$ directly from the pointwise conditions.

From $p(0)=0$ we get

$$c=0.$$

From $p(1)=2$ we get

$$a+b+c=2\implies a+b=2.$$

From $p(2)=6$ we get

$$4a+2b+c=6\implies 4a+2b=6.$$

Using $c=0$, solve the linear system

$$\begin{aligned}a+b&=2,\\ 4a+2b&=6.\end{aligned}$$

Multiply the first equation by 2 and subtract from the second:

$$4a+2b-2(a+b)=6-4\implies 2a=2\implies a=1.$$

Then $b=2-a=1$. Thus

$$\boxed{\,p(x)=x^2+x\,}$$

b) **Estimate at $x=1.5$:**

$$f(1.5)\approx p(1.5)=(1.5)^2+1.5=2.25+1.5=3.75.$$

c) **Existence and Uniqueness:** For distinct nodes $x_0,\dots,x_3$, there exists a unique polynomial of degree $\leq 3$ that interpolates the data.

If $q$ were another such polynomial, then $r=p-q$ would be a nonzero polynomial of degree $\leq 3$ with four distinct roots $x_0,\dots,x_3$, which is impossible. Hence $p$ is unique.

Grading manual: a) 7 points b) 1 point c) 2 points

Remark for c): Award **1 point** if the student provides any of the following valid arguments:

- References to the \underline{Lagrange} interpolation formula as a constructive proof of existence. (e.g. "The Lagrange form already gives a polynomial that interpolates the data.")
- References to the standard theorem from the lecture: (e.g. "For $n+1$ distinct nodes, there exists a polynomial of degree at most $n$ that interpolates the data.")
- Mentions that the nodes $x_0,\dots,x_3$ are distinct.

**No point** if:

- "Existence" is merely stated without any explanation.
- The argument is incorrect or irrelevant.

Award **1 point** for a correct explanation of the standard uniqueness argument. For example:

- "If $p$ and $q$ both interpolate the data, then $r=p-q$ is a polynomial of degree at most 3 with four distinct zeros. This is impossible unless $r\equiv 0$, so $p=q$."

**No point** if:

- "Uniqueness" is only stated without justification.
- The reasoning is logically incorrect.

Kildesett: course=TMA4130 term=host year=2025 problem=2 points=10 file=exam_math_4n_4d_tma4130_35-21.pdf
