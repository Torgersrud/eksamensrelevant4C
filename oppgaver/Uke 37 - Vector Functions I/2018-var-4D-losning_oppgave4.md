### **Løsning til Oppgave 4**

**a)** Apply the fixed point theorem on $x=g(x)=\frac{1}{2}\cos(x)$.

- $|g'(x)|=\displaystyle\frac{1}{2}|\sin(x)|\le\frac{1}{2}<1$.

- The function $\frac{1}{2}\cos(x)$ is monotonically decreasing on the interval $[0,1]$, thus $g(x)\in(g(1),g(0))=(0.27015,0.5)\subset(0,1)$

so the two conditions of the fixed point theorem are fulfilled, and the fixed exist and is unique.

**b)** Rewrite the equation to the form $f(x)=x-\frac{1}{2}\cos(x)=0$ and Newtons method becomes

$$x_{k+1}=x_k-\frac{x_k-\frac{1}{2}\cos(x_k)}{1+\frac{1}{2}\sin(x_k)}=\frac{x_k\sin(x_k)+\cos(x_k)}{2+\sin(x_k)}.$$

and the first iterations becomes

$$x_0=0.50000,\qquad x_1=0.45063,\qquad x_2=.45018.$$

Kildesett: course=TMA4135 term=var year=2018 problem=4 file=tma4125_final_exam_may_bm.pdf
