### **Solution to Problem 3**

(Problem 2 for Math 4M) Since $|x|=-x$ when $x<0$ and $|x|=x$ otherwise, we have

$$\hat{f}(w)=\frac{1}{\sqrt{2\pi}}\left[\int_{-\infty}^{0}xe^{(a-iw)x}\,dx+\int_{0}^{\infty}xe^{-(a+iw)x}\,dx\right]\equiv\frac{1}{\sqrt{2\pi}}(I_{1}+I_{2}).$$

Using integration by parts, we get:

$$I_{1}=\left.\frac{xe^{(a-iw)x}}{a-iw}\right|_{x=-\infty}^{0}-\frac{1}{a-iw}\int_{-\infty}^{0}e^{(a-iw)x}\,dx$$

$$=\left.\frac{xe^{(a-iw)x}}{a-iw}\right|_{x=-\infty}^{0}-\left.\frac{e^{(a-iw)x}}{(a-iw)^{2}}\right|_{x=-\infty}^{0}$$

$$=\lim_{t\to\infty}\left[-\frac{(-t)e^{-at}e^{iwt}}{a-iw}-\frac{1}{(a-iw)^{2}}+\frac{e^{-at}e^{iwt}}{(a-iw)^{2}}\right].$$

Since it is given that $a>0$, and $e^{iwt}$ is bounded for all $t$, the third term above converges to 0. Furthermore, we know that $t^{p}e^{-at}\to 0$, for any power $p$, as $t\to\infty$. Hence, the first term above converges to 0. Thus $I_{1}=-1/(a-iw)^{2}$.

In a similar way, the calculation of $I_{2}$ proceeds as follows:

$$I_{2}=\left.-\frac{xe^{-(a+iw)x}}{a+iw}\right|_{x=0}^{\infty}+\frac{1}{a+iw}\int_{0}^{\infty}e^{-(a+iw)x}\,dx$$

$$=\left.-\frac{xe^{-(a+iw)x}}{a+iw}\right|_{x=0}^{\infty}-\left.\frac{e^{-(a+iw)x}}{(a+iw)^{2}}\right|_{x=0}^{\infty}$$

$$=\lim_{t\to\infty}\left[-\frac{te^{-at}e^{-iwt}}{a+iw}+\frac{1}{(a+iw)^{2}}-\frac{e^{-at}e^{-iwt}}{(a+iw)^{2}}\right].$$

By exactly the same arguments as above to justify the limits, we get $I_{2}=1/(a+iw)^{2}$. Combining the values of $I_{1}$ and $I_{2}$, we get

$$\hat{f}(w)=\frac{1}{\sqrt{2\pi}}\left[-\frac{1}{(a-iw)^{2}}+\frac{1}{(a+iw)^{2}}\right]$$

$$=-\frac{4iaw}{\sqrt{2\pi}(a^{2}+w^{2})^{2}}.\qquad(2)$$

To evaluate the given integral, we use the Fourier-inversion formula. By (2), have:

$$f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{-4iaw}{(a^{2}+w^{2})^{2}}e^{iwx}\,dw$$

$$=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{-4iaw(\cos(wx)+i\sin(wx))}{(a^{2}+w^{2})^{2}}\,dw.$$

Since $f(x)$ is real-valued, the imaginary part on the right-hand side of the above equation must equal zero. Hence

$$f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{4aw\sin(wx)}{(a^{2}+w^{2})^{2}}\,dw\ \ \forall x\in\mathbb{R}.$$

The above holds true for each $x\in\mathbb{R}$ because $f$ is a continuous function and, as $a>0$, satisfies all the conditions of the theorem that gives us the Fourier-inversion formula. Taking $x=1$ and $a=1$ in the last equations gives us the answer:

$$\int_{-\infty}^{\infty}\frac{w(\sin(w)}{(1+w^{2})^{2}}\,dw=\left.\frac{\pi}{2}\,e^{-|x|}\right|_{x=1}=\frac{\pi e^{-1}}{2}.$$

*Kjeldevarsel: Eksamen-PDF-en for dette haustsettet blei aldri publisert; løysingsfila `solutions_2012h.pdf` er difor Kildesett, og oppgåveteksten er ikkje gjenteken i løysinga. I svaret er leddet trykt som $\frac{w(\sin(w)}{(1+w^2)^2}$ med ein overskotig open parentes, og verdien er generell oppgjeven som $\frac{\pi}{2}e^{-|x|}$ utan faktoren $x$ — etter inversjonsformelen over er det rette $\frac{\pi}{2}x\,e^{-|x|}$ (sympy-stadfesta); innsettinga $x=1$ gir same talverdi, så svaret $\pi e^{-1}/2$ er rett. Også setninga «By (2), have:» manglar «we» i kjelda — alt bevart ordrett.*

Kildesett: course=TMA4130 term=host year=2012 problem=3 file=solutions_2012h.pdf
