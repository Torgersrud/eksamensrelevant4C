### **Løsning til Oppgave 5**

**a)** $h_x=\frac{1}{2}(x^2+y^2)^{-1/2}\cdot2x$, og

$$\nabla h=\frac{(x,y)}{\|(x,y)\|}\ ;\quad \nabla h(P^*)=\frac{(1,1)}{\sqrt2}$$

$$D_{\vec a}h=\vec a\cdot\nabla h=0$$

**b)** [Figur: kjegle $z=\sqrt{x^2+y^2}$ med topp i origo, $z$-akse opp og vannrett tverrsnitt tegnet.]

Stigningen er $1$ radielt. Det gir at $\nabla h$ peker radielt og har lengde $1$, jf. at gradientens retning er den retningen stigningen er størst og lengden er lik denne stigningen.

**c)** $h(x,y)=10$ er en sirkel med radius $10$.

[Figur: sirkel med radius $10$ rundt origo, tangentlinjen $L$ i punktet $P^*$, punktet $Q$ på radialen gjennom $P*$'et utenfor sirkelen med avstand $5$ fra $P^*$, og vektoren $\nabla h(Q)$ tegnet i $Q$.]

$\nabla h(Q)$ er normal til linjen og er en enhetsvektor, og $(\nabla h)(Q)\cdot(Q-P)$ er projeksjonen av $Q-P$ på $\nabla h(Q)$'s retning. Denne projeksjonen er $5$ (avstanden fra $Q$ til $L$ langs radialen, $\|Q\|-\|P^*\|=15-10=5$) nettopp når $P$ ligger på $L$.

Kildesett: course=TMA4135 term=host year=2016 problem=5 file=tma4135_16h.pdf
