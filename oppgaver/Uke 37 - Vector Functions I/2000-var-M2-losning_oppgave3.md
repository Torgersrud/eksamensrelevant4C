### **Løsning til Oppgave 3**

$$\frac{\partial(u, v)}{\partial(x, y)} = \begin{vmatrix} 2x & -2y \\ y & x \end{vmatrix} = 2(x^2 + y^2), \ \text{så} \ \frac{\partial(x, y)}{\partial(u, v)} = \left( \frac{\partial(u, v)}{\partial(x, y)} \right)^{-1} = \frac{1}{2(x^2 + y^2)}.$$

Sammen med $\delta = k(x^2 + y^2)$ gir dette:

$$m = \iint_R \delta \, dA = \iint_R k(x^2 + y^2) \, dA = \int_{\frac{1}{2}}^{1} \int_1^2 k(x^2 + y^2) \cdot \frac{\partial(x, y)}{\partial(u, v)} \, du \, dv$$

$$= \int_{\frac{1}{2}}^{1} \int_1^2 k(x^2 + y^2) \, \frac{1}{2(x^2 + y^2)} \, du \, dv = \int_{\frac{1}{2}}^{1} \int_1^2 \frac{k}{2} \, du \, dv = \frac{k}{2} \cdot \frac{1}{2} = \frac{k}{4}.$$

Kildesett: course=SIF5005 term=var year=2000 problem=3 file=sif5005_00v.pdf
