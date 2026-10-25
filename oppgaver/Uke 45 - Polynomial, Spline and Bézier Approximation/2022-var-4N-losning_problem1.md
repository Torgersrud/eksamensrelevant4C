### **Solution to Problem 1** (Polynomial interpolation, 8 points)

A relatively short solution is the following: Since both $x_1$ and $x_5$ have the value $\frac{1}{2}$ we can write (1 P.)

$$p(x)=q(x)+\frac{1}{2}\quad\text{or}\ q(x)=p(x)-\frac{1}{2}$$

such that $q(-2)=q(2)=0$. This means we can write (1 P.)

$$q(x)=(x-2)(x+2)r(x)=(x^2-4)r(x)$$

Plugging the remaining points into this, we obtain (3 P.)

$$\begin{aligned}5=p(-1)=q(-1)+\frac{1}{2}=\big((-1)^2-4\big)r(-1)+\frac{1}{2}=-3r(-1)+\frac{1}{2}\\
\Rightarrow\ -3r(-1)=\frac{9}{2}\Rightarrow r(-1)=-\frac{3}{2}\\
\frac{5}{2}=p(0)=q(0)+\frac{1}{2}=\big(0^2-4\big)r(-1)-\frac{1}{2}=-4r(0)+\frac{1}{2}\\
\Rightarrow\ -4r(0)=2\Rightarrow r(0)=-\frac{1}{2}\\
-1=p(1)=q(1)+\frac{1}{2}=\big(1^2-4\big)r(1)+\frac{1}{2}=-3r(1)+\frac{1}{2}\\
\Rightarrow\ -3r(1)=-\frac{3}{2}\Rightarrow r(1)=\frac{1}{2}\end{aligned}$$

And we can easily see that $r(x)=x-\frac{1}{2}$. Hence we obtain $q(x)=(x^2-4)(x-\frac{1}{2})$ and therefore

$$p(x)=q(x)+\frac{1}{2}=x^3-\frac{1}{2}x^2-4x+\frac{5}{2}$$ (3 P.)

*Newton Scheme.*

For the newton Scheme we obtain the polynomials (3 P.)

$w_0(x)=1$

$w_1(x)=(x+2)$

$w_2(x)=(x+2)(x+1)=x^2+3x+2$

$w_3(x)=(x+2)(x+1)x=x^3+3x^2+2x$

$w_4(x)=(x+2)(x+1)x(x-1)=x^4+3x^3+2x^2-x^3-3x^2-2x=x^4+2x^3-x^2-2x$

and the Newton scheme looks as follows. \underline{Note since we have equidistant nodes, the denominator is just always equal to the number of nodes involved} (4 P.)

| $i$ | $x_i$ | $y_i=f[x_i]$ | $f[x_i,x_{i+1}]$ | $f[x_i,x_{i+1},x_{i+2}]$ | $f[x_i,x_{i+1},x_{i+2},x_{i+3}]$ | $f[x_1,x_2,x_3,x_4,x_5]$ |
|---|---|---|---|---|---|---|
| $1$ | $-2$ | $\frac{1}{2}$ | | | | |
| | | | $\dfrac{5-\frac{1}{2}}{-1-(-2)}=\dfrac{9}{2}$ | | | |
| $2$ | $-1$ | $5$ | | $\dfrac{-\frac{5}{2}-\frac{9}{2}}{2}=-\dfrac{7}{2}$ | | |
| | | | $\dfrac{\frac{5}{2}-5}{0-(-1)}=-\dfrac{5}{2}$ | | $\dfrac{-\frac{1}{2}-\left(-\frac{7}{2}\right)}{3}=1$ | |
| $3$ | $0$ | $\frac{5}{2}$ | | $\dfrac{-\frac{7}{2}-\left(-\frac{5}{2}\right)}{2}=-\dfrac{1}{2}$ | | $\dfrac{1-1}{4}=0$ |
| | | | $\dfrac{-1-\frac{5}{2}}{1-0}=-\dfrac{7}{2}$ | | $\dfrac{\frac{5}{2}-\left(-\frac{1}{2}\right)}{3}=1$ | |
| $4$ | $1$ | $-1$ | | $\dfrac{\frac{3}{2}-\left(-\frac{7}{2}\right)}{2}=\dfrac{5}{2}$ | | |
| | | | $\dfrac{\frac{1}{2}-(-1)}{2-1}=\dfrac{3}{2}$ | | | |
| $5$ | $2$ | $\frac{1}{2}$ | | | | |

Hence we obtain (1 P.)

$$\begin{aligned}p(x)&=\frac{1}{2}w_0+\frac{9}{2}w_1(x)-\frac{7}{2}w_2(x)+1w_3(x)-0w_4(x)\\
&=\frac{1}{2}+\frac{9}{2}(x+2)-\frac{7}{2}(x^2+3x+2)+(x^3+3x^2+2x)\\
&=\frac{1}{2}+\frac{9}{2}x+9-\frac{7}{2}x^2-\frac{21}{2}x-7+x^3+3x^2+2x\\
&=x^3-\frac{1}{2}x^2-4x+\frac{5}{2}\,.\end{aligned}$$

Kildesett: course=TMA4125 term=var year=2022 problem=1 points=8 file=TMA4125-Matematikk-4N-2022v_lf.pdf
