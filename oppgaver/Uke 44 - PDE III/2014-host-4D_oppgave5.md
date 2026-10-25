### **Oppgave 5**

Vi skal studere den modifiserte varmeledningsligningen

$$\frac{\partial u}{\partial t}(x,t)=\frac{\partial^2u}{\partial x^2}(x,t)-u(x,t)\quad\text{for }0\le x\le 1\text{ og }t\ge 0.\tag{1}$$

**a)** Finn alle ikke-trivielle løsninger av ligning (1) på formen $u(x,t)=F(x)G(t)$ som tilfredsstiller randbetingelsene

$$u(0,t)=0=u(1,t)\tag{2}$$

for alle $t\ge 0$.

**b)** Finn løsningen av ligning (1) som i tillegg til randbetingelsene (2) også tilfredsstiller initialbetingelsen

$$u(x,0)=\sin(\pi x)\cos(\pi x).\tag{3}$$

(Hint: Du kan spare tid ved å bruke trigonometriske identiteter for å omskrive $\sin(\pi x)\cos(\pi x)$.)

**c)** Sett opp et differensskjema med sentraldifferens i rom og fremoverdifferens i tid for numerisk løsning av ligning (1) med randbetingelsene (2) og initialbetingelsen (3). Med skrittlengder $h$ og $k$, kaller vi den numeriske tilnærmingen til $u(ih,jk)$ for $U_{i,j}$.

Bruk skrittlengder $h=1/4$ og $k=1/32$ og regn ut

$$|u(3/4,1/32)-U_{3,1}|.$$

Kildesett: course=TMA4135 term=host year=2014 problem=5 file=tma4135_14h.pdf
