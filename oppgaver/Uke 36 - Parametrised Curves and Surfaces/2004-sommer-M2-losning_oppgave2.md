### **Løsning til Oppgave 2**

**a)** Når $a$ er et tall, er

$$z = 3 + 3ax - 3y$$

ligningen for et plan med normalvektor $\mathbf{N}_1 = [3a, -3, -1]$.

Punktene $(0, 1, 0)$ og $(1, a, 3)$ ligger i planet fordi koordinatene passer i ligningen for planet:

$$0 = 3 + 3a \cdot 0 - 3 \cdot 1, \qquad 3 = 3 + 3a \cdot 1 - 3 \cdot a.$$

Planet står normalt på planet $y = 3z$ med normalvektor $\mathbf{N}_2 = [0, 1, -3]$ dersom $\mathbf{N}_1 \perp \mathbf{N}_2$. Dette holder fordi

$$\mathbf{N}_1 \cdot \mathbf{N}_2 = 3a \cdot 0 - 3 \cdot 1 - 1 \cdot (-3) = 0.$$

**b)** Vi kaller den gitt flaten for $S$. Planet $P$ tangerer flaten $S$ i punktet $(p, q, r)$ hvis og bare hvis:

* $(p, q, r)$ ligger i $P$, det vil si
  $$r = 3 + 3ap - 3q \qquad (1)$$
* $(p, q, r)$ ligger i $S$, det vil si
  $$-36p^2 + 9q^2 + r^2 = 9 \qquad (2)$$
* Normalen til $P$ i $(p, q, r)$ er parallell med normalen til $S$ i $(p, q, r)$, det vil si
  $$\nabla(3 + 3ax - 3y - z) = k \cdot \nabla(-36x^2 + 9y^2 + z^2 - 9)$$
  i punktet $(p, q, r)$. Altså
  $$[3a, -3, -1] = k \cdot [-72p, 18q, 2r]$$

som gir de tre ligningene

$$3a = -72kp \qquad (3)$$
$$-3 = 18kq \qquad (4)$$
$$-1 = 2kr. \qquad (5)$$

Derved har vi 5 ligninger med 5 ukjente: $p$, $q$, $r$, $k$ og $a$. Ved å løse ligningssystemet, finner vi at det har akkurat to løsninger, nemlig

$$p = 1/2, \quad q = 1, \quad r = 3, \quad a = 2, \quad \text{og} \quad k = -1/6$$

$$p = -1/2, \quad q = 1, \quad r = 3, \quad a = -2, \quad \text{og} \quad k = -1/6.$$

Altså tangerer $P$ flaten $S$ dersom $a = 2$ eller $a = -2$.

Kildesett: course=TMA4105 term=sommer year=2004 problem=2 file=tma4105_04k.pdf
