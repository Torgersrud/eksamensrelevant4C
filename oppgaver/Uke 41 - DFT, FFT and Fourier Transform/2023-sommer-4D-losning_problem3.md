### **Solution to Problem 3**

a) We can easily read off the Fourier coefficients $c_k(f) = \begin{cases}1 & \text{if } k = 3,\\ 0 & \text{else}.\end{cases}$

$$(1 \text{ P}.)$$

Since $f$ is bandlimited with $N = 3 < 4 = \frac{8}{2}$ the Fourier transform of length $n = 8$ is exact, i.e. $\hat{\mathbf{f}} = (c_0(f), c_1(f), c_2(f), c_3(f), c_{-4}(f), c_{-3}(f), c_{-2}(f), c_{-1}(f)) = (0, 0, 0, 1, 0, 0, 0, 0)$.

Alternatively the same argument can be done mentioning the Aliasing Lemma.

$$(4 \text{ P}.)$$

b) Similarly to a) we can associate the coefficients to the Fourier coefficients of a bandlimited function $g(x)$ with $c_k(g) = 0$ for $k \neq \pm 1$ and $c_{\pm 1}(g) = \pm \frac{1}{8} \mathrm{i}$, where the factor $\frac{1}{8}$ already anticipates the inverse DFT.

This in turn yields that $g$ is (up to a constant scaling) a sine function. To be precise the vector $\mathbf{g}$ is obtained by sampling $g(x) = -\frac{1}{4} \sin(x)$.

Alternatively one can also compute all 8 terms (consisting of 2 summands each) by hand and argue, without even computing these exactly, that the exponentials cancel out w.r.t. their complex components.

$$(5 \text{ P}.)$$

The exact values of $\mathbf{g}$ are $\mathbf{g} = -\frac{1}{4} \left( 0, \frac{1}{\sqrt{2}}, 1, \frac{1}{\sqrt{2}}, 0, -\frac{1}{\sqrt{2}}, -1, -\frac{1}{\sqrt{2}} \right)$

*If the students are exact with their Fourier transform and use the unitary one, a factor of $\frac{2}{\sqrt{8}} = \frac{1}{\sqrt{2}}$ is also ok. With the physical definition (the 1/8 upfront the DFT instead of its inverse) even the factor 2.*

Kildesett: course=TMA4135 term=sommer year=2023 problem=3 file=tma4125-30-35-matematikk4n-d-2023s_lf_correct.pdf
