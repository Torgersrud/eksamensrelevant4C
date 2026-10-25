### **Solution to Problem 10**

(a) Since the left-hand side of the equation is always positive, we cannot have any solution for $x$ non-positive. Consider the function

$$f\colon[0,\infty)\to\mathbb{R},\quad f(x)=e^{-x^{2}}-x$$

We have

$$f'(x)=-2xe^{-x^{2}}-1=-\Big(2xe^{-x^{2}}+1\Big)<0$$

which shows that $f$ is strictly decreasing. Since $f(0)=1>0$ and $f(1)=e^{-1}-1<0$ the function $f$ has a unique zero on the interval $[0,1]$ and no zeros outside this interval.

(b) [Method p. 2 in notes] Let $a_0=0$ and $b_0=1$ and $c_0=(a_0+b_0)/2=0.5$. Since $f(c_0)=e^{-0.5^2}-0.5=0.28>0$, we let $a_1=c_0=0.28$ and $b_1=b_0=1$. We find then $c_1=(a_1+b_1)/2=0.64$.

(c) The Newton iteration equals

$$x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)},\quad k=0,1,2,\ldots.$$

We have

$$f'(x)=-2xe^{-x^{2}}-1=-\Big(2xe^{-x^{2}}+1\Big),$$

and thus

$$x_0=0.5,\quad x_1=x_0-\frac{f(x_0)}{f'(x_0)}=0.5-\frac{f(0.5)}{f'(0.5)}\approx 0.656735.$$

Kildesett: course=TMA4135 term=kont year=2020 problem=10 points=12 file=tma4130_kont.pdf
