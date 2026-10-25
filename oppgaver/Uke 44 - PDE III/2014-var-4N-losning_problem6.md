### **Solution to Problem 6**

We discretize the domain $(0,1)$ into $N$ points with spacing $h$. That is, through the points

$$x_{i}=ih,\quad i=0,\ldots,N-1,\quad h=\frac{1}{N-1}.$$

Next, we discretize time through the points

$$t^{n}=n\Delta t,\quad n=0,1,2,3,\ldots$$

where $\Delta t$ is an undetermined step-size. Next, we will approximate $u(t,x)$ at these points using the notation

$$u(t^{n},x_{i})\approx u_{i}^{n},\quad i=0,\ldots,N-1,\ n=0,1,2,3,\ldots.$$

To approximate the derivatives in the PDE, we shall use the central differences

$$u_{tt}(t^{n},x_{i})\approx\frac{u_{i}^{n+1}-2u_{i}^{n}+u_{i}^{n-1}}{\Delta t^{2}},$$

$$u_{xx}(t^{n},x_{i})\approx\frac{u_{i+1}^{n}-2u_{i}^{n}+u_{i-1}^{n}}{h^{2}}.$$

In this way, we obtain the following method to determine the approximation $u_{i}^{n}$ of $u$:

1. Set the initial $u_{i}^{0}$ and $u_{i}^{1}$ as follows:

   $$u_{i}^{0}=0,\quad i=0,\ldots,N-1,$$

   $$u_{i}^{1}=\Delta t,\quad i=0,\ldots,N-1.$$

2. Determine sequentially $u_{i}^{n+1}$, $i=0,\ldots,N-1$, as follows:

   \- For $i=1,\ldots,N-2$,

   $$u_{i}^{n+1}=2u_{i}^{n}-u_{i}^{n-1}+2\frac{(\Delta t)^{2}}{h^{2}}(u_{i+1}^{n}-2u_{i}^{n}+u_{i-1}^{n})+(\Delta t)^{2}\sin(n\Delta t),$$

   \- At the boundary, set

   $$u_{0}^{n+1}=0,\quad u_{N-1}^{n+1}=0.$$

This method is second-order in $\Delta t$ and $h$.

Kildesett: course=TMA4123 term=var year=2014 problem=6 file=v14-english.pdf
