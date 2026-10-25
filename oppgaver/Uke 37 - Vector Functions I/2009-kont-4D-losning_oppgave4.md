### **Løsning til Oppgave 4**

Vi finner først gradienten til funksjonen i punktet $(x_0, y_0)$.

$$\text{grad} f(x_0, y_0) = \frac{\partial f}{\partial x}(x_0, y_0) \boldsymbol{i} + \frac{\partial f}{\partial y}(x_0, y_0) \boldsymbol{j}.$$

Litt regning gir

$$\text{grad} f(x_0, y_0) = 2x \left( 1 + e^{y^3} \right)^2 \boldsymbol{i} + 6x^2 y^2 e^{y^3} \left( 1 + e^{y^3} \right) \boldsymbol{j}.$$

Gradienten i punktet $(1, 1)$ blir dermed $2(1+e)^2 \boldsymbol{i} + 6e(1+e) \boldsymbol{j}$. Det er da bare å skrive opp svaret.

$$\boldsymbol{u}_+ = \frac{1}{\sqrt{10e^2 + 2e + 1}} ((1+e)\boldsymbol{i} + 3e\boldsymbol{j}), \quad \boldsymbol{u}_- = -\boldsymbol{u}_+ \quad \text{og} \quad \boldsymbol{u}_0 = \frac{\pm 1}{\sqrt{10e^2 + 2e + 1}} (3e\boldsymbol{i} - (1+e)\boldsymbol{j}).$$

Kildesett: course=TMA4135 term=kont year=2009 problem=4 file=tma4135_09k.pdf
