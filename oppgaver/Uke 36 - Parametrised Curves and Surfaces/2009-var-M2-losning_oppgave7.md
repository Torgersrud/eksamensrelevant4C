### **Løsning til Oppgave 7**

a) Med $\mathbf{r} = t\mathbf{i} + (2/3) t^{3/2} \mathbf{j}$, gir utregning at

$$\mathbf{v} = \mathbf{i} + \sqrt{t} \, \mathbf{j}, \qquad |\mathbf{v}| = \sqrt{1 + t},$$

$$\mathbf{T} = \frac{\mathbf{i} + \sqrt{t} \, \mathbf{j}}{\sqrt{1 + t}}, \qquad \frac{d\mathbf{T}}{dt} = \frac{-\sqrt{t} \, \mathbf{i} + \mathbf{j}}{2\sqrt{t} (1 + t)^{3/2}}, \qquad \left| \frac{d\mathbf{T}}{dt} \right| = \frac{1}{2\sqrt{t} (1 + t)},$$

$$\mathbf{N} = \frac{\frac{d\mathbf{T}}{dt}}{\left| \frac{d\mathbf{T}}{dt} \right|} = \frac{-\sqrt{t} \, \mathbf{i} + \mathbf{j}}{\sqrt{1 + t}}, \qquad \kappa = \left| \frac{d\mathbf{T}}{ds} \right| = \left| \frac{d\mathbf{T}}{dt} \frac{dt}{ds} \right| = \frac{\left| \frac{d\mathbf{T}}{dt} \right|}{\frac{ds}{dt}} = \frac{\left| \frac{d\mathbf{T}}{dt} \right|}{|\mathbf{v}|} = \frac{1}{2\sqrt{t} (1 + t)^{3/2}}.$$

b) Vi må først finne ut hvor partikkelen er ved tiden $t = 7/3$ s. I løpet av $7/3$ s beveger partikkelen seg en avstand $s = vt = 2(7/3) = 14/3$ m fra origo, men denne avstanden måles langs $y = (2/3) x^{3/2}$, så vi må vite hvordan vi regner ut lengder langs denne kurven. Til det kan vi bruke parametriseringen fra punkt (a), men vi kaller parameteren $\tau$ istedenfor $t$, siden $t$ nå betegner tiden. Da blir lengden fra origo ($\tau = 0$) til et punkt med parameterverdi $\tau = b$:

$$s(b) = \int_0^b |\mathbf{v}(\tau)| \, d\tau = \int_0^b \sqrt{1 + \tau} \, d\tau = \frac{2}{3} (1 + b)^{3/2} - \frac{2}{3}.$$

Ligningen $s(b) = 14/3$ gir $b = 3$, så partikkelen er i punktet $x = 3$, $y = (2/3) 3^{3/2}$, og fra punkt (a) har vi der (parameterverdi $\tau = 3$)

$$\mathbf{N} = \frac{-\sqrt{3} \, \mathbf{i} + \mathbf{j}}{\sqrt{1 + 3}} = \frac{-\sqrt{3} \, \mathbf{i} + \mathbf{j}}{2}, \qquad \kappa = \frac{1}{2\sqrt{3} (1 + 3)^{3/2}} = \frac{1}{2\sqrt{3} \cdot 2^3} = \frac{1}{16\sqrt{3}}.$$

Videre er farten konstant lik $v = 2$ m/s, så akselerasjonen er

$$\mathbf{a} = \kappa v^2 \mathbf{N} = \frac{1}{16\sqrt{3}} \cdot 2^2 \cdot \frac{-\sqrt{3} \, \mathbf{i} + \mathbf{j}}{2} = \frac{-\sqrt{3} \, \mathbf{i} + \mathbf{j}}{8\sqrt{3}}.$$

Kildesett: course=TMA4105 term=var year=2009 problem=7 file=tma4105_09v.pdf
