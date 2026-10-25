### **Solution to Problem 10**

If we define $u_{i,j}:=u(ih,jh)$, the difference method gives us the following equation

$$\frac{1}{h^2}(u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}-4u_{i,j})=2(ih\cdot jh)$$

So if $h=1$ we have the following equations

$$u_{2,1}+u_{0,1}+u_{1,2}+u_{1,0}-4u_{1,1}=2(1\cdot1)=2$$
$$u_{3,1}+u_{1,1}+u_{2,2}+u_{2,0}-4u_{2,1}=2(2\cdot1)=4$$
$$u_{2,2}+u_{0,2}+u_{1,3}+u_{1,1}-4u_{1,2}=2(1\cdot2)=4$$

and using the boundary conditions

$$u_{2,1}+1+u_{1,2}+1-4u_{1,1}=2$$
$$4+u_{1,1}+4+2-4u_{2,1}=4$$
$$4+2+4+u_{1,1}-4u_{1,2}=4$$

Hence the the desired linear system is

$$u_{2,1}+u_{1,2}-4u_{1,1}=0$$
$$u_{1,1}-4u_{2,1}=-6$$
$$u_{1,1}-4u_{1,2}=-6$$

Kildesett: course=TMA4130 term=host year=2016 problem=10 file=n16h.pdf
