### **Solution to Problem 7**

Denote $x_i:=ih$ and $t_j:=jk$, and let $u_{i,j}$ be a numerical approximation of $u(x_i,t_j)$.

The left hand side of the PDE can be discretised (in order to obtain an explicit method) as

$$\frac{\partial u}{\partial t}(x_i,t_j)\approx\frac{u_{i,j+1}-u_{i,j}}{k},$$

and the right hand side as

$$t_ju(x_i,t_j)+\frac{\partial^2u}{\partial x^2}(x_i,t_j)\approx jku_{i,j}+\frac{u_{i-1,j}-2u_{i,j}+u_{i+1,j}}{h^2}\,.$$

Thus one obtains

$$\frac{u_{i,j+1}-u_{i,j}}{k}=jku_{i,j}+\frac{u_{i-1,j}-2u_{i,j}+u_{i+1,j}}{h^2}$$

or, explicitly,

$$u_{i,j+1}=u_{i,j}+k\left(jku_{i,j}+\frac{u_{i-1,j}-2u_{i,j}+u_{i+1,j}}{h^2}\right)\,.$$

With $h=1/4$ and $k=1/10$, this becomes

$$u_{i,j+1}=u_{i,j}+\frac{j}{100}u_{i,j}+\frac{8}{5}(u_{i-1,j}-2u_{i,j}+u_{i+1,j}).$$

Now we use the initial condition $u(x,0)=x$ in order to obtain that

$$\begin{array}{c}u_{0,0}=0,\\[4pt] u_{1,0}=\displaystyle\frac{1}{4},\\[6pt] u_{2,0}=\displaystyle\frac{1}{2},\\[6pt] u_{3,0}=\displaystyle\frac{3}{4},\\[6pt] u_{4,0}=1.\end{array}$$

Thus

$$\begin{array}{l}\displaystyle u_{1,1}=u_{1,0}+0+\frac{8}{5}(u_{0,0}-2u_{1,0}+u_{2,0})=\frac{1}{4},\\[10pt] \displaystyle u_{2,1}=u_{2,0}+0+\frac{8}{5}(u_{1,0}-2u_{2,0}+u_{3,0})=\frac{1}{2},\\[10pt] \displaystyle u_{3,1}=u_{3,0}+0+\frac{8}{5}(u_{2,0}-2u_{3,0}+u_{4,0})=\frac{3}{4}.\end{array}$$

For the next iteration, we use the boundary conditions

$$u_{0,1}=0\qquad\text{and}\qquad u_{4,1}=1,$$

and obtain

$$\begin{array}{l}\displaystyle u_{1,2}=u_{1,1}+\frac{1}{100}u_{1,1}+\frac{8}{5}(u_{0,1}-2u_{1,1}+u_{2,1})=\frac{101}{400}=0.2525,\\[10pt] \displaystyle u_{2,2}=u_{2,1}+\frac{1}{100}u_{2,1}+\frac{8}{5}(u_{1,1}-2u_{2,1}+u_{3,1})=\frac{101}{200}=0.505,\\[10pt] \displaystyle u_{3,2}=u_{3,1}+\frac{1}{100}u_{3,1}+\frac{8}{5}(u_{2,1}-2u_{3,1}+u_{4,1})=\frac{303}{400}=0.7575.\end{array}$$

Kildesett: course=TMA4125 term=kont year=2016 problem=7 file=english.pdf
