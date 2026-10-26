### **Løsning til Oppgave 4**

Den gitte parameterfremstillingen gir

$$\frac{\partial \mathbf{r}}{\partial u} = (\cos v)\mathbf{i} + (\sin v)\mathbf{j}, \qquad \frac{\partial \mathbf{r}}{\partial v} = -(u \sin v)\mathbf{i} + (u \cos v)\mathbf{j} + \mathbf{k}$$

og dermed

$$\frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} = (\sin v)\mathbf{i} - (\cos v)\mathbf{j} + u\mathbf{k}, \qquad \left| \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \right| = \sqrt{1 + u^2}.$$

Vi har nå valget mellom de to integrasjonsrekkefølgene

$$\int_0^2 \int_{v/2}^1 \sqrt{1 + u^2}\, du\, dv \quad \text{og} \quad \int_0^1 \int_0^{2u} \sqrt{1 + u^2}\, dv\, du.$$

Det siste valget gir enklest integrasjon:

$$A = \int_0^1 \int_0^{2u} \sqrt{1 + u^2}\, dv\, du = \int_0^1 2u \sqrt{1 + u^2}\, du = \left[ \frac{2}{3} (1 + u^2)^{3/2} \right]_0^1 = \frac{2}{3} (2\sqrt{2} - 1).$$

Kildesett: course=SIF5005 term=var year=2002 problem=4 file=sif5005_02v.pdf
