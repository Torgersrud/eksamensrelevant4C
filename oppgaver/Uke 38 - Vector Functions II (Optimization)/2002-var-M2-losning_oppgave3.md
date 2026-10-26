### **Løsning til Oppgave 3**

Lagranges metode med den gitte funksjonen og føringen $g(x, y) = \frac{1}{4}x^2 + y^2 - 1 = 0$ leder til ligningene

$$y = \tfrac{1}{2}\lambda x, \quad x = 2\lambda y, \quad \tfrac{1}{4}x^2 + y^2 = 1.$$

Da må $x \neq 0$ og $y \neq 0$, for om én av de to er null, er også den andre det (ved en av de to første ligningene), men da kan ikke den tredje ligningen holde. Vi kan løse de to første ligningene med hensyn på $\lambda$, og får henholdsvis $\lambda = 2y/x$ og $\lambda = x/(2y)$. Så $2y/x = x/(2y)$, og opprydding gir $x^2 = 4y^2$. Vi setter det inn i den tredje ligningen og får $y^2 + y^2 = 1$, altså $y = \pm\sqrt{\frac{1}{2}}$. Vi ender med fire mulige ekstrempunkter for $f$ på ellipsen:

$$\left( \pm\sqrt{2},\, \pm\frac{1}{\sqrt{2}} \right)$$

der alle fire kombinasjoner av de to fortegnene $\pm$ forekommer.

For å komme videre er det greiest å bestemme funksjonen $f$ så langt vi kan. Mange vil nok med én gang se at $f(x, y) = xy$ har de gitte partiellderiverte, så vi vet at $f(x, y) = xy + C$. (Eventuelt kan man bruke metoden fra alternativ 2 i løsningen av oppgave 5.) Dette setter vi inn i de fire punktene:

$$f\big(\sqrt{2}, 1/\sqrt{2}\big) = f\big(-\sqrt{2}, -1/\sqrt{2}\big) = 1 + C, \quad f\big(\sqrt{2}, -1/\sqrt{2}\big) = f\big(-\sqrt{2}, 1/\sqrt{2}\big) = -1 + C$$

og de varmeste punktene er derfor

$$\pm\Big(\sqrt{2},\, \frac{1}{\sqrt{2}}\Big).$$

Kildesett: course=SIF5005 term=var year=2002 problem=3 file=sif5005_02v.pdf
