### **Løsning til Oppgave 2**

a) Vi setter inn $u(x, t) = F(x)G(t)$ i ligningen og får $G'F = 4F''G$. Ved å dele med $4FG$ får $\frac{G'}{4G} = \frac{F''}{F}$, og vi har separert variablene $x$ og $t$. Denne ligningen holder bare dersom $\frac{F''}{F} = k$ der $k$ er en konstant. For å få tilfredsstilt randbetingelsen må $k = -(\pi n)^2$ for $n = 1, 2, 3, \ldots$. For et gitt naturlig tall $n$ har vi da

$$F_n'' = -(\pi n)^2 F_n \qquad \text{og} \qquad G_n' = -(2\pi n)^2 G_n.$$

Løsningene er

$$u_n(x, t) = B_n e^{-(2\pi n)^2 t} \sin n\pi x$$

for vilkårlige heltall $n$ og vilkårlige konstanter $B_n$.

b) Superposisjonsprinsippet visere at løsningen av ligningen som tilfredstilller både randbetingelsen og initialbetingelsen er

$$u(x, t) = e^{-(2\pi)^2 t} \sin \pi x + \frac{1}{3} e^{-(6\pi)^2 t} \sin 3\pi x.$$

Kildesett: course=TMA4135 term=kont year=2008 problem=2 file=tma4135_08k.pdf
