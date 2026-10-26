### **Løsning til Oppgave 4**

La $f(x, y, z) = xz^2 - yz + \cos xy$. Da er

$$\vec{N}(x, y, z) = \nabla f(x, y, z) = \langle z^2 - y \sin xy, \; -z - x \sin xy, \; 2xz - y \rangle$$

en normalvektor til $S$ i punktet $(x, y, z)$. Spesielt er

$$\vec{N}(0, 0, 1) = \langle 1, -1, 0 \rangle.$$

Punktet $(0, 0, 1)$ ligger både på flaten $S$ ($f(0, 0, 1) = 1$) og på den gitte kurven ($t = 1$). Tangentvektor til kurven i $(0, 0, 1)$ er $\vec{r}\,'(1)$ der $\vec{r}(t) = \langle \ln t, \, t \ln t, \, t \rangle$. Det vil si

$$\vec{r}\,'(1) = \langle 1/t, \, \ln t + 1, \, 1 \rangle \big|_{t=1} = \langle 1, 1, 1 \rangle.$$

Siden $\vec{N}(0, 0, 1) \cdot \vec{r}\,'(1) = \langle 1, -1, 0 \rangle \cdot \langle 1, 1, 1 \rangle = 0$, er $\vec{N}(0, 0, 1)$ en normalvektor til tangenten til kurven i $(0, 0, 1)$. Derfor ligger tangenten til kurven i tangentplanet til flaten $S$.

*Kjeldevarsel: løsningsforslaget trykkjer «normalplanet» i den siste setninga — trykkfeil for «tangentplanet», sidan utrekninga $\vec{N}\cdot\vec{r}\,'=0$ nettopp viser at tangenten står vinkelrett på flatenormalen og difor ligg i tangentplanet (slik oppgåveteksten òg seier); teksten her følgjer den rette sluttforma.*

Kildesett: course=SIF5005 term=var year=2001 problem=4 file=sif5005_01v.pdf
