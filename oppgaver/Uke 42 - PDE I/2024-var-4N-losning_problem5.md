### **Solution to Problem 5** **D'Alembert (6 points)**

We use d'Alembert's method with $c=3$, we have that $f(x)=\frac{2}{1+x^2}$ and $g(x)=\frac{12x}{(1+x^2)^2}$ and obtain that
$$\begin{aligned}u(x,t)&=\frac{1}{2}\bigl(f(x+ct)+f(x-ct)\bigr)+\frac{1}{2c}\int_{x-ct}^{x+ct}g(s)\,\mathrm{d}s\\
&=\frac{1}{1+(x+3t)^2}+\frac{1}{1+(x-3t)^2}+\frac{1}{6}\int_{x-3t}^{x+3t}\frac{12s}{(1+s^2)^2}\,ds\end{aligned}$$
We cancel the fraction upfront and see that the integral is of the form $\int\frac{h'(s)}{(h(s))^2}\,\mathrm{d}s$ with $h(s)=1+s^2$ and hence $h'(s)=2s$. Hence the antiderivative is $-\frac{1}{h}$
$$\begin{aligned}&=\frac{1}{1+(x+3t)^2}+\frac{1}{1+(x-3t)^2}-\frac{1}{1+s^2}\bigg|_{x-3t}^{x+3t}\\
&=\frac{1}{1+(x+3t)^2}+\frac{1}{1+(x-3t)^2}-\frac{1}{1+(x+3t)^2}+\frac{1}{1+(x-3t)^2}\end{aligned}$$
This then simplifies to the solution
$$=\frac{2}{1+(x-3t)^2}.$$

**Grading manual** (2p) for d'Alembert's formula with $c=3$, (2p) for computing the integral, (2p) for the simplification to the solution.

Kildesett: course=TMA4125 term=var year=2024 problem=5 points=6 file=math4n-2024v-en_lf.pdf
