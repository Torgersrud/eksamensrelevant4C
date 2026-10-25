### **Solution to Problem 4**

There are two things to spot at the start which simplify this problem considerably.

The first is that the three conditions are all in terms of the inner product and so $W$ can be written as the set of all polynomials $p\in\text{Poly}_3$ such that:

$$\langle q_1,p\rangle=0,$$

$$\langle q_2,p\rangle=0,$$

$$\langle q_3,p\rangle=0,$$

where the $q_j$ are formed by rearranging the conditions to get all the terms on the same side. Thus $W$ is specified by giving a spanning set for its orthogonal complement. One way to proceed would therefore be to use Gram–Schmidt to reduce this to an orthonormal basis, use this to find the projection of $p$ onto $W^{\perp}$, and hence by subtraction find the projection of $p$ onto $W$.

Before doing that, we notice one other fact about the problem. The integral in the inner product is symmetric about the origin. This means that the inner product of an odd function with an even function will be 0, so all odd functions are orthogonal to all even functions. This suggests that when trying to split things into orthogonal families, a first step would be to split them into even and odd functions.

So let us do that with the spanning set for $W^{\perp}$:

$$q_1(t)=3(t^{2}+t)-(1+5t^{3})\qquad=(3t^{2}-1)+(3t-5t^{3})$$

$$q_2(t)=(-6t^{2}+5t^{3})-(-2+3t)\qquad=(-6t^{2}+2)+(5t^{3}-3t)$$

$$q_3(t)=(-3+6t)-(-9t^{2}+10t^{3})\qquad=(-3+9t^{2})+(6t-10t^{3})$$

From this, we can see that we get an orthogonal (but not orthonormal) basis by taking $r_1(t)=3t^{2}-1$ and $r_2(t)=5t^{3}-3t$.

Now $p(t)=3t^{2}-5t^{3}$ so, again using the even-odd property, $\langle r_1,p\rangle=\langle r_1,3t^{2}\rangle$ and $\langle r_2,p\rangle=\langle r_2,-5t^{3}\rangle$. These are not difficult to work out:

$$\langle r_1,p\rangle=\int_{-1}^{1}(3t^{2}-1)(3t^{2})dt=\int_{-1}^{1}9t^{4}-3t^{2}dt=\frac{18}{5}-2=\frac{8}{5},$$

$$\langle r_1,p\rangle=\int_{-1}^{1}(5t^{3}-3t)(5t^{3})dt=\int_{-1}^{1}25t^{6}-15t^{4}dt=\frac{50}{7}-6=\frac{8}{7}.$$

We also need to work out the lengths of $r_1$ and $r_2$. These are a little messier, but not much.

$$\langle r_1,r_1\rangle=\int_{-1}^{1}(3t^{2}-1)(3t^{2}-1)dt=\int_{-1}^{1}9t^{4}-6t^{2}+1dt=\frac{18}{5}-2=\frac{8}{5},$$

$$\langle r_2,r_2\rangle=\int_{-1}^{1}(5t^{3}-3t)(5t^{3}-3t)dt=\int_{-1}^{1}25t^{6}-30t^{4}+9t^{2}=\frac{50}{7}-12+6=\frac{8}{7}.$$

Substituting in to the formula for the closest point, we get

$$\frac{\langle p,r_1\rangle}{\langle r_1,r_1\rangle}r_1+\frac{\langle p,r_2\rangle}{\langle r_2,r_2\rangle}r_2=r_1+r_2=5t^{3}+3t^{2}-3t-1.$$

Then taking this away from $p$ results in $3t+1$, which must therefore be the closest point to $p$ in $W$.

*Kjeldevarsel: løysingsforslaget har tre trykkfeil i rekkjefølgjene. (1) Det andre indreproduktet i «not difficult to work out»-blokken står trykt som $\langle r_1,p\rangle$, men etter teksten over skal det vere $\langle r_2,p\rangle$. (2) Prosjeksjonslinja er trykt som $r_1+r_2$, men koeffisientane $\frac{8/5}{8/5}=1$ og $\frac{\langle p,r_2\rangle}{\langle r_2,r_2\rangle}=-1$ gir $r_1-r_2=-5t^{3}+3t^{2}+3t-1$ — rekna om med sympy. (3) Følgjer ein det trykte $r_1+r_2$, blir $p-(r_1+r_2)=-10t^{3}+3t+1$, ikkje det trykte svaret $3t+1$; med det rette projeksjonsleddet $r_1-r_2$ blir næraste punkt $p-(r_1-r_2)=1-3t$. Kontroll: $1-3t\in W$ og $\lVert p-(1-3t)\rVert^{2}=\lVert r_1-r_2\rVert^{2}=96/35$, mot $936/35$ for $3t+1$. Rett svar er difor $1-3t$.*

Kildesett: course=TMA4145 term=host year=2011 problem=4 file=tma4145eksh11en.pdf
