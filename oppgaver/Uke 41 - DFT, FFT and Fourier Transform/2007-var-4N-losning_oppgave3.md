### **Løsning til Oppgave 3**

*Problem 3*

Fourier Transform of $\dfrac{1}{a^{2}+t^{2}}$ is $\dfrac{1}{a}\sqrt{\dfrac{\pi}{2}}\ e^{-a|x|}$. Find $\displaystyle\int_{-\infty}^{0}e^{2x}\cos 3xt\ dx$

We have

$$\frac{1}{\sqrt{2\pi}}\ \frac{1}{a}\sqrt{\frac{\pi}{2}}\int\limits_{-\infty}^{\infty}e^{-a|x|}\ e^{ixt}\ dx=\ \frac{1}{a^{2}+t^{2}}$$

Taking the real part:

$$\frac{1}{2a}\int\limits_{-\infty}^{\infty}e^{-a|x|}\cos xt\ dx=\ \frac{1}{a^{2}+t^{2}}$$

$$\frac{1}{a}\int\limits_{-\infty}^{0}e^{-a|x|}\cos xt\ dx=\ \frac{1}{a}\int\limits_{-\infty}^{0}e^{ax}\cos xt\ dx$$

Let a=2 and replace t by 3t.

We obtain

$$\int\limits_{-\infty}^{0}e^{2x}\cos 3tx\ dx=\ \underline{\frac{2}{4+9t^{2}}}$$

*Kjeldevarsel: LF er handskriven på engelsk (PDF-s. 12, LF-merkt p.3.1) og er transkribert ordrett; overstreka utkast er utelne (eit overstreka ledd før $\cos$ i real part-steget og eit viska teikn i $dx$ i den gjentekne oppgåveteksten), og likskapsteikn med dobbel strek i marginen framfor $\frac{1}{a}\int_{-\infty}^{0}$-steget er teken med som vanleg likskap. LF skriv $\cos xt$ i utleiinga og $\cos 3tx$ i svaret (oppgåva trykte $\cos 3xt$). Svaret er understreka i LF og kontrollreikna med sympy: $\int_{-\infty}^{0}e^{2x}\cos(3tx)\,dx=\frac{2}{4+9t^{2}}$ for $t=0,\ 0.7$ og $-2.3$, og transformasjonsparet $\frac{1}{a^{2}+t^{2}}\leftrightarrow\frac{1}{a}\sqrt{\frac{\pi}{2}}e^{-a|x|}$ er kontrollreikna numerisk.*

Kildesett: course=TMA4123 term=var year=2007 problem=3 file=TMA4123_v07.pdf
