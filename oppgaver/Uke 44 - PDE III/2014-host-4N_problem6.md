### **Problem 6**

Let $\mathcal{R}$ be the region defined by the lines

$$L_1:\ y=4-x\qquad L_2: y=0\qquad L_3: x=0\,.$$

Let $u(x,y)$ be the function defined in $\mathcal{R}$ satisfying the Poisson equation

$$\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}=2xy$$

and the boundary conditions

$$\begin{array}{ll}u(x,y)=\frac{x^2+y^2}{16}&\text{if }(x,y)\in L_1\\ u(x,y)=1&\text{if }(x,y)\in L_2\\ u(x,y)=1&\text{if }(x,y)\in L_3\end{array}$$

[Figure: Koordinatsystem med x- og y-akse, merka med 4 på begge aksar. Skravert rettvinkla trekant med hjørne i (0,0), (4,0) og (0,4), merkt $\mathcal{R}$ inni. Langs venstre katet står «$u=1$» (vertikal tekst), langs nedre katet står «$u=1$», og langs hypotenusen står «$u=\frac{x^2+y^2}{16}$» (skrå tekst). Heile trekanten er punktert med eit raster med einingsavstand: randpunkt med heiltalskoordinatar langs alle tre sidene (inkludert (0,1), (0,2), (0,3), (1,0), (2,0), (3,0), (1,3), (2,2), (3,1)) og dei indre punkta (1,1), (1,2) og (2,1).]

**a)** Let us define the points $(x_i,y_j)=(i\cdot h,j\cdot h)$ with $h=1$. Use the method of difference equations with $h=1$ in order to set up a linear system for finding approximations of the values $u(1,1)$, $u(1,2)$ and $u(2,1)$.

**b)** Write the linear system you have found in **a)** in such a form that you can apply the Gauss-Seidel method. Then carry out three iterations of the Gauss-Seidel method with starting values 0 in all the variables. (Use only 4 decimals in your computations.)

Kildesett: course=TMA4130 term=host year=2014 problem=6 file=eksam2014.pdf
