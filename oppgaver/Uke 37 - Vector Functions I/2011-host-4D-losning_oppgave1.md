### **Løsning til Oppgave 1**

Vi har

$$f(x,y)=\frac{x^2+2y^2}{x^2-y^2},$$

for $x^2\ne y^2$. Dette gir

$$\nabla f=\frac{6xy}{(x^2-y^2)^2}[-y,x].$$

For $(x,y)=(2,1)$ er altså

$$\nabla f=\frac{4}{3}[-1,2].$$

Enhetsvektoren i retningen bestemt av $\bar{v}$ er

$$\bar{u}=\frac{\bar{v}}{|\bar{v}|}=\frac{1}{\sqrt{2}}[1,1],$$

og dermed er $Df=\nabla f\cdot\bar{u}=2\sqrt{2}/3$.

Størst mulig verdi for $Df=\nabla f\cdot\bar{u}$ er når $\bar{u}$ peker samme vei som $\nabla f$. Da er maksimal $Df=\nabla f\cdot\bar{u}=|\nabla f|$. For $(x,y)=(2,1)$ er følgelig maksimal retningsderivert

$$|\nabla f|=\frac{4}{3}\sqrt{5}.$$

Kildesett: course=TMA4135 term=host year=2011 problem=1 file=tma4135_11h.pdf
