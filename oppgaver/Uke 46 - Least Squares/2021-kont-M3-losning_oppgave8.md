### **Løsning til Oppgave 8**

**a)** Vi begynner med å regne ut $\langle \sin(x),\cos(x)\rangle$. Ved å bruke $u$-substitusjonen $u=\sin(x)$, $\mathrm{d}u=\cos(x)\,\mathrm{d}x$ får vi

$$\frac{1}{2\pi}\int_0^{2\pi}\sin(x)\cos(x)\,\mathrm{d}x=\frac{1}{2\pi}\int_0^0 u\,\mathrm{d}u=0.$$

Siden de to funksjonene allerede er ortogonale, danner de en ortogonal basis. For å få en ortonormal basis trenger vi kun å skalere dem med lengdene deres. Vi benytter oss av dobbelvinkelformelen

$$\cos(2x)=2\cos^2(x)-1=1-2\sin^2(x),$$

som gir oss $\sin^2(x)=\frac{1}{2}(1-\cos(2x))$ og $\cos^2(x)=\frac{1}{2}(1+\cos(2x))$:

$$\|\cos(x)\|^2=\frac{1}{2\pi}\int_0^{2\pi}\cos^2(x)\,\mathrm{d}x=\frac{1}{4\pi}\int_0^{2\pi}1+\cos(2x)\,\mathrm{d}x=\frac{1}{4\pi}\left[x+\sin(2x)/2\right]_0^{2\pi}=\frac{1}{2}$$

og tilsvarende $\|\sin(x)\|^2=\frac{1}{2}$. Lengdene er begge $1/\sqrt{2}$, og derfor danner

$$\mathbf{u}_1=\sqrt{2}\cos(x)\quad\text{og}\quad\mathbf{u}_2=\sqrt{2}\sin(x)$$

en ortonormal basis for $U$.

**b)** Vi beregner projeksjonen som

$$\frac{\langle x,\cos(x)\rangle}{\|\cos(x)\|^2}\cos(x)+\frac{\langle x,\sin(x)\rangle}{\|\sin(x)\|^2}\sin(x)=\frac{0}{1/2}\cos(x)+\frac{-1}{1/2}\sin(x)=-2\sin(x).$$

**c)** Addisjonsformelen gir

$$\cos(x+\pi/4)=\cos(x)\cos(\pi/4)-\sin(x)\sin(\pi/4).$$

Dette viser at $\cos(x+\pi/4)$ er en lineær kombinasjon av $\cos(x)$ og $\sin(x)$, og

$$\cos(x)\cos(\pi/4)-\sin(x)\sin(\pi/4)=\frac{\cos(x)}{\sqrt{2}}-\frac{\sin(x)}{\sqrt{2}}=\frac{1}{2}\mathbf{u}_1-\frac{1}{2}\mathbf{u}_2$$

skriver det i basis $\mathbf{u}_1$ og $\mathbf{u}_2$ som i (a).

*Kjeldevarsel: indreprodukta $\langle x,\cos x\rangle=0$, $\langle x,\sin x\rangle=-1$ og lengdene $\|\cos x\|^2=\|\sin x\|^2=\frac{1}{2}$ (og dermed projeksjonen $-2\sin x$) er kontrollrekna med sympy.*

Kildesett: course=TMA4110 term=kont year=2021 problem=8 file=eksamen-TMA4110-TMA4115-2021Kont.pdf
