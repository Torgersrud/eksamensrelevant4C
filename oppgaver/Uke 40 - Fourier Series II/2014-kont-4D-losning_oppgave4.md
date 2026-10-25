### **Løsning til Oppgave 4**

**a)** I vårt tilfelle er $L=1$ slik at

$$a_0=\frac{1}{2}\int_{-1}^1 f(x)\,\mathrm dx=\frac{1}{2}\int_0^1(1-x)\,\mathrm dx=\frac{1}{4}$$

$$a_k=\int_{-1}^1 f(x)\cos k\pi x\,\mathrm dx=\int_0^1(1-x)\cos k\pi x\,\mathrm dx$$

$$=\underbrace{\left[\frac{1}{k\pi}\sin k\pi x\right]_0^1}_{=0}-\int_0^1 x\cos k\pi x\,\mathrm dx$$

$$=-\Bigl(\underbrace{\left[\frac{x}{k\pi}\sin k\pi x\right]_0^1}_{=0}-\frac{1}{k\pi}\int_0^1\sin k\pi x\,\mathrm dx\Bigr)=\frac{1}{k\pi}\left[-\frac{1}{k\pi}\cos k\pi x\right]_0^1$$

$$=\frac{1}{k^2\pi^2}(1-\cos k\pi)=\begin{cases}2/k^2\pi^2&\text{for }k=1,3,5,\dots\\ 0&\text{for }k=2,4,6,\dots\end{cases}$$

$$b_k=\int_{-1}^1 f(x)\sin k\pi x\,\mathrm dx=\int_0^1(1-x)\sin k\pi x\,\mathrm dx$$

$$=\underbrace{\left[-\frac{1}{k\pi}\cos k\pi x\right]_0^1}_{=(1+(-1)^{k+1})/k\pi}-\int_0^1 x\sin k\pi x\,\mathrm dx$$

$$=\frac{1}{k\pi}(1+(-1)^{k+1})-\Bigl(\underbrace{\left[-\frac{x}{k\pi}\cos k\pi x\right]_0^1}_{=(-1)^{k+1}/k\pi}+\frac{1}{k\pi}\underbrace{\int_0^1\cos k\pi x\,\mathrm dx}_{=0}\Bigr)=\frac{1}{k\pi}\quad\text{for }k=1,2,3,\dots$$

Dermed er fourierrekken til $f$ gitt ved

$$a_0+\sum_{n=1}^\infty(a_n\cos n\pi x+b_n\sin n\pi x)=\frac{1}{4}+\frac{2}{\pi^2}\sum_{n=1}^\infty\frac{\cos(2n-1)\pi x}{(2n-1)^2}+\frac{1}{\pi}\sum_{n=1}^\infty\frac{\sin n\pi x}{n}.$$

**b)** Vi er oppgitt at $f(-1)=f(1)=0$, slik at

$$a_0+\sum_{n=1}^\infty(a_n\cos n\pi+b_n\sin n\pi)=\frac{1}{4}-\frac{2}{\pi^2}\sum_{n=1}^\infty\frac{1}{(2n-1)^2}=f(1)=0,$$

hvor vi har utnyttet at funksjonen er kontinuerlig i $x=1$. Derved er

$$\sum_{n=1}^\infty\frac{1}{(2n-1)^2}=\frac{\pi^2}{8}.$$

Kildesett: course=TMA4135 term=kont year=2014 problem=4 file=tma4135_14k.pdf
