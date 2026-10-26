### **Problem 5**

(Problem 4 for Math 4M)

Consider the boundary value problem

$$u_{xx}+u_{yy}+u_x=1$$

on the square $0<x<3$, $0<y<3$ with boundary values $u=1$ on the left side, $u=2$ on the right side and $u=0$ on the lower and upper sides.

**a)** Use the central difference approximations

$$\Delta u(x,y)\approx\frac{u(x+h,y)+u(x-h,y)+u(x,y+h)+u(x,y-h)-4u(x,y)}{h^{2}},\qquad u_x(x,y)\approx\frac{u(x+h,y)-u(x-h,y)}{2h}$$

to derive a finite difference scheme for the problem. With the notation $u_{i,j}\approx u(i,j)$ and $h=1$, show that the scheme can be written as

$$u_{i,j}=\frac{3}{8}u_{i+1,j}+\frac{1}{8}u_{i-1,j}+\frac{1}{4}u_{i,j+1}+\frac{1}{4}u_{i,j-1}-\frac{1}{4}.$$

**b)** Perform one iteration with the Gauss–Seidel method, starting from the values $u_{i,j}=1$ at all interior grid points, and compute the resulting approximations of $u(1,1)$, $u(2,1)$, $u(1,2)$ and $u(2,2)$.

*Kjeldevarsel: Eksamen-PDF-en for dette haustsettet blei aldri publisert; løysingsfila `solutions_2012h.pdf` er difor Kildesett, og oppgåveteksten er ikkje gjenteken i løysinga. Domene, randverdiane ($u=1$ til venstre, $u=2$ til høgre, $u=0$ nedst og øvst) og leddet $u_x$ i PDE-en er lesne av reknestycka i fasiten, og oppgåveteksten er rekonstruert frå forma på løysinga — a) differensskjema, b) éi Gauss–Seidel-iterasjon med startverdiar 1. Løysingsfila under er Kildesett for facit.*

Kildesett: course=TMA4130 term=host year=2012 problem=5 file=solutions_2012h.pdf
