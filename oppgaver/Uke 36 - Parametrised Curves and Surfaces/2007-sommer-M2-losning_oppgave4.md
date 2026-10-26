### **Løsning til Oppgave 4**

Vi deriverer og får

$$\mathbf{r}'(t) = 3(\cos^2 t - \sin^2 t) \, \mathbf{i} + 3(2 \cos t \sin t) \, \mathbf{j} = 3 \cos 2t \, \mathbf{i} + 3 \sin 2t \, \mathbf{j}.$$

Farta blir

$$|\mathbf{r}'(t)| = 3 \sqrt{(\cos^2 t - \sin^2 t)^2 + (2 \cos t \sin t)^2} = 3 \sqrt{(\cos^2 t + \sin^2 t)^2} = 3.$$

Enhetstangenten blir da

$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{|\mathbf{r}'(t)|} = \frac{\mathbf{r}'(t)}{3} = \cos 2t \, \mathbf{i} + \sin 2t \, \mathbf{j}.$$

Den prinsipale normalvektoren er

$$\mathbf{N}(t) = \frac{\mathbf{T}'(t)}{|\mathbf{T}'(t)|} = \frac{\mathbf{T}'(t)}{2} = -\sin 2t \, \mathbf{i} + \cos 2t \, \mathbf{j}.$$

Krumningen $\kappa(t)$ er definert som $\left| \dfrac{d\mathbf{T}}{ds} \right|$. Kjerneregelen gir

$$\frac{d\mathbf{T}}{dt} = \frac{d\mathbf{T}}{ds} \frac{ds}{dt} = \frac{d\mathbf{T}}{ds} \, |\mathbf{r}'(t)| = 3 \, \frac{d\mathbf{T}}{ds},$$

som gir $\dfrac{d\mathbf{T}}{ds} = \dfrac{1}{3} \dfrac{d\mathbf{T}}{dt}$, og dermed

$$\kappa(t) = \left| \frac{d\mathbf{T}}{ds} \right| = \frac{1}{3} \left| \frac{d\mathbf{T}}{dt} \right| = \frac{1}{3} \left| \langle -2 \sin 2t, \; 2 \cos 2t, \; 0 \rangle \right| = \frac{2}{3}.$$

Lengden av $C$ er

$$\int_0^{\pi} ds = \int_0^{\pi} |\mathbf{r}'(t)| \, dt = \int_0^{\pi} 3 \, dt = 3\pi.$$

Siden krumningen $\kappa(t) = 2/3$ er konstant og definert for alle $t$, må kurven være en del av en sirkelbue med radius $\rho = 1/\kappa = 3/2$. Siden lengden er $3\pi = 2\pi\rho$, må kurven være en hel sirkel, og sentrum er gitt ved

$$\mathbf{r}(t) + \rho \, \mathbf{N}(t) = \langle 0, \; 3/2 \rangle.$$

(Det stemmer også direkte: $x(t) = \tfrac{3}{2} \sin 2t$, $y(t) = \tfrac{3}{2}(1 - \cos 2t)$, som er sirkelen $x^2 + (y - 3/2)^2 = (3/2)^2$ gjennomløpt én gang når $t$ går fra $0$ til $\pi$.)

Kildesett: course=TMA4105 term=sommer year=2007 problem=4 file=tma4105_07k.pdf
