### **Solution to Problem 5** **Discrete Fourier Transform (10 points)**

a) We can directly read off $c_0(f)=3$, $c_{\pm2}(f)=1$ and all other coefficients are zero.

b) From the aliasing Lemma we have in general that
$$\hat f_k=\sum_{\ell\in\mathbb{Z}}c_{k+\ell N}(f),$$
where here for $N=4$ we have
$$\hat f_0=c_0(f)+c_4(f)+c_{-4}(f)+\dots=3+0+0=3,$$
$$\hat f_1=c_1(f)+c_5(f)+c_{-3}(f)+\dots=0+0+0=0,$$
$$\hat f_2=c_2(f)+c_6(f)+c_{-2}(f)+\dots=1+0+1=2,$$
$$\hat f_3=c_3(f)+c_7(f)+c_{-1}(f)+\dots=0+0+0=0.$$
or in short $\hat{\mathbf{f}}=(3,0,2,0)$.

Note that in the sums above we continued with $\dots$ after in both directions the first of the zeros appeared after which all terms are zero.

c) Similarly for $N=6$ we have
$$\hat f_0=c_0(f)+c_6(f)+c_{-6}(f)+\dots=3+0+0=3,$$
$$\hat f_1=c_1(f)+c_7(f)+c_{-5}(f)+\dots=0,$$
$$\hat f_2=c_2(f)+c_8(f)+c_{-4}(f)+\dots=1+0+0=1,$$
$$\hat f_3=c_3(f)+c_9(f)+c_{-3}(f)+\dots=0,$$
$$\hat f_4=c_4(f)+c_{10}(f)+c_{-2}(f)+\dots=0+0+1=1,$$
$$\hat f_5=c_5(f)+c_{11}(f)+c_{-1}(f)+\dots=0.$$
or in short $\hat{\mathbf{f}}=(3,0,1,0,1,0)$.

d) For the first case with $N=4$ a reconstruction of the Fourier coefficients $c_k(f)$ is not possible, since (very practially) we can not distinguish between the coefficients $c_{-2}(f)$ and $c_2(f)$, which are summed in $\hat f_2$.

For the second case with $N=6$ we could reconstruct the coefficients, even if $c_{\pm1}(f)$ would be nonzero.

e) The so-called Nyquist rate is $2B+1$ where in our case $B=2$, hence the smallest $N$ is $2B+1=5$ here.

Or a bit informally: In the Aliasing formulae each of the $c_{-2}(f),\dots,c_2(f)$ would "land" on its unique $\hat f_3,\hat f_4,\hat f_0,\hat f_1,\hat f_2$ (in exactly that order) and the reconstruction is still possible in any case for this bandlimit of $B=2$, that is even if $c_{\pm1}(f)$ is nonzero.

**Grading manual**

a) (1p)

b) (3p)

c) (3p)

d) (2p)

e) (1p)

Kildesett: course=TMA4125 term=sommer year=2025 problem=5 points=10 file=math4n-2025s-en-lf.pdf
