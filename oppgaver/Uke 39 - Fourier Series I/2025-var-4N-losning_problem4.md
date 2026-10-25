### **Solution to Problem 4** **Fourier Series (12 points)**

a) We can rewrite $2\cos(4x)=e^{4ix}+e^{-4ix}$. Then the whole function is already in the form of a (complex) Fourier series with only a few summands being nonzero, namely with the coefficients

- $c_{\pm 4}(f)=1$
- $c_6(f)=3$
- $c_9(f)=8$
- $c_{-7}(f)=5$

and all other coefficients are zero.

b) We can write $2(\cos(2x))^2=\cos(4x)+1$. Hence, the function reads

$$h(x)=1+\cos(4x)+\sin(5x)+2\cos(5x)+\sin(9x),$$

and one can directly read off the real coefficients $a_0=1$, $a_4=1$, $b_5=1$ $a_5=2$, $b_9=1$, and all others are zero.

c) In order to employ the convolution theorem, we first need both previous functions' $c_k$ coefficients. We have that

- $c_0(g)=a_0=1$
- $c_{\pm 4}(g)=\frac{1}{2}(a_4\pm\mathrm{i}b_4)=\frac{1}{2}$
- $c_5(g)=\frac{1}{2}(a_5+\mathrm{i}b_5)=1+\frac{\mathrm{i}}{2}$,
- $c_{-5}(g)=\frac{1}{2}(a_5-\mathrm{i}b_5)=1-\frac{\mathrm{i}}{2}$,
- $c_9(g)=-c_{-9}=-\frac{\mathrm{i}}{2}$ (since $a_9=0$)
- all other coefficients are zero.

The convolution theorem states that for $h=f*g$ the Fourier coefficients are given by $c_k(h)=2\pi c_k(f)c_k(g)$. Here, we get only nonzero coefficients of *both* functions "survive". We obtain

- $c_{\pm 4}(h)=2\pi\frac{1}{2}\cdot 2=2\pi$
- $c_9(h)=-2\pi\cdot 8\cdot\frac{\mathrm{i}}{2}=-8\pi\mathrm{i}$
- and all others are zero.

Hence, using the same idea of combining $c_{\pm 4}(h)$ into a cosine as before, the function $h$ reads

$$h(x)=4\pi\cos(4x)-8\pi\mathrm{i}e^{9\mathrm{i}x}$$

**Grading manual**

a) (3p)

b) (4p)

c) (5p)

Kildesett: course=TMA4125 term=var year=2025 problem=4 points=12 file=math4n-2025v-en-lf.pdf
