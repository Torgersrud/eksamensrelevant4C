### **Solution to Problem 5**

(Problem 4 for Math 4M)

**a)** We use the following approximation of the Laplace operator:

$$\Delta u(x,y)=\frac{1}{h^{2}}\left(u(x+h,y)+u(x-h,y)+u(x,y+h)+u(x,y-h)-4u(x,y)\right).$$

Combining this with the central difference approximation of $u_{x}$ given in the problem, we obtain the following difference scheme for the given PDE:

$$1=\frac{1}{h^{2}}\left(u(x+h,y)+u(x-h,y)+u(x,y+h)+u(x,y-h)-4u(x,y)\right)$$

$$+\frac{1}{2h}\left(u(x+h,y)-u(x-h,y)\right).$$

(With the notation $u_{i,j}\approx u(i,j)$ — i.e. the approximation of the solution to the Dirichlet problem at the grid-points — the above can be expressed as:

$$u_{i,j}=\frac{3}{8}u_{i+1,j}+\frac{1}{8}u_{i-1,j}+\frac{1}{4}u_{i,j+1}+\frac{1}{4}u_{i,j-1}-\frac{1}{4}.\ \ )$$

**b)** The unknown quantities are then $u_{1,1}$, $u_{2,1}$, $u_{2,1}$ and $u_{2,2}$ while the other $u_{i,j}$s are given by the prescribed boundary values. One iteration with the Gauss-Seidel method, with the starting values equal to 1, yields:

$$u_{1,1}=\frac{3}{8}u_{2,1}+\frac{1}{8}u_{0,1}+\frac{1}{4}u_{1,2}+\frac{1}{4}u_{1,0}-\frac{1}{4}=\frac{3}{8}+\frac{1}{8}=\frac{1}{2},$$

$$u_{2,1}=\frac{3}{8}u_{3,1}+\frac{1}{8}u_{1,1}+\frac{1}{4}u_{2,2}+\frac{1}{4}u_{2,0}-\frac{1}{4}=2\times\frac{3}{8}+\frac{1}{8}\times\frac{1}{2}+\frac{1}{4}+0-\frac{1}{4}=\frac{13}{16},$$

$$u_{1,2}=\frac{3}{8}u_{2,2}+\frac{1}{8}u_{0,2}+\frac{1}{4}u_{1,3}+\frac{1}{4}u_{1,1}-\frac{1}{4}=\frac{3}{8}+\frac{1}{8}+0+\frac{1}{4}\times\frac{1}{2}-\frac{1}{4}=\frac{3}{8},$$

and

$$u_{2,2}=\frac{3}{8}u_{3,2}+\frac{1}{8}u_{1,2}+\frac{1}{4}u_{2,3}+\frac{1}{4}u_{2,1}-\frac{1}{4}=2\times\frac{3}{8}+\frac{1}{8}\times\frac{3}{8}+0+\frac{1}{4}\times\frac{13}{16}-\frac{1}{4}=\frac{3}{4}.$$

These are the approximations of $u(1,1)$, $u(2,1)$, $u(1,2)$ and $u(2,2)$ sought for.

*Kjeldevarsel: Eksamen-PDF-en for dette haustsettet blei aldri publisert; løysingsfila `solutions_2012h.pdf` er difor Kildesett, og oppgåveteksten er ikkje gjenteken i løysinga. I første linje av b) er den tredje ukjende trykt som $u_{2,1}$ — etter reknestycka under skal det vere $u_{1,2}$; bevart ordrett. Det same gjeld den overskotige høgreparentesen til slutt i parenteuset i a) og «$u_{i,j}$s» utan skiljeteikn. Gauss–Seidel-tala $1/2$, $13/16$, $3/8$, $3/4$ er kontrollreknade med brørekning og stemmer med randverdiane utrekninga legg til grunn ($u_{0,j}=1$, $u_{3,j}=2$, nedre og øvre rand 0, startverdiar 1).*

Kildesett: course=TMA4130 term=host year=2012 problem=5 file=solutions_2012h.pdf
