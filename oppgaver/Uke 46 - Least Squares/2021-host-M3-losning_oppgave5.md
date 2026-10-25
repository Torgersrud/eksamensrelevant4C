### **Løsning til Oppgave 5**

**a)** For å finne en ortogonal basis bruker vi Gram–Schmidt. Vi velger vår første basisvektor til å være $\mathbf{u}_1=1$, og beregner den andre til å være

$$\mathbf{u}_2=x-\frac{\langle 1,x\rangle}{\langle 1,1\rangle}1.$$

For å gjøre dette må vi altså beregne de to indreproduktene

$$\langle 1,x\rangle=\int_0^1 1\cdot x\,\,dx=\left[\frac{x^2}{2}\right]_0^1=\frac{1}{2},\qquad \langle 1,1\rangle=\int_0^1 1\cdot 1\,\,dx=[x]_0^1=1.$$

Vi får da en ortogonal basis $\{1,x-\frac{1}{2}\}$.

**b)** For å beregne projeksjonen av $h(x)$ ned på $U$, projiserer vi ned på hver enkelt basisvektor i den ortogonale basisen vår. Altså har vi

$$\operatorname{Proj}_U(h(x))=\frac{\langle 1,h(x)\rangle}{\langle 1,1\rangle}1+\frac{\langle x-\frac{1}{2},h(x)\rangle}{\langle x-\frac{1}{2},x-\frac{1}{2}\rangle}(x-\frac{1}{2}). \tag{1}$$

Vi beregner indreproduktene:

$$\langle 1,h(x)\rangle=\int_0^1 1\cdot e^x\,\,dx=[e^x]_0^1=e-1,$$

$$\langle x-\frac{1}{2},h(x)\rangle=\int_0^1\left(x-\frac{1}{2}\right)e^x\,\,dx=\left[(x-1)e^x-\frac{1}{2}e^x\right]_0^1=\frac{3-e}{2},$$

$$\langle x-\frac{1}{2},x-\frac{1}{2}\rangle=\int_0^1\left(x-\frac{1}{2}\right)^2\,\,dx=\left[\frac{(x-1/2)^3}{3}\right]_0^1=\frac{1}{12}.$$

Puttar vi disse inn i (1) får vi

$$\operatorname{Proj}_U(h(x))=e-1+12\cdot\frac{3-e}{2}\left(x-\frac{1}{2}\right)=(18-6e)x-10+4e.$$

*Kjeldevarsel: den ortogonale basisen $\{1,x-\frac{1}{2}\}$, indreprodukta $e-1$, $\frac{3-e}{2}$, $\frac{1}{12}$ og projeksjonen $(18-6e)x-10+4e$ er kontrollrekna med sympy.*

Kildesett: course=TMA4110 term=host year=2021 problem=5 file=tma4110-eksamen-h21-bokmaal.pdf
