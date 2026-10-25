### **Solution to Problem 1** **Interpolation [10 pts]**

We use the direct method. We are looking for a solution to the following linear system of equations:

$$2=c_0+0\cdot c_1-c_2-c_3+0\cdot c_4\tag{1}$$

$$\sqrt{2}=c_0+\frac{\sqrt{2}}{2}c_1-\frac{\sqrt{2}}{2}c_2+0\cdot c_3-c_4\tag{2}$$

$$0=c_0+c_1+0\cdot c_2+c_3+0\cdot c_4\tag{3}$$

$$\sqrt{2}=c_0+\frac{\sqrt{2}}{2}c_1+\frac{\sqrt{2}}{2}c_2+0\cdot c_3+c_4\tag{4}$$

$$2=c_0+0\cdot c_1+c_2-c_3+0\cdot c_4\tag{5}$$

Comparing the equations (1) and (5), we conclude that $c_2=0$. Then subtracting (4) from (2) we also see that $c_4=0$ and the system is reduced to the following system with three unknowns and three equations

$$2=c_0-c_3$$

$$\sqrt{2}=c_0+\frac{\sqrt{2}}{2}c_1$$

$$0=c_0+c_1+c_3$$

The solution is $c_0=0,c_1=2,c_3=-2$. Then $t(x)=2\cos x-2\cos 2x$.

**Grading manual** (10p) in total.

Kildesett: course=TMA4135 term=host year=2023 problem=1 points=10 file=tma4130_2023h_exam.pdf
