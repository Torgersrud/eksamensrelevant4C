### **Løsning til Oppgave 4**

Evaluate convolution

$$(u(t+1)-u(t-1))*e^{-|t|}$$

and find its Fourier transform.

$$u(t+1)-u(t-1)=\begin{cases}1, & |t|<1\\ 0 & \text{otherwise}\end{cases}$$

Fourier transform:

$$\frac{1}{\sqrt{2\pi}}\int_{-1}^{1}e^{-i\omega t}\,dt=\frac{-1}{\sqrt{2\pi}}\ \frac{e^{-i\omega}-e^{i\omega}}{i\omega}=\sqrt{\frac{2}{\pi}}\ \frac{\sin\omega}{\omega}$$

$$\mathcal{F}\left(e^{-|t|}\right)=\frac{1}{\sqrt{2\pi}}\int\limits_0^{\infty}e^{-(1+i\omega)t}\,dt+\frac{1}{\sqrt{2\pi}}\int\limits_{-\infty}^0e^{(1-i\omega)t}\,dt=I_1+I_2$$

$$I_1=\frac{1}{\sqrt{2\pi}}\ \frac{1}{1+i\omega}\ ;\quad I_2=\frac{1}{\sqrt{2\pi}}\ \frac{1}{1-i\omega}$$

$$I_1+I_2=\frac{1}{\sqrt{2\pi}}\ \frac{1-i\omega+1+i\omega}{1+\omega^2}=\sqrt{\frac{2}{\pi}}\ \frac{1}{1+\omega^2}$$

Fourier transform of the convolution

$$\sqrt{2\pi}\ \frac{2}{\pi}\ \frac{\sin\omega}{\omega}\ \frac{1}{1+\omega^2}=\frac{2\sqrt{2}}{\sqrt{\pi}}\ \frac{\sin\omega}{\omega\left(1+\omega^2\right)}$$

(Continuation)

Denote $f(t)=\left[u(t+1)-u(t-1)\right]*e^{-|t|}=\int_{-1}^{1}e^{-|t-\tau|}\,d\tau$

* $t>1\Rightarrow|t-\tau|=t-\tau$ for all $\tau$, $-1<\tau<1$

$$\Rightarrow f(t)=\int\limits_{-1}^1e^{-(t-\tau)}\,d\tau=e^{-t}\int\limits_{-1}^1e^{\tau}\,d\tau=\left(e-\frac{1}{e}\right)e^{-t}$$

* $t<-1\Rightarrow|t-\tau|=-t+\tau$ for all $\tau$, $-1<\tau<1$

$$\Rightarrow f(t)=\int\limits_{-1}^1e^{t-\tau}\,d\tau=e^{t}\int\limits_{-1}^1e^{-\tau}\,d\tau=\left(e-\frac{1}{e}\right)e^{t}$$

* $-1<t<1\Rightarrow|t-\tau|=\begin{cases}t-\tau, & \tau<t\\ \tau-t, & \tau>t\end{cases}$

$$f(t)=\int\limits_{-1}^te^{-t+\tau}\,d\tau+\int\limits_t^1e^{-\tau+t}\,d\tau$$

$$\int\limits_{-1}^te^{-t+\tau}\,d\tau=e^{-t}\int\limits_{-1}^te^{\tau}\,d\tau=e^{-t}\left(e^{t}-\frac{1}{e}\right)=1-e^{-t-1}$$

$$\int\limits_t^1e^{-\tau+t}\,d\tau=e^{t}\int\limits_t^1e^{-\tau}\,d\tau=e^{t}\left(-\frac{1}{e}+e^{-t}\right)=-e^{t-1}+1$$

$$f(t)=2-\frac{1}{e}\left(e^{t}+e^{-t}\right)$$

Finally write all together:

$$f(t)=\begin{cases}\left(e-e^{-1}\right)e^{-t}, & t\geq 1\\[3pt] 2-e^{-1}\left(e^{t}+e^{-t}\right), & -1<t<1\\[3pt] \left(e-e^{-1}\right)e^{t}, & t\leq -1\end{cases}$$

*Kjeldevarsel: LF er handskriven på engelsk (s. 8–9) og er transkribert ordrett i den rekkjefølgja LF brukar (fouriertransformen først, konvolusjonen som funksjon etterpå); eit overstreka utrekning av fouriertransformen med $2\pi\omega$-frekvens ($\int_{-1}^1e^{-2i\pi\omega t}dt=\frac{-1}{2i\pi\omega}(e^{-2i\pi\omega}-e^{2i\pi\omega})=\frac{\sin 2\pi\omega}{\pi\omega}$) på side 8 er utelaten. Alt er kontrollreikna med sympy: $\frac{1}{\sqrt{2\pi}}\int_{-1}^{1}e^{-i\omega t}dt=\sqrt{\frac{2}{\pi}}\frac{\sin\omega}{\omega}$, $\mathcal{F}(e^{-|t|})=\sqrt{\frac{2}{\pi}}\frac{1}{1+\omega^2}$, og med LF si unitære transformkonvensjon (konvolusjonssetninga $\widehat{f*g}=\sqrt{2\pi}\,\hat f\,\hat g$) blir transformen av konvolusjonen $\frac{2\sqrt 2}{\sqrt\pi}\frac{\sin\omega}{\omega(1+\omega^2)}$; det stykkevist definerte konvolusjonsuttryktet stemmer med direkte integrasjon $\int_{-1}^1e^{-|t-\tau|}d\tau$ i alle punkta og er kontinuerleg i $t=\pm1$.*

Kildesett: course=TMA4125 term=var year=2006 problem=4 file=eksamen-bok_2006v.pdf
