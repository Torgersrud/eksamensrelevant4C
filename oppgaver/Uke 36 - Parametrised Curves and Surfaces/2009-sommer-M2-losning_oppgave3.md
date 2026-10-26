### **Løsning til Oppgave 3**

a) Ved Newtons andre lov gjelder det at

$$\mathbf{F} = m\mathbf{a} = m\mathbf{r}''(t), \quad \mathbf{r}(t) = \langle \cos t, \sin t, 2t \rangle$$

langs kurven $C$. Vi har $\mathbf{r}'(t) = \langle -\sin t, \cos t, 2 \rangle$ og $\mathbf{r}''(t) = \langle -\cos t, -\sin t, 0 \rangle = \langle -x, -y, 0 \rangle$. Det følger derfor at $\mathbf{F} = \mathbf{G}$ langs $C$.

Starthastighet $\mathbf{v}(0) = \mathbf{r}'(0) = \langle -\sin 0, \cos 0, 2 \rangle = \langle 0, 1, 2 \rangle$.

b) Av a) ser vi at farten $v(t) = |\mathbf{r}'(t)| = \sqrt{\sin^2 t + \cos^2 t + 2^2} = \sqrt{5}$ er konstant under hele bevegelsen. Kraftfeltet $\mathbf{G}$ gir derfor bare retningsendring. Det vil si, komponenten av $\mathbf{G}$ som gir fartsendring er lik $0$ og komponenten som gir retningsendring er $\mathbf{G}$. (Direkte utregning bekrefter: $\mathbf{G} \cdot \mathbf{T} = \frac{\mathbf{G} \cdot \mathbf{r}'}{|\mathbf{r}'|} = \frac{m(\sin t \cos t - \sin t \cos t + 0)}{\sqrt{5}} = 0$.)

c) Arbeidet er gitt ved

$$W = \int_C \mathbf{G} \cdot d\mathbf{r} = \int_0^{4\pi} m\langle -\cos t, -\sin t, 0 \rangle \cdot \langle -\sin t, \cos t, 2 \rangle \, dt = \int_0^{4\pi} m(\sin t \cos t - \sin t \cos t) \, dt = 0.$$

*Kjeldevarsel: løsningsforslagets «Alternativ løsning» grunngir $\mathbf{G} \cdot \mathbf{T} = 0$ i b) med at «$\mathbf{r}'(t) \perp \mathbf{r}(t)$ for denne bevegelsen» og arbeidet lik null i c) med at «$\mathbf{G} \perp \mathbf{r}$ i hvert punkt på $C$». Begge perpendicularitetene som trykkes, feiler: $\mathbf{r}' \cdot \mathbf{r} = -\sin t \cos t + \sin t \cos t + 2 \cdot 2t = 4t$ og $\mathbf{G} \cdot \mathbf{r} = -m(x^2 + y^2) = -m$. Riktig grunngiving er $\mathbf{G} \cdot \mathbf{r}' = 0$ (jf. utregningen over); svarene er likevel korrekte.*

Kildesett: course=TMA4105 term=sommer year=2009 problem=3 file=tma4105_09k.pdf
