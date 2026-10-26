### **Løsning til Oppgave 5**

Ved kjerneregelen blir den tidsderiverte av valutakursen

$$\frac{d}{dt} f(x, y, z) = \frac{\partial f}{\partial x} \frac{dx}{dt} + \frac{\partial f}{\partial y} \frac{dy}{dt} + \frac{\partial f}{\partial z} \frac{dz}{dt} = -\frac{1}{x^2 y} \frac{dx}{dt} + \left(-\frac{1}{xy^2} + \frac{1}{z}\right) \frac{dy}{dt} + \left(-\frac{y}{z^2} + \frac{1}{z}\right) \frac{dz}{dt}.$$

Vi setter inn de gitte tallene, og får

$$\frac{df}{dt} = -\frac{1}{200^2 \cdot 100} \cdot 1 + \left(-\frac{1}{200 \cdot 100^2} + \frac{1}{400}\right) \cdot \left(-\frac{1}{2}\right) + \left(-\frac{100}{400^2} + \frac{1}{400}\right) \cdot \frac{1}{2}$$

$$= -\frac{1}{4\,000\,000} + \frac{1}{4\,000\,000} - \frac{1}{800} - \frac{1}{3200} + \frac{1}{800} = -\frac{1}{3200} < 0,$$

så valutakursen avtar i øyeblikket.

Kildesett: course=SIF5005 term=sommer year=2003 problem=5 file=sif5005_03k.pdf
