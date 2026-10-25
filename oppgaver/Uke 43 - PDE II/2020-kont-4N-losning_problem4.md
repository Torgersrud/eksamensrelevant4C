### **Solution to Problem 4**

Solution: A direct computation gives

$$\begin{aligned}\frac{\partial^{2}u}{\partial x^{2}}&=\frac{\partial}{\partial x}\left(\frac{\partial u}{\partial y}\frac{\partial y}{\partial x}+\frac{\partial u}{\partial z}\frac{\partial z}{\partial x}\right)\\
&=\frac{\partial}{\partial y}\left(\frac{\partial u}{\partial y}+\frac{\partial u}{\partial z}\right)\frac{\partial y}{\partial x}+\frac{\partial}{\partial z}\left(\frac{\partial u}{\partial y}+\frac{\partial u}{\partial z}\right)\frac{\partial z}{\partial x}\\
&=\frac{\partial^{2}u}{\partial y^{2}}+2\frac{\partial^{2}u}{\partial y\partial z}+\frac{\partial^{2}u}{\partial z^{2}}.\end{aligned}$$

Likewise,

$$\frac{\partial^{2}u}{\partial t^{2}}=\frac{\partial^{2}u}{\partial y^{2}}-2\frac{\partial^{2}u}{\partial y\partial z}+\frac{\partial^{2}u}{\partial z^{2}}.$$

Taking a difference and dividing by 4 on both sides yields the desired equation.

Kildesett: course=TMA4135 term=kont year=2020 problem=4 points=6 file=tma4130_kont.pdf
