### **Løsning til Oppgave 3**

a) Vi setter $u(x, t) = F(x)G(t)$ inn i ligning (1). Da får vi

$$F''G = FG'.$$

Deler vi med $FG$ får vi

$$\frac{F''(x)}{F(x)} = \frac{G'(t)}{G(t)}.$$

Siden $x$ og $t$ er frie variable må begge sider være en og samme konstant, altså

$$F''(x) = kF(x) \quad \text{og} \quad G'(t) = kG(t).$$

Løser vi disse ligningene og setter inn randbetingelsene får vi ikke-trivielle løsninger kun når $k = -p^2$ og $\sin(2p) = 0$, som viser at vi må ha $p = n\frac{\pi}{2}$ for $n = 1, 2, 3, \ldots$. Løsningene blir opp til multiplikasjon med en konstant,

$$u_n(x, t) = e^{-(n\frac{\pi}{2})^2 t} \sin\left(n\frac{\pi}{2}x\right).$$

b) Siden ligningen og randbetingelsene er lineære og homogene kan vi bruke superposisjonsprinsippet. Det vil si at en lineær kombinasjon

$$u(x, t) = \sum_{n=1}^{N} b_n e^{-(n\frac{\pi}{2})^2 t} \sin\left(n\frac{\pi}{2}x\right)$$

er løsning av (1) og (2). Setter vi $t = 0$ og sammenligner med initialbetingelsen (3) får vi

$$u(x, 0) = \sum_{n=1}^{N} b_n \sin\left(n\frac{\pi}{2}x\right) = \sin\left(\frac{\pi}{2}x\right) + 5\sin\left(5\frac{\pi}{2}x\right).$$

Dette viser at $b_n = 0$ unntatt for $n = 1$ og $n = 5$, og at

$$u(x, t) = e^{-(\frac{\pi}{2})^2 t} \sin\left(\frac{\pi}{2}x\right) + 5e^{-(5\frac{\pi}{2})^2 t} \sin\left(5\frac{\pi}{2}x\right).$$

Kildesett: course=TMA4135 term=host year=2009 problem=3 file=tma4135_09h.pdf
