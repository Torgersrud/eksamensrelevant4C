### **Solution to Problem 4**

**b.** The integral is the squared $L^{2}(0,1)$-distance from $e^{t}$ to $a+bt$ in $M=\operatorname{span}\{1,t\}$, so it is minimal precisely when the error is orthogonal to $1$ and $t$ — that is, when $(a,b)$ solves the normal equations

$$\begin{bmatrix}\langle 1,1\rangle&\langle t,1\rangle\\ \langle 1,t\rangle&\langle t,t\rangle\end{bmatrix}\begin{bmatrix}a\\ b\end{bmatrix}=\begin{bmatrix}\langle e^{t},1\rangle\\ \langle e^{t},t\rangle\end{bmatrix}.$$

The entries are

$$\langle 1,1\rangle=1,\quad \langle 1,t\rangle=\frac12,\quad \langle t,t\rangle=\frac13,\qquad
\langle e^{t},1\rangle=\int_{0}^{1}e^{t}dt=e-1,\quad \langle e^{t},t\rangle=\int_{0}^{1}te^{t}dt=1,$$

so

$$a+\frac{b}{2}=e-1,\qquad \frac{a}{2}+\frac{b}{3}=1 .$$

Subtracting half of the first equation from the second gives $b/12=1-(e-1)/2=(3-e)/2$, hence

$$b=6(3-e)=18-6e,\qquad a=(e-1)-\frac{b}{2}=(e-1)-3(3-e)=4e-10 .$$

(Both come out real, hence complex, as required; numerically $a\approx 0.8731$ and $b\approx 1.6903$. This agrees with the projection $\operatorname{proj}_{M}e^{t}=(4e-10)+6(3-e)t$ in the facit.)

Kildesett: course=TMA4145 term=host year=2006 problem=4 file=tma4145eksh06en.pdf
