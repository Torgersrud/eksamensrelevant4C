### **Løsning til Oppgave 6**

Det er klart at problemet er symmetrisk, slik at for de angitte indre nodene vil $u_{12}=u_{21}$ og $u_{13}=u_{31}$.

Dermed kan vi sette $u_{11}=X$, $u_{21}=u_{12}=Y$, og $u_{31}=u_{13}=Z$. Fempunktsapproksimasjonen, som her kan skrives

$$\nabla^2(u_c)\approx\frac{u_V+u_N+u_\mathrm{Ø}+u_S-4u_c}{h^2}=0,$$

gir oss skjemaet

$$4u_c=u_V+u_N+u_\mathrm{Ø}+u_S,$$

og følgende tre ligninger

$$4X=2Y,$$

$$4Y=X+20+Z+0,$$

$$4Z=Y+20+10+0,$$

med løsning

$$X=u_{11}=\frac{55}{13}\approx4.23,$$

$$Y=u_{21}=\frac{110}{13}\approx8.46,$$

$$Z=u_{31}=\frac{125}{13}\approx9.62.$$

*Kjeldevarsel: LF løyser 3×3-systemet utan mellomrekningar; verdiane $55/13$, $110/13$ og $125/13$ er her kontrollreikna med sympy og løyser dei tre likningane eksakt. Subskripten $\mathrm{Ø}$ i $u_\mathrm{Ø}$ står for aust (høgre side).*

Kildesett: course=TMA4125 term=var year=2011 problem=6 file=tma4125nbokmaal.pdf
