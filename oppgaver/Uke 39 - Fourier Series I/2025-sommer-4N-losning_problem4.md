### **Solution to Problem 4** **Fourier Series (12 points)**

a) We can rewrite $9\sin(3x)=\frac{9i}{2}(e^{3ix}-e^{-3ix})$. Then the whole function is already in the form of a (complex) Fourier series with only a few summands being non-zero, namely with the coefficients

- $c_{\pm 3}(f)=\pm\frac{9}{2}i$
- $c_{-5}(f)=3$
- $c_7(f)=2$
- $c_{-9}(f)=1$

and all other coefficients are zero.

b) The Fourier coefficients of the Dirichlet kernel $D_N$ are given by
$$c_k(D_N)=\begin{cases}1&\text{if }k\in\{-N,-N+1,\dots,N-1,N\}\\ 0&\text{otherwise.}\end{cases}$$

c) The convolution theorem states that for $g_N=f*D_N$ the Fourier coefficients are given by
$$c_k(g_N)=2\pi c_k(f)c_k(D_N)=\begin{cases}2\pi c_k(f)&\text{if }k=-N,-N+1,\dots,N-1,N\\ 0&\text{otherwise.}\end{cases}$$
We hence get that
$$g_5(x)=2\pi\bigl(9\sin(3x)+3e^{-5ix}\bigr)$$
Since all Fourier coefficients of $f$ with an index $|k|>5$ are zero get "masked" out. For $g_{10}$ we get simply $g_{10}(x)=2\pi f(x)$.

As an interpretation, the convolution with the Dirichlet kernel $D_N$ acts as a low-pass filter, i.e. it removes all Fourier coefficients of $f$ with an index $|k|>N$.

d) The modified Dirichlet kernel $\tilde D_N$ is preferred over the original Dirichlet kernel $D_N$ because

- it is normalized, i.e. $\int_{-\pi}^{\pi}\tilde D_N(x)dx=1$,
- when using it in convolution tasks like Item c), it does not scale the result by $2\pi$.

**Grading manual**

a) (3p)

b) (3p)

c) (4p)

d) (2p)

Kildesett: course=TMA4125 term=sommer year=2025 problem=4 points=12 file=math4n-2025s-en-lf.pdf
