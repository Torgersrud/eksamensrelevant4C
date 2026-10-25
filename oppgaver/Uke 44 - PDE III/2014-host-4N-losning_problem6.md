### **Solution to Problem 6**

**a)** Using the notation of the text, we have that $(x_1,y_1)=(1,1)$, $(x_2,y_1)=(2,1)$ and $(x_1,y_2)=(1,2)$, so we write $u_{11}=u(1,1)$, $u_{12}=u(1,2)$ and $u_{21}=u(2,1)$. The equation gives us the following relations

$$\frac{u_{i+1,j}+u_{i-1,j}-2u_{i,j}}{h^2}+\frac{u_{i,j+1}+u_{i,j-1}-2u_{i,j}}{h^2}=2(ih)(jh)$$

so if we replace $h=1$ we have

$$u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}-4u_{i,j}=2ij$$

Therefore we set up the 3 equations with $(i,j)=(1,1)$ and $(i,j)=(1,2)$ and $(i,j)=(2,1)$

$$\left\{\begin{array}{l}u_{21}+u_{01}+u_{12}+u_{10}-4u_{11}=2\\ u_{22}+u_{02}+u_{13}+u_{11}-4u_{12}=4\\ u_{31}+u_{11}+u_{22}+u_{20}-4u_{21}=4\end{array}\right.$$

So using the boundary conditions we have $u_{0,1}=u_{1,0}=u_{0,2}=u_{2,0}=1$, and $u_{2,2}=\frac{2^2+2^2}{16}=\frac{1}{2}$, $u_{1,3}=\frac{1+3^2}{16}=\frac{5}{8}$ and $u_{3,1}=\frac{3^2+1}{16}=\frac{5}{8}$, so the desired system is

$$\left\{\begin{array}{l}u_{21}+1+u_{12}+1-4u_{11}=2\\ \frac{1}{2}+1+\frac{5}{8}+u_{11}-4u_{12}=4\\ \frac{5}{8}+u_{11}+\frac{1}{2}+1-4u_{21}=4\end{array}\right.$$

and

$$\left\{\begin{array}{l}u_{21}+u_{12}-4u_{11}=0\\ u_{11}-4u_{12}=\frac{15}{8}\\ u_{11}-4u_{21}=\frac{15}{8}\end{array}\right.$$

**b)** We set up the system

$$\left\{\begin{array}{l}u_{21}+u_{12}-4u_{11}=0\\ u_{11}-4u_{12}=\frac{15}{8}\\ u_{11}-4u_{21}=\frac{15}{8}\end{array}\right.$$

in the Gauss-Seidel form

$$\left\{\begin{array}{l}-\frac{1}{4}u_{21}-\frac{1}{4}u_{12}+u_{11}=0\\ -\frac{1}{4}u_{11}+u_{12}=-\frac{15}{32}\\ -\frac{1}{4}u_{11}+u_{21}=-\frac{15}{32}\end{array}\right.$$

so the Gauss-Seidel iteration formula is

$$u_{11}^{(n+1)}=\frac{1}{4}u_{21}^{(n)}+\frac{1}{4}u_{12}^{(n)}$$

$$u_{12}^{(n+1)}=\frac{1}{4}u_{11}^{(n+1)}-\frac{15}{32}$$

$$u_{21}^{(n+1)}=\frac{1}{4}u_{11}^{(n+1)}-\frac{15}{32}$$

So if we start with $u_{11}^{(0)}=u_{12}^{(0)}=u_{21}^{(0)}=0$

$$u_{11}^{(1)}=\frac{1}{4}0+\frac{1}{4}0=0$$

$$u_{12}^{(1)}=\frac{1}{4}0-\frac{15}{32}=-\frac{15}{32}$$

$$u_{21}^{(1)}=\frac{1}{4}0-\frac{15}{32}=-\frac{15}{32}$$

and continue with the second step

$$u_{11}^{(2)}=\frac{1}{4}\left(-\frac{15}{32}\right)+\frac{1}{4}\left(-\frac{15}{32}\right)=-\frac{15}{64}$$

$$u_{12}^{(2)}=\frac{1}{4}\left(-\frac{15}{64}\right)-\frac{15}{32}=-\frac{135}{256}$$

$$u_{21}^{(2)}=\frac{1}{4}\left(-\frac{15}{64}\right)-\frac{15}{32}=-\frac{135}{256}$$

and finally the

$$u_{11}^{(3)}=\frac{1}{4}\left(-\frac{135}{256}\right)+\frac{1}{4}\left(-\frac{135}{256}\right)=-\frac{135}{512}$$

$$u_{12}^{(3)}=\frac{1}{4}\left(-\frac{135}{512}\right)-\frac{15}{32}=-\frac{1095}{2048}$$

$$u_{21}^{(3)}=\frac{1}{4}\left(-\frac{135}{512}\right)-\frac{15}{32}=-\frac{1095}{2048}$$

Kildesett: course=TMA4130 term=host year=2014 problem=6 file=eksam2014.pdf
