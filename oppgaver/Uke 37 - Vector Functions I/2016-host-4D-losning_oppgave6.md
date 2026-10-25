### **Løsning til Oppgave 6**

**a)** To ligninger:

$$|(x,y)-A|=15.5\,\text{m},\qquad|(x,y)-B|=6.5\,\text{m}$$

[Figur: rommet $A=(0,0)$, $B=(20,0)$, $C=(20,10)$, $D=(0,10)$ tegnet i målestokk, med sirkelbue om $A$ gjennom målt posisjon og sirkelbue om $B$; skjæringspunktet avleses som $\sim R_0^*=(15,4)$m, og $R_1$ og $R_B$ er markert.]

Av figuren fås

$$R_0^*=(15,4)\,\text{m}$$

To gradienter:

$$\nabla f_A(R_0^*)=\frac{R_0^*-A}{|R_0^*-A|}=\frac{(15,4)}{|(15,4)|},\qquad\nabla f_B(R_0^*)=\frac{(15,4)-(20,0)}{|(-5,4)|}=\frac{(-5,4)}{|(-5,4)|}$$

Lineariserte ligninger (= Newton):

$$\begin{bmatrix}\nabla f_A(R_0^*)\\ \nabla f_B(R_0^*)\end{bmatrix}\cdot\begin{bmatrix}\Delta x\\ \Delta y\end{bmatrix}=\begin{bmatrix}15.5\,\text{m}-|R_0^*-A|\\ 6.5\,\text{m}-|R_0^*-B|\end{bmatrix}$$

dvs. (etter multiplikasjon med lengdene)

$$\begin{bmatrix}15&4\\ -5&4\end{bmatrix}\begin{bmatrix}\Delta x\\ \Delta y\end{bmatrix}=\begin{bmatrix}-0.3753\,\text{m}\\ 0.6203\,\text{m}\end{bmatrix}$$

Gauss-eliminasjon gir $(\Delta x,\Delta y)\approx(-0.0498,\ 0.0929)$m og

$$\underline{\underline{R_1^*\approx(14.95,\ 4.09)\,\text{m}}}$$

(som er lik eksakt løsning med de oppgitte antall siffer.)

**b)** $R_1=(14,6.5)$m og $R_B=(20,6.5)$m — konvergens etter 1 steg.

Den geometriske tolkningen: for hver måling projiseres startpunktet inn mot målesirkelen langs radialen fra hjørnet, dvs. Newton's metode erstatter målesirkelen med tangenten i punktet hvor radialen gjennom startpunktet treffer sirkelen. $R_1$ er skjæringspunktet mellom de to tangentlinjene — se figuren i a). Med bare målingen om $B$ beveger metoden punktet langs radialen fra $B$ gjennom $C$ helt inn på sirkelen, og treffer $(20,6.5)$m eksakt allerede etter ett steg.

Med $4$ målinger vil Newton's metode gi $4$ linjer, og approksimert skjæringspunkt finnes i hvert steg ved minste kvadraters metode.

Kildesett: course=TMA4135 term=host year=2016 problem=6 file=tma4135_16h.pdf
