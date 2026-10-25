### **Løsning til Oppgave 5**

**a)** Vi har gitt tre punkter, og generelt vil da polynomet være en parabel, $p_2(x)=a_0+a_1x+a_2x^2$. De oppgitte punktene gir oss systemet

$$a_0+a_10+a_20=1,$$

$$a_0+a_11+a_21=2,$$

$$a_0+a_12+a_24=5,$$

som umiddelbart gir oss $a_0=1$, $a_1=0$, $a_2=1$, med andre ord, $p_2(x)=1+x^2$ (Kan alternativt løses med Lagrange-interpolasjon eller ses direkte).

**b)** Lagrangepolynomet som er 0 i $x=0,1,2$ og 1 i $x=3$, er

$$L(x)=\frac{x(x-1)(x-2)}{3(3-1)(3-2)}=\frac{1}{6}x(x-1)(x-2)\,.$$

Vi kan kombinere $p_2$ og $L_4$ til et nytt polynom, $p_3(x)$, som har verdien 16 for $x=3$. Alle polynomer på formen

$$p_2(x)+cL(x),\ c\in\mathbb{R},$$

går gjennom punktene gitt i (a). Av disse vil spesielt

$$p_3(x)=p_2(x)+\left(16-p_2(3)\right)L(x)$$

også gå gjennom $(3,16)$. Hvis vi setter inn for $p_2$ og $L$, får vi

$$p_3(x)=1+x^2+\left(16-1-9\right)\frac{1}{6}x(x-1)(x-2)=1+2x-2x^2+x^3.$$

*Kjeldevarsel: Trykkfeilen «$L_4$» i setninga om kombinasjonen er bevart ordrett; polynomet er det same $L(x)$ frå punktet over (grad 3, ikkje 4). Alle polynoma er kontrollreikna med sympy: $p_2=1+x^2$ treffer $(0,1),(1,2),(2,5)$, $L(3)=1$ og $L(0)=L(1)=L(2)=0$, og $p_3=1+2x-2x^2+x^3$ treffer i tillegg $(3,16)$ i alle fire nodar.*

Kildesett: course=TMA4125 term=var year=2011 problem=5 file=tma4125nbokmaal.pdf
