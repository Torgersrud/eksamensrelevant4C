### **Oppgave 9**

Vi skal løse varmeligningen

$$u_t=u_{xx},$$

for $0\leq x\leq 1$ og $t\geq 0$ med randkrav

$$u(0,t)=u(1,t)=0$$

og initialkrav

$$u(x,0)=x-x^2$$

Skriv en fullstendig algoritme som løser problemet numerisk med et eksplisitt skjema for $t\in[0,1]$. Bruk skrittlengder $h=1/M$ og $k=1/N$ i henholdsvis $x-$ og $t-$retning.

La $h=0.2$ og $k=0.02$ og finn en approximasjon til løsningen $u(0.4,0.02)$.

Anta at du bruker algoritmen med steglengder $h=k$. Hvordan vil du forvente at den numeriske løsningen oppfører seg over tid? Begrunn svaret.

Kildesett: course=TMA4135 term=kont year=2019 problem=9 file=tma4125-30-35-k19-bm.pdf
