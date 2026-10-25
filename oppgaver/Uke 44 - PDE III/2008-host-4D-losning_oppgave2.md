### **Løsning til Oppgave 2**

a)

[Figur: Tannhjulsgraf for den partiske periodiske funksjonen med periode 4, vist for $-2 < x < 6$: nedgåande linjestykke med null i $x = \pm 1$, topp med verdi $1$ ved $x = 0$ og $x = 4$, botn med verdi $-1$ ved $x = 2$ og $x = 6$. x-aksen merkt $-2$, $0$, $2$, $4$, $6$.]

Cosinusrekka til $f$ blir av Formen

$$f(x) = a_0 + \sum_{n=0}^{\infty} a_n \cos n\frac{\pi}{2} x.$$

Vi har $a_0 = 0$, og $a_n = \int_0^2 f(x) \cos n\frac{\pi}{2} x \, dx$. En gang delvisintegrasjon viser at

$$a_n = \begin{cases} 0 & \text{for} \quad n \text{ like}, \\ \frac{8}{\pi^2} \frac{1}{n^2} & \text{for} \quad n \text{ odde}. \end{cases}$$

b) Et standard argument, viser at løsningen kan skrives som

$$u(x,t) = A_0 + \sum_{n=1}^{\infty} A_n e^{-(n\frac{\pi}{2})^2 t} \cos n\frac{\pi}{2} x.$$

Vi får oppfylt initialbetingelsen ved å velge $A_n = a_n$ som i punkt a). Altså er

$$u(x,t) = \frac{8}{\pi^2} \sum_{k=0}^{\infty} \frac{1}{(2k+1)^2} e^{-((2k+1)\frac{\pi}{2})^2 t} \cos(2k+1)\frac{\pi}{2} x.$$

Kildesett: course=TMA4135 term=host year=2008 problem=2 file=tma4135_08h.pdf
