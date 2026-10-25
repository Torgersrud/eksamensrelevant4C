### **Løsning til Oppgave 5**

Integralligningen kan skrives på formen

$$f(x)-(f*g)(x)=e^{-|x|},\qquad g(x)=e^{-4|x|}.\qquad(*)$$

La så $\hat{f}(w)=\mathcal{F}(f)$. Fourier-transformerer så $(*)$. Det gir

$$\hat{f}(w)-\sqrt{2\pi}\hat{f}(w)\cdot\sqrt{\frac{2}{\pi}}\frac{4}{w^2+16}=\sqrt{\frac{2}{\pi}}\frac{1}{w^2+1},$$

det vil si

$$\left(1-\frac{8}{w^2+16}\right)\hat{f}(w)=\frac{w^2+8}{w^2+16}\hat{f}(w)=\sqrt{\frac{2}{\pi}}\frac{1}{w^2+1}.$$

Altså har vi at

$$\hat{f}(w)=\sqrt{\frac{2}{\pi}}\frac{w^2+16}{(w^2+1)(w^2+8)}.$$

Delbrøkoppspalting gir så

$$
\begin{aligned}
\frac{w^2+16}{(w^2+1)(w^2+8)}&=\frac{1}{w^2+1}+\frac{8}{(w^2+1)(w^2+8)}=\frac{1}{w^2+1}+\frac{8}{7}\left(\frac{1}{w^2+1}-\frac{1}{w^2+8}\right)\\
&=\frac{1}{7}\left(\frac{15}{w^2+1}-\frac{8}{w^2+8}\right).
\end{aligned}
$$

Finner så $f(x)$ ved å ta invers-transformasjonen, det vil si

$$f(x)=\mathcal{F}^{-1}(\hat{f})=\frac{1}{7}\left(15e^{-|x|}-\frac{8}{2\sqrt{2}}e^{-2\sqrt{2}|x|}\right)=\frac{1}{7}\left(15e^{-|x|}-2\sqrt{2}e^{-2\sqrt{2}|x|}\right).$$

Kildesett: course=TMA4135 term=host year=2010 problem=5 file=tma4135_10h.pdf
