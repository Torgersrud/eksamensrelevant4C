### **Løsning til Oppgave 2**

Kurven gitt ved $xy^2 = 8$ er symmetrisk om $x$-aksen og ligger i høyre halvplan. Vi konsentrerer oss derfor om den delen av kurven som ligger i første kvadrant, dvs $x > 0$ og $y > 0$. Vi finner minimum blant punktene $(x, y)$ som tilfredstiller ligningene:

$$\nabla(x^2 + y^2) - \lambda \nabla(xy^2 - 8) = 0, \qquad xy^2 - 8 = 0.$$

Dette gir 3 ligninger

$$2x - \lambda y^2 = 0, \qquad 2y - \lambda 2xy = 0, \qquad xy^2 = 8.$$

Det er mange måter å løse disse ligningene på. Her er en måte. Siden $xy^2 = 8$ kan verken $x$ eller $y$ være 0, så vi kan dele den andre ligningen med $2y$ uten å miste noen løsninger. Vi finner da $\lambda = x^{-1}$. Fra den siste ligningen får vi $y^2 = 8x^{-1}$. Setter vi dette inn i den første ligningen får vi $2x = x^{-1} 8x^{-1}$, eller $x = 2^{\frac{2}{3}}$. Fra den siste ligninge får vi $y = (8x^{-1})^{\frac{1}{2}} = 2^{\frac{3}{2}} 2^{-\frac{1}{3}} = 2^{\frac{7}{6}}$. Siden vi kun finner ett kritisk punkt i første kvadrant, og avstanden til punkter på kurven kan bli så stor man bare vil, må dette være et minimumspunkt, og avstanden er

$$(x^2 + y^2)^{\frac{1}{2}} = \left(2^{\frac{4}{3}} + 2^{\frac{7}{3}}\right)^{\frac{1}{2}} = \left(2^{\frac{4}{3}} + 2^{\frac{4}{3}+1}\right)^{\frac{1}{2}} = \left(2^{\frac{4}{3}}(1+2)\right)^{\frac{1}{2}} = 2^{\frac{2}{3}} 3^{\frac{1}{2}} = 2.749459275\ldots.$$

*Kjeldevarsel: løsningsforslaget trykkjer «tilfredstiller» (riktig «tilfredsstiller») og «den siste ligninge» (riktig «ligningen»); teksten er teken vare på som han står.*

Kildesett: course=TMA4105 term=sommer year=2010 problem=2 file=tma4105_10k.pdf
