### **Løsning til Oppgave 1**

Gradienten til $f$ er $\nabla f = \langle 4y - 4x, 4x - 4y^3 \rangle$, og den Hessiske determinanten er

$$\begin{vmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{vmatrix} = \begin{vmatrix} -4 & 4 \\ 4 & -12y^2 \end{vmatrix} = 48y^2 - 16.$$

a) Vi finner alle de kritiske punktene ved å løse ligningene

$$4y - 4x = 0, \qquad 4x - 4y^3 = 0.$$

Setter vi $y = x$ inn i den andre ligningen får vi $x = x^3$, som har løsningene $0$, $1$ og $-1$. Altså er det nøyaktig 3 kritiske punkter, $(-1, -1)$, $(0, 0)$ og $(1, 1)$.

b) Den Hessiske determinanten er negativ i $(0, 0)$, så dette er et sadelpunkt. De to andre kritiske punktene er lokale maksimumspunkter, fordi den Hessiske determinanten er positiv og $-4 < 0$.

Kildesett: course=TMA4105 term=sommer year=2010 problem=1 file=tma4105_10k.pdf
