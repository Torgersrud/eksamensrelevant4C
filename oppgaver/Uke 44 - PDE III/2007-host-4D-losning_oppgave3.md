### **Løsning til Oppgave 3**

a) Ved å sette inn $u(x,t) = F(x)G(t)$ får vi to ligninger

$$F'' = kF$$
$$G' = kG$$

med randkravene $F'(0) = F'(\pi) = 0$.

Dette gir $k = -n^2$, for $n = 0, 1, 2, \ldots$ og funksjonene blir $u_0(x,t) = 1$ og $u_n(x,t) = e^{-n^2 t} \cos nx$ for $n = 1, 2, \ldots$.

b) Ved hjelp av resultatet fra oppgave 2b) finner vi

$$u(x,t) = \frac{\pi}{2} + \frac{4}{\pi} \left( \frac{e^{-t} \cos x}{1} + \frac{e^{-9t} \cos 3x}{9} + \frac{e^{-25t} \cos 5x}{25} + \frac{e^{-49t} \cos 7x}{49} + \cdots \right).$$

Kildesett: course=TMA4135 term=host year=2007 problem=3 file=tma4135_07h.pdf
