### **Løsning til Oppgave 1**

Vi finner de partiellderiverte av første og annen orden av $f(x, y) = x \sin y$:

$$f_x = \sin y, \quad f_y = x \cos y, \qquad f_{xx} = 0, \quad f_{xy} = \cos y, \quad f_{yy} = -x \sin y.$$

Vi finner de kritiske punktene ved å løse $f_x = f_y = 0$. $f_x = 0$ gir $\sin y = 0$, dvs. $y = \pi n$ for $n$ heltallig. Derfor er $\cos y = \pm 1 \neq 0$, så $f_y = 0$ gir $x = 0$. De kritiske punktene er altså

$$x = 0, \quad y = \pi n, \quad n = 0, \pm 1, \pm 2, \ldots$$

Diskriminanten i annenderiverttesten er

$$\Delta(x, y) = f_{xx} f_{yy} - f_{xy}^2 = -\cos^2 y,$$

og i de kritiske punktene har denne verdien $-1$, siden $\cos y = \cos \pi n = \pm 1$ for heltallig $n$. De kritiske punktene er derfor **sadelpunkter**.

*Løsningsforslaget har en figur som viser flaten $z = x \sin y$: en bølgeflate som svinger mellom toppar og dalar langs $y$-aksen, med sadlane i punkta $(0, \pi n)$.*

Kildesett: course=TMA4105 term=var year=2005 problem=1 file=tma4105_05v.pdf
