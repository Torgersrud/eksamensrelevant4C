### **Løysing til Oppgave 4**

Vi bruker polynominterpolasjon. Funksjonen $D(T)$ kan tilnærmast med Lagrange-polynomet

$$D(T)\approx p_3(T)=12.8\frac{(T-10)(T-15)(T-20)}{(5-10)(5-15)(5-20)}+11.33\frac{(T-5)(T-15)(T-20)}{(10-5)(10-15)(10-20)}$$
$$+\;10.15\frac{(T-5)(T-10)(T-20)}{(15-5)(15-10)(15-20)}+9.17\frac{(T-5)(T-10)(T-15)}{(20-5)(20-10)(20-15)}$$

og

$$D(13)\approx p_3(13)=-12.8\frac{42}{750}+11.33\frac{112}{250}+10.15\frac{168}{250}-9.17\frac{48}{750}=10.59.$$

Så $D(13\;\mathrm{{}}^\circ\mathrm{C})\approx 10.59\ \mathrm{mg/l}$.

Kildesett: course=TMA4125 term=kont year=2006 problem=4 file=TMA4125-30-2006-k.pdf
