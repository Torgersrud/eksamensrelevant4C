### **Oppgave 6**

Vi skal løse diffusjonsligningen med et kildeledd, gitt ved

$$u_t = u_{xx} + x, \qquad 0 \leq x \leq 1, \qquad t \geq 0,$$

med randbetingelsene

$$u(0,t) = 1, \qquad u(1,t) = 0, \qquad t \geq 0$$

og startbetingelsen

$$u(x,0) = 1 - x, \qquad 0 \leq x \leq 1.$$

La $h$ være skrittlengden i $x$-retningen og $k$ i $t$-retningen, og formuler en eksplisitt metode som gir tilnærmelse til løsningen $u(x,t)$ i punktene $(x_i, t_j)$ der $x_i = ih$ og $t_j = jk$.

La $h = 0.25$, $k = 0.01$, og bruk metoden til å finne tilnærmelser til $u(0.25, 0.01)$, $u(0.5, 0.01)$ og $u(0.75, 0.01)$.

Kildesett: course=TMA4125 term=kont year=2006 problem=6 file=TMA4125-30-2006-k.pdf
