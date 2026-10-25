### **Solution to Problem 3**

The integral is the squared $L^{2}(0,2\pi)$-distance from $x$ to the function $a\cos t+b\sin t$ in the subspace $M=\operatorname{span}\{\cos t,\sin t\}$. It is minimal precisely when the error $x-(a\cos t+b\sin t)$ is orthogonal to both $\cos t$ and $\sin t$, i.e. when $(a,b)$ solve the normal equations. The needed inner products are

$$\int_{0}^{2\pi}\cos^{2}t\,dt=\pi,\qquad \int_{0}^{2\pi}\sin^{2}t\,dt=\pi,\qquad \int_{0}^{2\pi}\cos t\,\sin t\,dt=0,$$

so $\{\cos t,\sin t\}$ is already an orthogonal system, and

$$a=\frac{\langle x,\cos t\rangle}{\langle\cos t,\cos t\rangle}=\frac1\pi\int_{0}^{\alpha}\cos t\,dt=\frac{\sin\alpha}{\pi},\qquad
b=\frac{\langle x,\sin t\rangle}{\langle\sin t,\sin t\rangle}=\frac1\pi\int_{0}^{\alpha}\sin t\,dt=\frac{1-\cos\alpha}{\pi}.$$

(The two coefficients come out real, hence in particular complex, as required.)

Kildesett: course=TMA4145 term=host year=2007 problem=3 file=tma4145eksh07en.pdf
