### **Solution to Problem 6**

Since the function $g$ contains only a constant and cosine terms, it is even, that is $g(x)=g(-x)$. Also, the function $h$ only contains sine terms and therefore is odd, that is, $h(-x)=-h(x)$. Finally, we note that

$$g(x)+h(x)=a_0+\sum_{n=1}^{\infty}\left(a_n\cos(nx)+b_n\sin(nx)\right)=f(x)$$

(at all points $x$ where $f$ is continuous), as $a_n$ and $b_n$ are the Fourier coefficients of $f$. In other words,

$$\begin{array}{ll}g(x)+h(x)=e^x&\qquad\text{for all }0<x<\pi,\\ g(x)+h(x)=0&\qquad\text{for all }-\pi<x<0.\end{array}$$

Now the second equation can also be written as

$$g(-x)+h(-x)=0\qquad\text{for all }0<x<\pi.$$

Using the fact that $g(-x)=g(x)$ and $h(-x)=-h(x)$, we thus obtain the system of equations

$$\begin{array}{ll}g(x)+h(x)=e^x&\qquad\text{for all }0<x<\pi,\\ g(x)-h(x)=0&\qquad\text{for all }0<x<\pi.\end{array}$$

Solving this system for $g(x)$ and $h(x)$ yields

$$g(x)=h(x)=\frac{1}{2}e^x\qquad\text{for all }0<x<\pi.$$

Since $g$ is even and $h$ is odd, this means that

$$g(x)=\begin{cases}\frac{1}{2}e^x&\text{for }0<x<\pi,\\[4pt] \frac{1}{2}e^{-x}&\text{for }-\pi<x<0,\end{cases}$$

and

$$h(x)=\begin{cases}\frac{1}{2}e^x&\text{for }0<x<\pi,\\[4pt] -\frac{1}{2}e^{-x}&\text{for }-\pi<x<0.\end{cases}$$

In particular, we obtain

$$g(-\pi/2)=g(\pi/2)=\frac{1}{2}e^{\pi/2}$$

and

$$h(-\pi/2)=-\frac{1}{2}e^{\pi/2}\qquad\text{and}\qquad h(\pi/2)=\frac{1}{2}e^{\pi/2}\,.$$

At the point $0$, the functions $g$ and $h$ are equal to the means of their left-hand and right-hand limits, respectively. Therefore

$$g(0)=\frac{1}{2}\Bigl(g(0-0)+g(0+0)\Bigr)=\frac{1}{2}\left(e^{-0}+e^{0}\right)=1$$

and

$$h(x)=\frac{1}{2}\Bigl(h(0-0)+h(0+0)\Bigr)=\frac{1}{2}\left(-e^{-0}+e^{0}\right)=0.$$

*Kjeldevarsel: i det utgitte steget for $g(0)$ er grensene sette inn som $e^{-0}$ og $e^{0}$, men venstre- og høgre grense for $g$ i $0$ er $\frac{1}{2}e^{-0}$ og $\frac{1}{2}e^{0}$, slik at $g(0)=\frac{1}{2}$ (kontrollrekna: $a_0+\sum a_n=\frac{1}{2}(f(0+)+f(0-))=\frac{1}{2}$). Uttrykket $h(x)=$ i den siste linja bør lese $h(0)=$. Teksten over fylgjer fasiten som det står.*

Kildesett: course=TMA4125 term=kont year=2016 problem=6 file=english.pdf
