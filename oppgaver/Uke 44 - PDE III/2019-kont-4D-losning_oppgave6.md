### **Løsning til Oppgave 6**

Taylor-utvikler $f(x\pm h)$ rundt $x$:

$$\begin{aligned}\frac{f(x+h)-2f(x)+f(x-h)}{h^2}=&\frac{1}{h^2}\Bigg(f(x)+hf'(x)+\frac{h^2}{2}f''(x)+\frac{h^3}{3!}f'''(x)+\frac{h^4}{4!}f^{(4)}(\xi_1)\\&-2f(x)\\&+f(x)-hf'(x)+\frac{h^2}{2}f''(x)-\frac{h^3}{3!}f'''(x)+\frac{h^4}{4!}f^{(4)}(\xi_2)\Bigg)\\=&f''(x)+\frac{h^2}{4!}\Big(f^{(4)}(\xi_1)+f^{(4)}(\xi_2)\Big)\qquad\text{(Middelverdisetningen)}\\=&f''(x)+\frac{h^2}{12}f^{(4)}(\xi).\end{aligned}$$

Her er $x-h<\xi_1<x$, $x<\xi_2<x+h$ og $\xi_1<\xi<\xi_2$, så $x-h<\xi<x+h$. Forutsatt at $f^{(4)}(x)$ er kontinuerlig i et område rundt $x$ så finnes en konstant $C$ slik at $|f^{(4)}|<C$ i området, og

$$\Big|f''(x)-\frac{f(x+h)-2f(x)+f(x-h)}{h^2}\Big|<\frac{C}{12}h^2.$$

Tilnærmelsen er av orden 2.

Kildesett: course=TMA4135 term=kont year=2019 problem=6 file=tma4125-30-35-k19-bm.pdf
