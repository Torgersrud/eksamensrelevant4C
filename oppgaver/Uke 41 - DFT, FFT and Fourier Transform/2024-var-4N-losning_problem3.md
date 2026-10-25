### **Solution to Problem 3** **Fourier Series (10 points)**

a) We can directly read off

- $c_{-1}(g)=2$
- $c_5(g)=3$
- $c_{-9}(g)=5$
- $c_{16}(g)=7$

and all other coefficients are zero.

b) We can write $2(\sin(3x))^2=1-\cos(6x)$. Hence the function reads
$$h(x)=1-\cos(6x)+\sin(6x)-2\sin(9x)$$
and can directly read off the real coefficients $a_0=1$, $a_6=-1$, $b_6=1$ and $b_9=-2$ and all others are zero. This means for the complex coefficients, that

- $c_0=a_0=1$
- $c_6=\frac{1}{2}(a_6-ib_6)=-\frac{1}{2}-\frac{1}{2}i$
- $c_{-6}=-\frac{1}{2}+\frac{1}{2}i$,
  either the same way as above or since $h$ is real we just need the conjugate
- $c_9=-c_{-9}=i$ (since $a_9=0$)
- all other coefficients are zero.

c) It can be written as a matrix multiplication, but for computational reasons you shouldn't. By applying a divide and conquer approach, the computational effort can be reduced from $\mathcal{O}(N^2)$ to $\mathcal{O}(N\log N)$

d) The coefficients $c_k(g)$ are related to the discrete coefficients by the Aliasing formula
$$\hat g_k=\sum_{\ell\in\mathbb{Z}}c_{k+\ell N}(g),\quad k=0,\dots,N-1$$
We obtain that both $-9$ and $-1$ are equivalent to $7$ modulo $8$, $16$ is congruent $0$ modulo $8$. So we get

- $\hat g_0=c_{16}(g)=7$
- $\hat g_5=c_{-5}=3$
- $\hat g_7=c_{-1}(g)+c_{-9}(g)=7$

and all other discrete coefficients are zero.

**Grading manual**

a) (2p)

b) (3p)

c) (2p)

d) (3p)

Kildesett: course=TMA4125 term=var year=2024 problem=3 points=10 file=math4n-2024v-en_lf.pdf
