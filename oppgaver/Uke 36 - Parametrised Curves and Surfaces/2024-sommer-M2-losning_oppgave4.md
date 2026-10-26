### **Løsning til Oppgave 4**

La $z_1 = \sqrt{3 - x^2 - y^2}$ og $z_2 = (x^2 + y^2)/2$. For å finne en parametrisering av skjæringskurven $C$ mellom flatene gitt ved $z_1$ og $z_2$ ser vi på

$$z_1 = z_2 \iff \sqrt{3 - x^2 - y^2} = \frac{1}{2}(x^2 + y^2).$$

Ved å kvadrere begge sider av den siste ligningen får vi

$$3 - x^2 - y^2 = \frac{1}{4}\bigl(x^2 + y^2\bigr)^2$$

$$12 - 4x^2 - 4y^2 = x^4 + 2x^2y^2 + y^4$$

$$12 = x^4 + 4x^2 + 2x^2y^2 + 4y^2 + y^4$$

$$12 = \bigl(x^2 + y^2\bigr)^2 + 4\bigl(x^2 + y^2\bigr).$$

La så $u = x^2 + y^2$ slik at

$$u^2 + 4u - 12 = (u + 6)(u - 2) = 0$$

som gir at $u = 2$ ($u$ kan ikke være lik $-6$ i og med at $u = x^2 + y^2$ er alltid større eller lik 0). Altså er projeksjonen av $C$ i $xy$-planet gitt ved

$$x^2 + y^2 = 2.$$

Legg merke til at når $x^2 + y^2 = 2$ så er $z_1 = z_2 = 1$.

En parametrisering av $C$ er så gitt ved

$$\mathbf{r}(t) = \bigl(\sqrt{2}\cos(t), \, \sqrt{2}\sin(t), \, 1\bigr)$$

for $0 \leqslant t \leqslant 2\pi$.

Kildesett: course=TMA4105 term=sommer year=2024 problem=4 file=tma4105_2024k.pdf
