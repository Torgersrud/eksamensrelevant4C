### **Solution to Problem 5**

The weight $t$ makes this least squares in the inner product $(f,g)_{T}=\int_{0}^{1}t\,f(t)\overline{g(t)}\,dt$, projecting $f(t)=\mathrm{e}^{t}$ on to $\operatorname{span}\{1,t\}$. The normal equations for $(a,b)$ are

$$\begin{bmatrix}(1,1)_{T}&(1,t)_{T}\\ (t,1)_{T}&(t,t)_{T}\end{bmatrix}\begin{bmatrix}a\\ b\end{bmatrix}=\begin{bmatrix}(f,1)_{T}\\ (f,t)_{T}\end{bmatrix}.$$

With $\int_{0}^{1}t\,dt=1/2$, $\int_{0}^{1}t^{2}dt=1/3$, $\int_{0}^{1}t^{3}dt=1/4$ and (by parts) $\int_{0}^{1}t\,\mathrm{e}^{t}dt=1$, $\int_{0}^{1}t^{2}\mathrm{e}^{t}dt=\mathrm{e}-2$, this is

$$\begin{bmatrix}1/2&1/3\\ 1/3&1/4\end{bmatrix}\begin{bmatrix}a\\ b\end{bmatrix}=\begin{bmatrix}1\\ \mathrm{e}-2\end{bmatrix}.$$

The determinant is $1/8-1/9=1/72$, so

$$a=72\left(\frac{1}{4}-\frac{\mathrm{e}-2}{3}\right)=66-24\,\mathrm{e},\qquad b=72\left(\frac{\mathrm{e}-2}{2}-\frac{1}{3}\right)=36\,\mathrm{e}-96,$$

i.e. $a\approx 0.76124$ and $b\approx 1.85815$. The approximating function is

$$a+bt\approx 0.76124+1.85815\,t,$$

in agreement with the attached solution, which gives the closest point as $(36\mathrm{e}-96)t+(66-24\mathrm{e})$.

Kildesett: course=TMA4145 term=host year=2008 problem=5 file=tma4145eksh08en.pdf
