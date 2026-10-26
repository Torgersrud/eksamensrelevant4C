### **Løsning til Oppgave 6**

$$f(1, \ln 2, 8) = 1 \cdot 8 \cdot e^{2\ln 2} = 8 \cdot 2^2 = 32.$$

Anslag for maksimal feil:

$$|\Delta f| \approx \frac{\partial f}{\partial x}(1, \ln 2, 8) \cdot |\Delta x| + \frac{\partial f}{\partial y}(1, \ln 2, 8) \cdot |\Delta y| + \frac{\partial f}{\partial z}(1, \ln 2, 8) \cdot |\Delta z|$$

$$\le \left( z e^{2y} \right)_{(1, \ln 2, 8)} \cdot 0.1 + \left( 2xz e^{2y} \right)_{(1, \ln 2, 8)} \cdot 0.1 + \left( x e^{2y} \right)_{(1, \ln 2, 8)} \cdot 0.1$$

$$= 8 \cdot 2^2 \cdot 0.1 + 2 \cdot 8 \cdot 2^2 \cdot 0.1 + 1 \cdot 2^2 \cdot 0.1 = 10.$$

Kildesett: course=TMA4105 term=sommer year=2009 problem=6 file=tma4105_09k.pdf
