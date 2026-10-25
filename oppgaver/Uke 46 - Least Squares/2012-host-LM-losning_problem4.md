### **Solution to Problem 4**

**a)** Let

$$e_1:=\tfrac{1}{\sqrt{2}}(1,1,0),$$

so that $\{e_1\}$ is an orthonormal basis for $M$. Since—in the Hilbert space $\mathbb{R}^{3}$ with the inner product $\langle x,y\rangle=\sum_{j=1}^{3}x_jy_j$ (which corresponds to the given norm)—Fourier coefficients are best possible, we get

$$y_0=\langle x_0,e_1\rangle e_1=\tfrac{1}{2}\langle(1,2,3),(1,1,0)\rangle(1,1,0)=(\tfrac{3}{2},\tfrac{3}{2},0),$$

with

$$d^{2}=\lVert(1,2,3)\rVert^{2}-\left|\frac{1}{\sqrt{2}}\langle(1,2,3),(1,1,0)\rangle\right|^{2}=\frac{19}{2},$$

so that the minimal distance $\inf_{y\in M}\lVert x_0-y\rVert=\sqrt{\frac{19}{2}}$ is realized by $y_0=(\frac{3}{2},\frac{3}{2},0)\in M$. (One can check the answer, for example, by minimizing $f(t):=\lVert(1-t,2-t,3)\rVert^{2}$.)

**c)** $L_2((0,1),\mathbb{R})$ is a Hilbert space, and $M$ is a finite-dimensional subspace, whence closed and convex (and non-empty); the existence of a unique minimizing element $y_0$ is thus guaranteed by the minimal distance theorem. We find $y_0$ by constructing an orthonormal basis $\{e_1,e_2\}$ for $M$. Since

$$\int_0^{1}|1|^{2}\,dt=1\quad\text{let}\quad e_1:=1.$$

(*Fotnote 2 i løysingsforslaget: «We adopt here, as in the problem formulation, the slight abuse of notation $f=f(t)$.»*)

Then let

$$v_2=t-\langle t,1\rangle1=t-\int_0^{1}t\,dt=t-\frac{1}{2},$$

and

$$e_2=\frac{v_2}{\lVert v_2\rVert}=\sqrt{3}(2t-1)$$

Thus,

$$y_0=\langle t^{2},e_1\rangle e_1+\langle t^{2},e_2\rangle e_2=\int_0^{1}s^{2}\,ds+3\left(\int_0^{1}s^{2}(2s-1)\,ds\right)(2t-1),$$

and $y_0=t-\frac{1}{6}$ is the unique minimizing element. The distance is given by

$$d^{2}=\lVert x_0\rVert^{2}-|\langle t^{2},e_1\rangle|^{2}-|\langle t^{2},e_2\rangle|^{2}$$

$$=\int_0^{1}t^{4}\,dt-\left(\int_0^{1}t^{2}\,dt\right)^{2}-3\left(\int_0^{1}t^{2}(2t-1)\,dt\right)^{2}$$

$$=\frac{1}{5}-\frac{1}{9}-\frac{1}{12}=\frac{1}{180},$$

where the values of the integrals $\langle t^{2},e_1\rangle$ and $\langle t^{2},e_2\rangle$ are already known. Hence, $d=\frac{1}{6\sqrt{5}}$.

*(Oppgåvens punkt b) er utelatt — sjå Kjeldevarselet i oppgåveteksten. Løysingsforslaget reknar likevel dette punktet ut; det er utelatt her.)*

Kildesett: course=TMA4145 term=host year=2012 problem=4 file=tma4145eksh12en.pdf
