### **Solution to Problem 5**

Let $f_1(t)=\sin t$ and $f_2(t)=\sin 2t$. We have that

$$\langle f_1,f_2\rangle=\int_0^{2\pi}\sin t\sin 2t\,dt=2\int_0^{2\pi}\sin^2 t\cos t\,dt=\left[\frac{2}{3}\sin^3 t\right]_0^{2\pi}=0,$$

so $f_1$ and $f_2$ are orthogonal in $L^2[0,2\pi]$. Moreover, we have that

$$\lVert f_1\rVert_2^2=\int_0^{2\pi}\sin^2 t\,dt=\frac{1}{2}\int_0^{2\pi}(1-\cos 2t)\,dt=\pi$$

and

$$\lVert f_2\rVert_2^2=\int_0^{2\pi}\sin^2 2t\,dt=\frac{1}{2}\int_0^{2\pi}(1-\cos 4t)\,dt=\pi,$$

so

$$e_1:=\frac{1}{\sqrt{\pi}}f_1\quad\text{and }\quad e_2:=\frac{1}{\sqrt{\pi}}f_2$$

are orthonormal elements of $L^2[0,2\pi]$. Now observe that

$$\int_0^{2\pi}\left\lvert t-a\sin t-b\sin 2t\right\rvert^2 dt=\lVert t-af_1-bf_2\rVert_2^2=\lVert t-a\sqrt{\pi}e_1-b\sqrt{\pi}e_2\rVert_2^2.\tag{5}$$

For a finite orthonormal system $\{e_1,e_2\}$ in $L^2[0,2\pi]$ we have a unique closest point property, meaning that the right hand side of (5) is minimal if

$$a\sqrt{\pi}=\langle t,e_1\rangle=\frac{1}{\sqrt{\pi}}\int_0^{2\pi}t\sin t\,dt=-2\sqrt{\pi}$$

and

$$b\sqrt{\pi}=\langle t,e_2\rangle=\frac{1}{\sqrt{\pi}}\ \int_0^{2\pi}t\sin 2t\,dt=-\sqrt{\pi}.$$

Thus (5) is minimal if $a=-2$ and $b=-1$.

Kildesett: course=TMA4145 term=host year=2018 problem=5 file=tma4145eksh18en.pdf
