### **Oppgave 5**

Betrakt den partielle differensialligningen

$$\frac{\partial^2 u}{\partial x^2}(x,t)+4u(x,t)=\frac{\partial u}{\partial t}(x,t) \qquad (2)$$

for $0\le x\le\pi$ og $t\ge 0$.

**a)** Finn alle ikke-trivielle løsninger av ligning (2) på formen $u(x,t)=F(x)G(t)$ som tilfredsstiller randbetingelsene

$$u(0,t)=\frac{\partial u}{\partial x}(\pi,t)=0$$

for alle $t\ge 0$.

**b)** Finn en løsning av ligning (2) som i tillegg til randbetingelsene fra 5a også tilfredsstiller initialbetingelsen

$$u(x,0)=\sin\left(\frac{3}{2}x\right)+2\sin\left(\frac{5}{2}x\right)+3\sin\left(\frac{7}{2}x\right)$$

for alle $0\le x\le\pi$.

**c)** Utled Crank–Nicolsons metode for numerisk løsning av ligning (2) med (de nye) randbetingelsene

$$u(0,t)=u(\pi,t)=0$$

for alle $t\ge 0$. Skriv $h$ for steglengden i rom. Angi matriseformen til det lineære ligningssystemet som må løses for å gjøre et tidsskritt av lengde $k$. (Du trenger ikke å løse ligningssystemet!)

Kildesett: course=TMA4135 term=host year=2015 problem=5 file=tma4135_15h.pdf
