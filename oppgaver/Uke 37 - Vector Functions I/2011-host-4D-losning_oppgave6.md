### **Løsning til Oppgave 6**

With $F$ as the two expression we have $F(\pi/2,0)=(0,\pi-3)$ and

$$J(x,y)=\left(\begin{array}{cc}\cos x-x\sin x&\cos^2 y-\sin^2 y\\ 2\sin x+2x\cos x&\cos y-y\sin y\end{array}\right)$$

so that

$$J(\pi/2,0)=\left(\begin{array}{cc}-\pi/2&1\\ 2&1\end{array}\right)$$

If we invert this we obtain

$$J^{-1}(\pi/2,0)=\frac{1}{\pi/2+2}\left(\begin{array}{cc}-1&1\\ 2&\pi/2\end{array}\right)$$

Therefore the next iteration $(x_1,y_1)$ is given by

$$(x_1,y_1)=(\pi/2,0)-J^{-1}(0,\pi-3)^T=\left(\frac{1}{2}(\pi^2+12)/(\pi+4),-\pi(\pi-3)/(\pi+4)\right)\approx(1.5311,-0.0623).$$

Kildesett: course=TMA4135 term=host year=2011 problem=6 file=tma4135_11h.pdf
