### **Løsning til Oppgave 1**

Sidan hyperboloiden ikkje har nokre randpunkt, held det å sjekka dei kritiske punkta med hjelp av lagrangemultiplikatorar. Lèt

$$f(x, y, z) = z^2 + 2xy + 1, \qquad g(x, y, z) = x^2 + y^2 + z^2,$$

skal me då finna punkta $(x, y, z)$ der $f(x, y, z) = 0$ og $\nabla f = \lambda \nabla g$. Me har

$$\nabla f = (2y, 2x, 2z), \qquad \nabla g = (2x, 2y, 2z)$$

og får dermed likningane

$$z^2 + 2xy + 1 = 0$$
$$2y = 2\lambda x$$
$$2x = 2\lambda y$$
$$2z = 2\lambda z.$$

Frå den siste likninga ser me at me må ha $\lambda = 1$ eller $z = 0$. Men viss $\lambda = 1$ har me òg $x = y$, og den fyrste likninga vert dermed

$$z^2 + 2x^2 + 1 = 0,$$

som er umogleg for reelle tal $x, z$. Altso er $z = 0$.

Sidan $y = \lambda x = \lambda^2 y$, er $\lambda^2 = 1$ eller $y = 0$. Men viss $y = z = 0$ har me inga løysing av den fyrste likninga, og sidan me allereie har utelukka $\lambda = 1$, er me nøydde til å ha $\lambda = -1$ og dermed $x = -y$. Set me dette inn i den fyrste likninga i lag med $z = 0$, får me

$$0 - 2y^2 + 1 = 0 \quad \Rightarrow \quad y = \pm\frac{1}{\sqrt{2}}.$$

Likningssystemet vårt har altso dei to løysingane

$$(x, y, z) = \left(\mp\frac{1}{\sqrt{2}}, \pm\frac{1}{\sqrt{2}}, 0\right).$$

Evaluerer me i desse to punkta, får me

$$g\left(\mp\frac{1}{\sqrt{2}}, \pm\frac{1}{\sqrt{2}}, 0\right) = \frac{1}{2} + \frac{1}{2} + 0 = 1,$$

so båe desse punkta har same avstand frå origo. For å visa at dette er minimumsavstanden kan me observera at me kan finna punkt vilkårleg langt vekke frå origo som ligg på hyperboloiden, slik at det ikkje finst nokon maksimumsavstand.

Kildesett: course=TMA4105 term=sommer year=2022 problem=1 file=tma4105_2022k.pdf
