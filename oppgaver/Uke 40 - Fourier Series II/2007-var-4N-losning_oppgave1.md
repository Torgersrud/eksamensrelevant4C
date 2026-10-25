### **Løsning til Oppgave 1**

*Problem 1*

*a.* Let $f(x)$ be a $2\pi$-periodic function such that $f(x)=e^{-2x}$ for $-\pi<x<\pi$. Find the Fourier series of $f$ in the complex form.

*b.* Let $g(x)$ be a $2\pi$-periodic function such that $g(x)=e^{x}$ for $-\pi<x<\pi$. The Fourier series of $g$ has the form

$$g(x)\sim\frac{\sinh\pi}{\pi}\sum_{n=-\infty}^{\infty}\frac{(-1)^{n}}{1-in}\,e^{inx}$$

Find the sum of the series

$$\sum_{n=1}^{\infty}\frac{(-1)^{n}}{1+n^{2}}\quad\text{and}\quad\sum_{n=1}^{\infty}\frac{1}{1+n^{2}}$$

*a.*

$$f(x)\sim\sum_{n=-\infty}^{\infty}c_{n}e^{inx},\quad c_{n}=\frac{1}{2\pi}\int\limits_{-\pi}^{\pi}f(x)e^{-inx}dx$$

In our case

$$c_{n}=\frac{1}{2\pi}\int\limits_{-\pi}^{\pi}e^{-2x}e^{-inx}dx=\frac{1}{2\pi}\int\limits_{-\pi}^{\pi}e^{x(-2-in)}dx=$$

$$=\frac{1}{2\pi}\frac{-1}{2+in}\Bigl[e^{-\pi(2+in)}-e^{\pi(2+in)}\Bigr]=$$

$$=\frac{(-1)^{n}}{2+in}\ \frac{e^{2\pi}-e^{-2\pi}}{2\pi}=\frac{(-1)^{n}}{2+in}\ \frac{\sinh 2\pi}{\pi}$$

$$e^{-2x}\sim\frac{\sinh 2\pi}{\pi}\sum_{n=-\infty}^{\infty}\frac{(-1)^{n}}{2+in}\ e^{inx}$$

*b.*

$$\frac{1}{1-in}=\frac{1+in}{1+n^{2}}\ \Rightarrow$$

$$g(x)\sim\frac{\sinh\pi}{\pi}\sum_{-\infty}^{\infty}(-1)^{n}\ \frac{1+in}{1+n^{2}}\ e^{inx}$$

[Figur: handteikna akselaus utkast av $g$: tre oppadstigande bogar av $e^{x}$-typen med stipla kanter, y-aksen merkt $g$ med merke for $e^{\pi}$ oppe og $e^{-\pi}$ nede, x-aksen merkt $x$, med merke for $1$ og pil høgre.]

$$1=g(0)=\frac{\sinh\pi}{\pi}\sum_{-\infty}^{\infty}(-1)^{n}\ \frac{1+in}{1+n^{2}}=\ \frac{\sinh\pi}{\pi}+$$

$$+\ \frac{2}{\pi}\sinh\pi\sum_{1}^{\infty}(-1)^{n}\ \frac{1}{1+n^{2}}\ \Rightarrow$$

$$\Rightarrow\ \frac{\pi}{2\sinh\pi}-\ \frac{1}{2}\ =\ \sum_{1}^{\infty}(-1)^{n}\ \frac{1}{1+n^{2}}$$

$$\frac{1}{2}\bigl(g(\pi+0)+g(\pi-0)\bigr)=\ \frac{1}{2}\bigl(e^{\pi}+e^{-\pi}\bigr)=\cosh\pi=$$

$$=\ \frac{\sinh\pi}{\pi}\sum_{n=-\infty}^{\infty}\frac{1+in}{1+n^{2}}=\ \frac{\sinh\pi}{\pi}\sum_{n=-\infty}^{\infty}\ \frac{1}{1+n^{2}}=$$

$$=\ \frac{\sinh\pi}{\pi}\ +2\ \frac{\sinh\pi}{\pi}\sum_{1}^{\infty}\ \frac{1}{1+n^{2}}$$

$$\Rightarrow\ \frac{\pi}{2}\ \frac{\cosh\pi}{\sinh\pi}-\ \frac{1}{2}\ =\ \sum_{1}^{\infty}\ \frac{1}{1+n^{2}}$$

*Kjeldevarsel: LF er handskriven på engelsk (s. 7–9 i PDF-en, LF-eigne merke p.1.1–p.1.3) og er transkribert ordrett; overstreka utkast er utelne (eit overstreka svarlinje i 1a, eit overstreka tal i leddet framfor 1-summen, eit viska tal i 1b og ein overstreka $\frac{1}{2}$-faktor framfor $\cosh\pi$ i 1b — $\frac{1}{2}(e^{\pi}+e^{-\pi})=\cosh\pi$), og brøken framfor 1-summen i 1b er skriven om til $\frac{2}{\pi}\sinh\pi$ etter viskinga. Alle tal er kontrollreikna med sympy: $c_{n}=\frac{(-1)^{n}}{2+in}\frac{\sinh 2\pi}{\pi}$ stemmer med direkte integrasjon for $n=0,\pm1,2,5$, $\sum_{1}^{\infty}(-1)^{n}/(1+n^{2})=\frac{\pi}{2\sinh\pi}-\frac{1}{2}$ og $\sum_{1}^{\infty}1/(1+n^{2})=\frac{\pi}{2}\frac{\cosh\pi}{\sinh\pi}-\frac{1}{2}$ er eksakte.*

Kildesett: course=TMA4123 term=var year=2007 problem=1 file=TMA4123_v07.pdf
