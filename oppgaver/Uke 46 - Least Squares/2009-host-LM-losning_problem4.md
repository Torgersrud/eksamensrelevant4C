### **Solution to Problem 4**

**1.** Linearity in the first argument and conjugate symmetry follow directly from the corresponding properties of complex numbers:

$$\langle p_{1}+\lambda p_{2},q\rangle=\sum_{j=0}^{3}\bigl(p_{1}(j)+\lambda p_{2}(j)\bigr)\overline{q(j)}=\langle p_{1},q\rangle+\lambda\langle p_{2},q\rangle,$$

$$\langle p,q\rangle=\sum_{j=0}^{3}p(j)\overline{q(j)}=\overline{\sum_{j=0}^{3}q(j)\overline{p(j)}}=\overline{\langle q,p\rangle}.$$

For non-degeneracy: if $\langle p,p\rangle=\sum_{j=0}^{3}\lvert p(j)\rvert^{2}=0$, then $p(j)=0$ for $j\in\{0,1,2,3\}$; a polynomial of degree at most $3$ with four roots is the zero polynomial. Positive-homogeneity $\langle p,p\rangle=\sum\lvert p(j)\rvert^{2}\ge 0$ is clear. So this is an inner product.

**2.** We have

$$\langle 1,1\rangle=\sum_{j=0}^{3}1=4,$$

so we normalise $1$ to $1/2$. Next,

$$\langle t,1/2\rangle=\sum_{j=0}^{3}j/2=(0+1+2+3)/2=3,$$

so subtracting $\langle t,1/2\rangle\cdot(1/2)=3/2$ from $t$ leaves $t-3/2$, which is orthogonal to $1/2$. The length of $t-3/2$ is

$$\langle t-3/2,t-3/2\rangle=\sum_{j=0}^{3}(j-3/2)^{2}=9/4+1/4+1/4+9/4=5,$$

so an orthonormal basis of $\mathrm{Poly}_{1}$ is

$$\left\{\,1/2,\;(1/\sqrt{5})(t-3/2)\,\right\}.$$

**3.** The projection (closest point) is

$$\langle p,1/2\rangle\cdot 1/2+\langle p,(t-3/2)/\sqrt{5}\rangle\cdot(t-3/2)/\sqrt{5}=\tfrac{1}{4}\langle p,1\rangle\cdot 1+\tfrac{1}{5}\bigl(\langle p,t\rangle-\tfrac{3}{2}\langle p,1\rangle\bigr)(t-3/2).$$

From the specification,

$$\langle p,1\rangle=p(0)+p(1)+p(2)+p(3)=-3+1+3+3=4,$$
$$\langle p,t\rangle=p(1)+2p(2)+3p(3)=1+6+9=16,$$

so the closest point is $1+\frac{1}{5}(16-6)(t-3/2)=1+2(t-3/2)$, i.e.

$$2t-2.$$

**4.** No. If $\deg p\le 1$ we would have $p=2t-2$, but $2t-2$ takes the value $-2$ at $t=0$, not $-3$.

Kildesett: course=TMA4145 term=host year=2009 problem=4 file=tma4145eksh09en.pdf
