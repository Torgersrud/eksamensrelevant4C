### **Solution to Problem 6** (Fourier Series, 12 points)

a) We can rewrite $2\cos(4x)=e^{4ix}+e^{-4ix}$. Then the whole function is already in the form of a (complex) Fourier series with only a few summands being nonzero, namely with the coefficients (2 P.)

- $c_{\pm 4}(f)=1$
- $c_{6}(f)=3$
- $c_{9}(f)=8$
- $c_{-7}(f)=5$

and all other coefficients are zero. (1 P.)

b) We can write $2\left(\cos(2x)\right)^{2}=\cos(4x)+1$. (1 P.)

Hence, the function reads

$$g(x)=1+\cos(4x)+\sin(5x)+2\cos(5x)+\sin(9x),$$

and one can directly read off the real coefficients $a_0=1$, $a_4=1$, $a_5=2$, $b_5=1$, $b_9=1$, and all others are zero. (3 P.)

c) In order to employ the convolution theorem, we first need both previous functions' $c_k$ coefficients. We have that (2 P.)

- $c_0(g)=a_0=1$
- $c_{\pm 4}(g)=\frac{1}{2}(a_4\mp ib_4)=\frac{1}{2}$
- $c_5(g)=\frac{1}{2}(a_5-ib_5)=1-\frac{i}{2}$,
- $c_{-5}(g)=\frac{1}{2}(a_5+ib_5)=1+\frac{i}{2}$,
- $c_9(g)=-c_{-9}=-\frac{i}{2}$ (since $a_9=0$)
- all other coefficients are zero.

The convolution theorem states that for $h=f*g$ the Fourier coefficients are given by $c_k(h)=2\pi c_k(f)c_k(g)$. Here, only coefficients that are nonzero for *both* functions "survive". We obtain (2 P.)

- $c_{\pm 4}(h)=2\pi\cdot 1\cdot\frac{1}{2}=\pi$
- $c_9(h)=-2\pi\cdot 8\cdot\frac{i}{2}=-8\pi i$
- and all others are zero.

Hence, using the same idea of combining $c_{\pm 4}(h)$ into a cosine as before, the function $h$ reads (1 P.)

$$h(x)=2\pi\cos(4x)-8\pi ie^{9ix}$$

Kildesett: course=TMA4432 term=test year=2026 problem=6 points=12 file=test-exam-math4c_web.pdf
