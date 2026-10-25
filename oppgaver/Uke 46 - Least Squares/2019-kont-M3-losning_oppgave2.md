### **Løsning til Oppgave 2**

**a)** Nullrommet til $A$ er alle vektorer $\mathbf{x}$ slik at

$$A\mathbf{x}=\mathbf{0}.$$

For at nullrommet skal være et underrom av $\mathbb{R}^n$ så må vi vise tre ting:
1) $\mathbf{0}\in\mathrm{Null}\ A$,
2) dersom $\mathbf{u},\mathbf{v}\in\mathrm{Null}\ A$ så må $\mathbf{u}+\mathbf{v}\in\mathrm{Null}\ A$, og
3) dersom $\mathbf{u}\in\mathrm{Null}\ A$ så må $r\mathbf{u}\in\mathrm{Null}\ A$ for alle $r\in\mathbb{R}$.

Det er lett å se at punkt 1) er oppfylt: $A\mathbf{0}=\mathbf{0}$. Dermed er $\mathbf{0}\in\mathrm{Null}\ A$.
Punkt 2) følger fra det faktum at matrisemultiplikasjon er distributiv. Da får vi at $A(\mathbf{u}+\mathbf{v})=A\mathbf{u}+A\mathbf{v}=\mathbf{0}+\mathbf{0}=\mathbf{0}$, som gir at $\mathbf{u}+\mathbf{v}\in\mathrm{Null}\ A$.
Punkt 3) følger fra det faktum at konstanter kan flyttes utenfor. Da får vi at $A(r\mathbf{u})=r(A\mathbf{u})=r\mathbf{0}=\mathbf{0}$, som gir at $r\mathbf{u}\in\mathrm{Null}\ A$ for alle $r\in\mathbb{R}$.

**b)** Vi beregner

$$\begin{bmatrix}2&4&0\\ -5&-4&6\\ 1&-2&-4\end{bmatrix}\begin{bmatrix}1\\ 2\\ -1\end{bmatrix}=\begin{bmatrix}6\\ -19\\ 1\end{bmatrix}$$

og

$$\begin{bmatrix}2&4&0\\ -5&-4&6\\ 1&-2&-4\end{bmatrix}\begin{bmatrix}2\\ -1\\ 1\end{bmatrix}=\begin{bmatrix}0\\ 0\\ 0\end{bmatrix}$$

Den første vektoren ligger ikke i nullrommet til $A$. Den andre gjør det.

Siden nullrommet til $A$ inneholder minst én vektor, må kolonnerommet til $A$ ha være en- eller todimensjonalt, og siden kolonnene i $A$ ikke er parallelle, må kolonnerommet være todimensjonalt. Siden

$$\begin{bmatrix}2\\ -1\\ 1\end{bmatrix}$$

ligger i nullrommet til $A$, og det er endimensjonalt, så er den en basisvektor for nullrommet. Videre kan vi finne en basis for kolonnerommet ved å Gauss-eliminere matrisen på følgende vis:

$$\begin{bmatrix}2&4&0\\ -5&-4&6\\ 1&-2&-4\end{bmatrix}\sim\begin{bmatrix}1&2&0\\ -5&-4&6\\ 1&-2&-4\end{bmatrix}\sim\begin{bmatrix}1&2&0\\ 0&6&6\\ 0&-4&-4\end{bmatrix}\sim\begin{bmatrix}1&2&0\\ 0&1&1\\ 0&1&1\end{bmatrix}\sim\begin{bmatrix}1&2&0\\ 0&1&1\\ 0&0&0\end{bmatrix}.$$

Da ser vi at de to første kolonnene har ledende enere, og vi kan dermed velge en basis for kolonnerommet til $A$ som består av de to første kolonnene i matrisen $A$. Vi kan også forenkle den andre kolonnen ved å dele på to. Dette impliserer at:

$$\mathrm{Col}\ A=span\left\{\begin{bmatrix}2\\ -5\\ 1\end{bmatrix},\begin{bmatrix}2\\ -2\\ -1\end{bmatrix}\right\},\ \text{og}\ \mathrm{Null}\ A=span\left\{\begin{bmatrix}2\\ -1\\ 1\end{bmatrix}\right\}.$$

**c)** Vi tar utgangspunkt i basisen vi fant i forrige oppgave, og bruker Gram-Schmidt for å finne en ortogonal basis for kolonnerommet til $A$: Først setter vi $\mathbf{v}_1=\begin{bmatrix}2&-5&1\end{bmatrix}^{\top}$, og så ortogonaliserer vi slik at

$$\mathbf{v}_2=\begin{bmatrix}2\\ -2\\ -1\end{bmatrix}-\frac{\begin{bmatrix}2\\ -2\\ -1\end{bmatrix}\cdot\begin{bmatrix}2\\ -5\\ 1\end{bmatrix}}{\begin{bmatrix}2\\ -5\\ 1\end{bmatrix}\cdot\begin{bmatrix}2\\ -5\\ 1\end{bmatrix}}\begin{bmatrix}2\\ -5\\ 1\end{bmatrix}=\begin{bmatrix}2\\ -2\\ -1\end{bmatrix}-\frac{13}{30}\begin{bmatrix}2\\ -5\\ 1\end{bmatrix}=\frac{1}{30}\begin{bmatrix}34\\ 5\\ -43\end{bmatrix}$$

og, etter å ha skalert opp $\mathbf{v}_2$, velger

$$\left\{\begin{bmatrix}2\\ -5\\ 1\end{bmatrix},\begin{bmatrix}34\\ 5\\ -43\end{bmatrix}\right\}$$

som vår ortogonale basis.

Siden vi har en ortogonal basis for kolonnerommet til $A$, kan vi projisere vektoren

$$\mathbf{b}=\begin{bmatrix}3\\ 3\\ 9\end{bmatrix}$$

på hvert av disse basiselementene, og så legge projeksjonene sammen for å få den ortogonale projeksjonen på kolonnerommet. Vektoren vi skal ha, er altså

$$\begin{aligned}P_{\mathrm{Col}\,A}(\mathbf{b})&=P_{\mathbf{v}_1}(\mathbf{b})+P_{\mathbf{v}_2}(\mathbf{b})\\
&=\frac{\begin{bmatrix}3\\ 3\\ 9\end{bmatrix}\cdot\begin{bmatrix}2\\ -5\\ 1\end{bmatrix}}{\begin{bmatrix}2\\ -5\\ 1\end{bmatrix}\cdot\begin{bmatrix}2\\ -5\\ 1\end{bmatrix}}\begin{bmatrix}2\\ -5\\ 1\end{bmatrix}+\frac{\begin{bmatrix}3\\ 3\\ 9\end{bmatrix}\cdot\begin{bmatrix}34\\ 5\\ -43\end{bmatrix}}{\begin{bmatrix}34\\ 5\\ -43\end{bmatrix}\cdot\begin{bmatrix}34\\ 5\\ -43\end{bmatrix}}\begin{bmatrix}34\\ 5\\ -43\end{bmatrix}\\
&=\frac{0}{30}\begin{bmatrix}2\\ -5\\ 1\end{bmatrix}+\frac{-270}{3030}\begin{bmatrix}34\\ 5\\ -43\end{bmatrix}\\
&=\frac{-9}{101}\begin{bmatrix}34\\ 5\\ -43\end{bmatrix}.\end{aligned}$$

Vi kunne også brukt minste kvadraters metode for å få samme løsning, eller brukt en annen basis fra forrige oppgave.

*Kjeldevarsel: fasiten skriv $\begin{bmatrix}6\\ -19\\ 1\end{bmatrix}$ i det første produktet i b), men rekninga gir $\begin{bmatrix}10\\ -19\\ 1\end{bmatrix}$ — trykkfeil i fasiten, konklusjonen endrar seg ikkje. Teksten over fylgjer fasiten som det står. Gram-Schmidt-steget, projeksjonssummen $P_{\mathrm{Col}\,A}(\mathbf{b})=P_{\mathbf{v}_1}(\mathbf{b})+P_{\mathbf{v}_2}(\mathbf{b})$ og svaret $\frac{-9}{101}(34,5,-43)^{\top}$ er kontrollrekna med sympy.*

Kildesett: course=TMA4110 term=kont year=2019 problem=2 file=TMA4110_TMA4115_kont_sommer2019_bokmaal.pdf
