### **Løsning til Oppgave 9**

Implisitt derivasjon med hensyn på $y$ av $x + z + (y + z)^5 = 6$ gir

$$\frac{\partial z}{\partial y} + 5\left(1 + \frac{\partial z}{\partial y}\right)(y + z)^4 = 0, \tag{7}$$

som gir at

$$\frac{\partial z}{\partial y} = -\frac{5(y + z)^4}{1 + 5(y + z)^4}.$$

Implisitt derivasjon med hensyn på $x$ av $x + z + (y + z)^5 = 6$ gir

$$1 + \frac{\partial z}{\partial x} + 5\frac{\partial z}{\partial x}(y + z)^4 = 0,$$

som gir at

$$\frac{\partial z}{\partial x} = -\frac{1}{1 + 5(y + z)^4}.$$

Implisitt derivasjon med hensyn på $x$ av ligning (7) gir

$$\frac{\partial^2 z}{\partial x \, \partial y} + 5\frac{\partial^2 z}{\partial x \, \partial y}(y + z)^4 + 20\left(1 + \frac{\partial z}{\partial y}\right)(y + z)^3\frac{\partial z}{\partial x} = 0$$

som innsatt for uttrykkene for $\partial z/\partial x$ og $\partial z/\partial y$ gir at

$$\frac{\partial^2 z}{\partial x \, \partial y}\left(1 + 5(y + z)^4\right) - \frac{20(y + z)^3}{\left(1 + 5(y + z)^4\right)^2} = 0.$$

Det vil si,

$$\frac{\partial^2 z}{\partial x \, \partial y} = \frac{20(y + z)^3}{\left(1 + 5(y + z)^4\right)^3}$$

som igjen gir at

$$\left.\frac{\partial^2 z}{\partial x \, \partial y}\right|_{(2, -2, 3)} = \frac{20}{6^3} = \frac{5}{54}.$$

Kildesett: course=TMA4105 term=sommer year=2018 problem=9 file=tma4105_2018k.pdf
