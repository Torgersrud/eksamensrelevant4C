### **Løsning til Oppgave 4**

a)  Ved Lagrange-interpolasjon:

$$p(x)=\frac{(x-\frac{1}{2})(x-1)}{-\frac{1}{2}\cdot(-1)}+\frac{2}{3}\cdot\frac{x(x-1)}{\frac{1}{2}\cdot(-\frac{1}{2})}+\frac{1}{2}\cdot\frac{x(x-\frac{1}{2})}{1\cdot\frac{1}{2}}$$

$$=(2x^2-3x+1)+\frac{2}{3}(-4x^2+4x)+\frac{1}{2}(2x^2-x)$$

$$=\frac{1}{3}x^2-\frac{5}{6}x+1.$$

Ved bruk av dividerte differenser får vi følgende tabell

$$\begin{array}{cc|cc}0&1&&\\ &&-2/3&\\ 1/2&2/3&&1/3\\ &&-1/3&\\ 1&1/2&&\end{array}$$

og polynomet blir

$$p(x)=1-\frac{2}{3}x+\frac{1}{3}x\left(x-\frac{1}{2}\right)=\frac{1}{3}x^2-\frac{5}{6}x+1.$$

Dette gir $y(3/4)\approx p(3/4)=3/16=0,562500$.

(Til sammenligning: den underliggende funksjonen er $y(x)=1/(1+x)$ slik at $y(3/4)=4/7\approx 0,571428$.)

b)  Vi finner en tilnærmelse til integralet ved å integrere interpolasjonspolynomet:

$$\int_0^1p(x)\,\mathrm{d}x=\frac{25}{36}\approx 0,694444.$$

Trapesmetoden gir

$$T=\frac{1}{2}\left(\frac{1}{2}y_0+y_1+\frac{1}{2}y_2\right)=\frac{17}{24}\approx 0,708333.$$

Feilen ved bruk av de to metodene er henholdsvis $1,3\cdot 10^{-3}$ og $1,5\cdot 10^{-2}$. Vi får altså en vesentlig bedre tilnærmelse ved å integrere 2. grads-polynomet (som i dette tilfellet gir samme resultat som om vi hadde brukt Simpsons metode).

*Kjeldevarsel: I løsningsforslagets punkt a) står det "$p(3/4)=3/16=0,562500$", men utrekninga gir $p(3/4)=9/16=0,5625$. Desimaltalet og resten av oppgåva er rette; trykkfeilen gjeld berre brøken $3/16$. Vi har kontrollert at $p(x)=\frac{1}{3}x^2-\frac{5}{6}x+1$ gir $p(3/4)=9/16$, og at $\int_0^1p\,\mathrm{d}x=25/36$ og $T=17/24$ med feil høvesvis $1{,}3\cdot 10^{-3}$ og $1{,}5\cdot 10^{-2}$ mot $\ln 2$.*

Kildesett: course=TMA4135 term=kont year=2011 problem=4 file=tma4135_11k.pdf
