### **Løsning til Oppgave 3**

a) Vi setter $U(w,t) = \mathcal{F}(u)(w,t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-ixw} u(x,t) dx$. Fouriertransformerer vi ligningen blir den transformerte

$$U_t = -w^2 U - U = -(w^2 + 1)U.$$

Dette er en første ordens ordinær differensialligning, og den generelle losningen er

$$U(w,t) = A(w) e^{-(w^2 + 1)t}.$$

Ved å sette inn for $t = 0$ ser vi at $A(w) = U(w,0)$.

b) Initialbetingelsen gir $U(w,0) = \mathcal{F}(e^{-\frac{1}{2}x^2})(w) = e^{-\frac{1}{2}w^2}$. Fra punkt a) får vi derfor at

$$U(w,t) = e^{-\frac{1}{2}w^2} e^{-(w^2 + 1)t} = e^{-t} e^{-\left(t + \frac{1}{2}\right)w^2}.$$

Den inverse Fouriertransformen gir oss

$$u(x,t) = \frac{e^{\left(\frac{x^2}{4t+2} - t\right)}}{\sqrt{2t+1}}.$$

**Kjeldevarsel:** Eksponenten i svaret er trykt med feil forteikn på $x^2$-leddet. Det rette svaret er

$$u(x,t) = \frac{1}{\sqrt{2t+1}}\, e^{-\left(t + \frac{x^2}{4t+2}\right)}$$

Med pluss framfor $x^2$-leddet, som i kjelda, veks uttrykket i $x$ og løyser ikkje $u_t = u_{xx} - u$ (verifisert ved symbolsk rekning).

Kildesett: course=TMA4135 term=kont year=2006 problem=3 file=tma4135_06k.pdf
