### **Solution to Problem 5**

The integral is the square of the distance from $f(t)=4t^{2}-4t$ to the subspace spanned by $\varphi_{1}(t)=\sin(2\pi t)$, $\varphi_{2}(t)=\cos(\pi t)$ and $\varphi_{3}(t)=1$, so we must solve the Gram system $G\,(a,b,c)^{\top}=\bigl((f,\varphi_{1}),(f,\varphi_{2}),(f,\varphi_{3})\bigr)^{\top}$ with $G_{ij}=(\varphi_{i},\varphi_{j})$.

The Gram matrix entries are

$$G=\begin{bmatrix}1/2&4/(3\pi)&0\\ 4/(3\pi)&1/2&0\\ 0&0&1\end{bmatrix}$$

using $\int_{0}^{1}\sin^{2}(2\pi t)\,dt=\int_{0}^{1}\cos^{2}(\pi t)\,dt=1/2$, $\int_{0}^{1}\sin(2\pi t)\cos(\pi t)\,dt=\tfrac{1}{2}\int_{0}^{1}\bigl(\sin(3\pi t)+\sin(\pi t)\bigr)dt=4/(3\pi)$, and $\int_{0}^{1}\sin(2\pi t)\,dt=\int_{0}^{1}\cos(\pi t)\,dt=0$.

For the right-hand side, the substitution $t\mapsto 1-t$ shows that $f(1-t)=f(t)$ while $\varphi_{1}(1-t)=-\varphi_{1}(t)$ and $\varphi_{2}(1-t)=-\varphi_{2}(t)$, so (pairing the integrals over $[0,1/2]$ and $[1/2,1]$) $(f,\varphi_{1})=(f,\varphi_{2})=0$; direct integration gives

$$(f,1)=\int_{0}^{1}(4t^{2}-4t)\,dt=\left[\tfrac{4}{3}t^{3}-2t^{2}\right]_{0}^{1}=\tfrac{4}{3}-2=-\tfrac{2}{3}.$$

The system is

$$\tfrac{1}{2}a+\tfrac{4}{3\pi}b=0,\qquad \tfrac{4}{3\pi}a+\tfrac{1}{2}b=0,\qquad c=-\tfrac{2}{3}.$$

The determinant of the first two equations is $\tfrac{1}{4}-\tfrac{16}{9\pi^{2}}\ne 0$, so $a=b=0$. The minimum is thus attained at

$$a=0,\qquad b=0,\qquad c=-\tfrac{2}{3}.$$

*Kjeldevarsel: fasiten reknar $(f,1)=\left[\tfrac{4}{3}t^{3}-2t^{2}\right]_{0}^{1}=\tfrac{26}{3}$ og oppgav difor $c=26/3$ — men $4/3-2=-2/3$ (kontrollrekna med sympy), så det rette svaret er $c=-2/3$. Fasitens $a=0$ og $b=0$ er rette.*

Kildesett: course=TMA4145 term=kont year=2009 problem=5 file=tma4145ekss09en.pdf
