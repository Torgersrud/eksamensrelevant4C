### **Løsning til Oppgave 3**

Skriv $g(x, y) = 3x^2 + y^2 - 6$, så bibetingelsen har formen $g(x, y) = 0$. Lagranges multiplikatormetode gir ligningen $\nabla f = \lambda \nabla g$, altså

$$y = 6\lambda x, \quad x = 2\lambda y.$$

Den siste ligningen gir $\lambda = x/(2y)$. Vi setter det inn i den første og forenkler til $y^2 = 3x^2$. Det setter vi inn i bibetingelsen $3x^2 + y^2 = 6$, forenkler, og får $x^2 = 1$. Dermed må $x = \pm 1$ og $y = \pm\sqrt{3}\,x$, som gir fire kritiske punkter $(1, \sqrt{3})$, $(-1, \sqrt{3})$, $(1, -\sqrt{3})$ og $(-1, -\sqrt{3})$. I disse fire punktene blir verdien av $f(x, y) = xy$ henholdsvis $\sqrt{3}$, $-\sqrt{3}$, $-\sqrt{3}$ og $\sqrt{3}$.

I utledningen dividerte vi med $y$. Men vi ser at $y = 0$ gir $x = 0$, og bibetingelsen $3x^2 + y^2 = 6$ holder ikke. Så det er ikke flere kritiske punkter, og største og minste verdi til $f$ på kurven er derfor $\sqrt{3}$ og $-\sqrt{3}$.

*Alternativt:* Man kan parametrisere kurva $3x^2 + y^2 - 6$ som $x(t) = \sqrt{2}\cos(t)$, $y(t) = \sqrt{6}\sin(t)$ for $0 \le t < 2\pi$. Om $z(t) := f(x(t), y(t)) = 2\sqrt{3}\cos(t)\sin(t)$ får vi $z'(t) = 2\sqrt{3}\cos(2t)$, som har nullpunkter i $t = \pi/4$, $t = 3\pi/4$, $t = 5\pi/4$ og $t = 7\pi/4$. I disse punktene har $z$ verdi henholdsvis $\sqrt{3}$, $-\sqrt{3}$, $\sqrt{3}$ og $-\sqrt{3}$. Altså har $z$, og dermed også $f$, maksimal- og minimalverdi $\sqrt{3}$ og $-\sqrt{3}$.

Kildesett: course=TMA4105 term=var year=2014 problem=3 file=tma4105_14v.pdf
