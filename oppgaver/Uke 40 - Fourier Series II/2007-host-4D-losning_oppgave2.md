### **Løsning til Oppgave 2**

a)

[Figur: Tannhjulsgraf av den partiske periodiske funksjonen på $[-\pi, 3\pi]$: lineær nedgang frå $(−\pi, 0)$ til toppen $(0, \pi)$, så ned til $(\pi, 0)$, opp att til $(2\pi, \pi)$ og ned til $(3\pi, 0)$. Aksar merka $x$ og $y$, toppunkt merkt $\pi$.]

b) Cosinusrekka er $a_0 + \sum_{n=1}^{\infty} a_n \cos nx$, der $a_0 = \frac{1}{\pi} \int_0^{\pi} (\pi - x) dx$, og $a_n = \frac{2}{\pi} \int_0^{\pi} (\pi - x) \cos nx dx$. Vi finner at $a_0 = \frac{\pi}{2}$, $a_{2n} = 0$, og $a_{2n+1} = \frac{4}{\pi} \frac{1}{(2n+1)^2}$. Siden $f$ er kontinuerlig og har høyre og venstre deriverte overalt, er

$$f(x) = \frac{\pi}{2} + \frac{4}{\pi} \left( \frac{\cos x}{1} + \frac{\cos 3x}{9} + \frac{\cos 5x}{25} + \frac{\cos 7x}{49} + \cdots \right).$$

Setter vi inn for $x = 0$, finner vi at $\sum_{n=0}^{\infty} \frac{1}{(2n+1)^2} = \frac{\pi^2}{8}$.

Kildesett: course=TMA4135 term=host year=2007 problem=2 file=tma4135_07h.pdf
