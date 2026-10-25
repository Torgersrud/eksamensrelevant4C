### **Oppgave 5**

I et anisotropt materiale der varmekonduktivitet i $y$-retningen er to ganger høyere enn i $x$-retningen tar den stasjonære varmeligningen formen

$$u_{xx}+2u_{yy}=0.\tag{1}$$

Vi vil løse (1) numerisk. Området er et kvadrat med sidelengde 1 og randbetingelser er gitt ved

$$u(x,0)=u(0,y)=0$$
$$u(x,1)=u(1,y)=1$$

for $x,y$ i $[0,1]$. Vi betrakter det følgende gitteret

[Figur: Et kvadratisk gitter med $4\times 4$ noder $U_{i,j}$, $i,j=0,1,2,3$, merkt fra $U_{0,0}$ nederst til venstre til $U_{3,3}$ øverst til høyre. De fire indre nodene $U_{1,1}$, $U_{2,1}$, $U_{1,2}$, $U_{2,2}$ er teikna som fylte punkt; alle randnodene er opne sirklar.]

der $h=\frac{1}{3}$ og $U_{i,j}\approx u(ih,jh)$.

**a)** Vis at differenseskjemaet som tilsvarer (1) er

$$U_{i+1,j}+U_{i-1,j}+2U_{i,j+1}+2U_{i,j-1}-6U_{i,j}=0.$$

**b)** Sett opp systemet som $U_{i,j}$ ($i,j=1,2$) tilfredsstiller og gjør et steg ved hjelp av Gauss Seidel iterasjon med startpunktet $U_{1,1}^0=U_{2,1}^0=U_{1,2}^0=U_{2,2}^0=\frac{1}{2}$.

Kildesett: course=TMA4130 term=host year=2006 problem=5 file=eksamen-bok_2006.pdf
