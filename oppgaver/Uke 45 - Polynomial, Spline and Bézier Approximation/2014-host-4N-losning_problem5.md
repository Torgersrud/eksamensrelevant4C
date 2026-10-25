### **Solution to Problem 5**

**a)** We use the Lagrange polynomial formula

$$p_4(x)=0\cdot\frac{(x+1)x(x-1)(x-2)}{(-2+1)(-2)(-2-1)(-2-2)}+2\cdot\frac{(x+2)x(x-1)(x-2)}{(-1+2)(-1)(-1-1)(-1-2)}+0\cdot\frac{(x+2)(x-1)(x+1)(x-2)}{(0+2)(0-1)(0+1)(0-2)}$$

$$+1\cdot\frac{(x+2)(x+1)x(x-2)}{(1+2)(1+1)1(1-2)}+0\cdot\frac{(x+2)(x+1)x(x-1)}{(2+2)(2+1)2(2-1)}$$

$$=-\frac{1}{3}(x+2)x(x-1)(x-2)-\frac{1}{6}(x+2)(x+1)x(x-2)=-\frac{1}{2}x^4+\frac{1}{6}x^3+2x^2-\frac{2}{3}x$$

**b)** Using the Error formula of the Simpson method we have the following inequality

$$|E_n|\le h^4\frac{(3-1)}{180}\mathrm{max}_{[1,3]}|f^{(iv)}(x)|<0.001$$

We have that

$$f(x)=x^2\ln(x)\qquad f'(x)=2x\ln(x)+x\qquad f''(x)=2\ln(x)+3\qquad f'''(x)=\frac{2}{x}\qquad\text{and}\qquad f^{(iv)}(x)=-\frac{2}{x^2}$$

so we have that $\mathrm{max}_{[1,3]}|-\frac{2}{x^2}|=2$. Therefore

$$h^4\,\frac{2}{180}2<0.001$$

or

$$h^4<0.045$$

and thus

$$h<0.461.$$

Since in Simpson's rule the length of the interval (in our case: $b-a=2$) has to be an even multiple of the step length $h$, the largest possible step size that works for Simpson's method is $h=1/3$. With this we obtain

$$\int_1^3x^2\ln(x)\,dx\approx\frac{1}{9}\Big[1\ln(1)+4\Big(\frac{4}{3}\Big)^2\ln\Big(\frac{4}{3}\Big)+2\Big(\frac{5}{3}\Big)^2\ln\Big(\frac{5}{3}\Big)+4\Big(\frac{6}{3}\Big)^2\ln\Big(\frac{6}{3}\Big)+2\Big(\frac{7}{3}\Big)^2\ln\Big(\frac{7}{3}\Big)$$

$$+4\Big(\frac{8}{3}\Big)^2\ln\Big(\frac{8}{3}\Big)+\Big(\frac{9}{3}\Big)^2\ln\Big(\frac{9}{3}\Big)\Big]\approx 6.9985.$$

Kildesett: course=TMA4130 term=host year=2014 problem=5 file=eksam2014.pdf
