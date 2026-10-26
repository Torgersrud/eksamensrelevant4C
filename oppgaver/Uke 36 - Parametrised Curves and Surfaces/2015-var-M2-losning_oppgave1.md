### **Løsning til Oppgave 1**

Vi deriverer, og setter inn $t = 1$ for det gitte punktet på kurven:

$$\mathbf{r}'(t) = \mathbf{i} + t^2\mathbf{j} + \sqrt{2}t\mathbf{k}, \qquad \mathbf{r}'(1) = \mathbf{i} + \mathbf{j} + \sqrt{2}\mathbf{k}.$$

Det gir

$$|\mathbf{r}'(t)| = \sqrt{1 + t^4 + 2t^2} = 1 + t^2, \qquad |\mathbf{r}'(1)| = 2.$$

Enhetstangenten for $t = 1$ blir

$$\hat{\mathbf{T}} = \frac{\mathbf{r}'(1)}{|\mathbf{r}'(1)|} = \frac{\mathbf{i} + \mathbf{j} + \sqrt{2}\mathbf{k}}{2},$$

og buelengden av hele kurven blir

$$\int_0^2 |\mathbf{r}'(t)| \, dt = \int_0^2 (1 + t^2) \, dt = 2 + \frac{2^3}{3} = \frac{14}{3}.$$

Kildesett: course=TMA4105 term=var year=2015 problem=1 file=tma4105_15v.pdf
