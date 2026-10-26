### **Løsning til Oppgave 10**

Punktet med sylinderkoordinater $(r, \theta, z) = (\sqrt{2}, \pi/4, 1)$ har kartesiske koordinater

$$x = r\cos\theta = \sqrt{2} \cdot \frac{1}{\sqrt{2}} = 1, \quad y = r\sin\theta = \sqrt{2} \cdot \frac{1}{\sqrt{2}} = 1, \quad z = 1,$$

som er punktet der vi kjenner verdien av $\nabla f$. Kjerneregelen gir da

$$\frac{\partial g}{\partial \theta} = \frac{\partial f}{\partial x} \frac{\partial x}{\partial \theta} + \frac{\partial f}{\partial y} \frac{\partial y}{\partial \theta} + \frac{\partial f}{\partial z} \frac{\partial z}{\partial \theta}$$

$$= \frac{\partial f}{\partial x}(-r\sin\theta) + \frac{\partial f}{\partial y} \, r\cos\theta + \frac{\partial f}{\partial z} \cdot 0$$

$$= 1 \cdot (-1) + 1 \cdot 1 + 0 = 0.$$

Kildesett: course=TMA4105 term=sommer year=2021 problem=10 file=tma4105_2021k.pdf
