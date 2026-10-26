### **Løsning til Oppgave 5**

Kurven $2x^{3/2} + y^3 + 5xy = 1$ skjærer koordinataksene i $(0, 1)$ og $((\frac{1}{2})^{2/3}, 0)$ (og ingen andre steder), så vi får et område som vist på figuren.

*Løsningsforslaget har ein figur som viser området i første kvadrant, avgrensa av aksane og ein konveks kurve mellom (0,1) og eit punkt rundt 0,63 på x-aksen.*

Funksjonen $f(x, y) = xy$ har ett kritisk punkt, i origo, så ingen kritiske punkter ligger i det indre av området. Maksimum og minimum oppnås derfor på randen. Siden $f(x, y) \ge 0$ i 1. kvadrant og $f(x, y) = 0$ langs aksene, er $f_{\min} = 0$ i $R$.

Maksimum må etter dette oppnås langs kurven $2x^{3/2} + y^3 + 5xy = 1$. Lagranges metode, med $g(x, y) = 2x^{3/2} + y^3 + 5xy$, gir:

$$\nabla f = \lambda \nabla g \ \Rightarrow\ \left\{ \begin{array}{l} y = \lambda (3x^{1/2} + 5y) \\ x = \lambda (3y^2 + 5x) \end{array} \right. \Rightarrow\ \left\{ \begin{array}{l} xy = \lambda (3x^{3/2} + 5xy) \\ xy = \lambda (3y^3 + 5xy) \end{array} \right. \Rightarrow\ x^{3/2} = y^3 \Rightarrow x = y^2.$$

Innsatt i $2x^{3/2} + y^3 + 5xy = 1$ gir dette $8y^3 = 1$, dvs. $y = 1/2$ og $x = y^2 = 1/4$.

Så $f_{\max} = f(1/4, 1/2) = 1/8$.

Kildesett: course=SIF5005 term=var year=2000 problem=5 file=sif5005_00v.pdf
