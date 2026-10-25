### **Solution to Problem 3**

Given the function

$$f(x)=\begin{cases}\cos x, & \text{if } |x|\leq 1;\\ 0, & \text{otherwise}.\end{cases}$$

Find the Fourier transform of $f$ and evaluate the integral

$$\int_{-\infty}^{\infty}\frac{\sin 2w}{w}\cos w\ \,dw.$$

*Solution.* We use

$$\cos x=\frac{1}{2}\Bigl(e^{ix}+e^{-ix}\Bigr).$$

Therefore

$$\hat{f}(w)=\frac{1}{\sqrt{2\pi}}\frac{1}{2}\int_{-1}^{1}e^{-ix(w-1)}dx+\frac{1}{\sqrt{2\pi}}\frac{1}{2}\int_{-1}^{1}e^{-ix(w+1)}dx.$$

A direct calculation gives

$$\frac{1}{\sqrt{2\pi}}\frac{1}{2}\int_{-1}^{1}e^{-ix(w-1)}dx=\frac{1}{\sqrt{2\pi}}\ \frac{\sin(w-1)}{w-1} \tag{7}$$

$$\frac{1}{\sqrt{2\pi}}\frac{1}{2}\int_{-1}^{1}e^{-ix(w+1)}dx=\frac{1}{\sqrt{2\pi}}\ \frac{\sin(w+1)}{w+1} \tag{8}$$

Therefore

$$\hat{f}(w)=\underline{\frac{1}{\sqrt{2\pi}}\Bigl(\frac{\sin(w-1)}{w-1}+\frac{\sin(w+1)}{w+1}\Bigr)}.$$

In order to evaluate the integral put $u=w-1$ in (7) (equivalently you may put $u=w+1$ in (8)). You will obtain

$$\frac{1}{\sqrt{2\pi}}\frac{1}{2}\int_{-1}^{1}e^{-ixu}dx=\frac{1}{\sqrt{2\pi}}\ \frac{\sin u}{u}.$$

Inverse Fourier transform yields

$$\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{\sin u}{u}e^{iux}du=\begin{cases}\frac{1}{2}, & \text{if } |x|<1;\\ \frac{1}{4}, & \text{if } |x|=1;\\ 0, & \text{if } |x|>1.\end{cases}$$

In this formula change variables $u=2w$ and put $x=1/2$:

$$\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{\sin 2w}{w}e^{iw}dw=\frac{1}{2}.$$

Take the real part of the both sides and multiply by $2\pi$:

$$\underline{\int_{-\infty}^{\infty}\frac{\sin 2w}{w}\cos w\ \,dw=\pi}.$$

*Kjeldevarsel: LF er på engelsk og er transkribert ordrett, med undertlininga LF brukar på svara bevarte som $\underline{\ \ }$. Attmerkingar: (i) LF omformar oppgåva med $|x|\leq 1$ der eksamensarket har $|x|<1$ — utan betydning for transformen; (ii) «Take the real part of the both sides» er LF si eiga setningsforming. Alt er kontrollreikna med sympy: $\frac{1}{\sqrt{2\pi}}\int_{-1}^{1}\cos x\,e^{-ixw}dx$ stemmer med LF si samansette form i punktprøvar (maks avvik $\sim 10^{-16}$), og $\int_{-\infty}^{\infty}\frac{\sin 2w}{w}\cos w\,dw=\pi$ eksakt (framgangsmåten med $u=2w$ og $x=1/2$ i LF si inverse transformformel er konsistent med stykkefunksjonen).*

Kildesett: course=TMA4130 term=host year=2007 problem=3 file=exam-en_2007.pdf
