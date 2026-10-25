### **Solution to Problem 1**

**a)** Three points may be interpolated with a quadratic polynomial $p(x)$. Using Lagrange interpolation

$$p(x)=\frac{(x-\frac{1}{2})(x-1)}{-\frac{1}{2}}\cdot 0+\frac{(x-0)(x-1)}{\frac{1}{2}\cdot\left(-\frac{1}{2}\right)}\frac{\sin(\frac{\pi}{2})}{\frac{1}{2}+1}+\frac{x(x-\frac{1}{2})}{\frac{1}{2}}\cdot 0=\frac{8}{3}x(1-x).$$

**b)** Since $p(x)$ is a good approximation to $f(x)$, we have that

$$I\approx\int_{0}^{1}p(x)\ dx=\frac{8}{3}\int_{0}^{1}x(1-x)\ dx=\frac{8}{6}-\frac{8}{9}=\frac{4}{9}.$$

**c)** We want to determine the polynomial $q(x)$ using $p(x)$. Hence, we write $q(x)$ as a sum of $p(x)$ and a polynomial which is zero in the points given in $a$:

$$q(x)=p(x)+\frac{x(x-\frac{1}{2})(x-1)}{\frac{3}{2}\cdot\frac{1}{2}}C,$$

where $C$ is to be determined such that $q(1.5)=f(1.5)$. Hence,

$$C=f(1.5)-p(1.5)=\frac{\sin\left(\frac{3\pi}{2}\right)}{\frac{3}{2}+1}-\frac{8}{3}\frac{3}{2}\left(1-\frac{3}{2}\right)=\frac{8}{5},$$

and consequently,

$$q(x)=\frac{8}{3}x(1-x)+\frac{32}{15}x\left(x-\frac{1}{2}\right)(x-1).$$

*Kjeldevarsel: Det fyrste leddet i Lagrange-formelen i a) er trykt med nemnar $-\frac{1}{2}$; differansefaktorane for noden $x=0$ er $(0-\frac{1}{2})(0-1)=+\frac{1}{2}$. Trykkfeilen er ufarleg fordi leddet blir multiplisert med $f(0)=0$.*

Kildesett: course=TMA4123 term=var year=2014 problem=1 file=v14-english.pdf
