### **Løsning til Oppgave 4**

**a)** Vi har $f(0)=1$, $f(1)=1/2$ og $f(2)=1/5$. Interpolasjonspolynomet (på Lagrange-form) er

$$p_2(x)=f(x_0)\frac{(x-x_1)(x-x_2)}{(x_0-x_1)(x_0-x_2)}+f(x_1)\frac{(x-x_0)(x-x_2)}{(x_1-x_0)(x_1-x_2)}+f(x_2)\frac{(x-x_0)(x-x_1)}{(x_2-x_0)(x_2-x_1)}$$

$$=\frac{(x-1)(x-2)}{(-1)(-2)}+\frac{1}{2}\cdot\frac{x(x-2)}{1\cdot(1-2)}+\frac{1}{5}\cdot\frac{x(x-1)}{2\cdot(2-1)}$$

$$=\frac{1}{2}(x-1)(x-2)+\frac{1}{10}x(x-1)-\frac{1}{2}x(x-2)$$

$$=\frac{1}{10}(x^2-6x+10).$$

**b)** Ved å integrere begge sider av differensialligningen fra $0$ til $x$ får vi

$$\int_{0}^{x}\frac{dy}{dt}dt=\int_{0}^{x}\frac{1}{1+t^2}\,\mathrm{d}t$$

$$y(x)-y(0)=\int_{0}^{x}\frac{1}{1+t^2}\,\mathrm{d}t$$

$$y(x)=1+\int_{0}^{x}\frac{1}{1+t^2}\,\mathrm{d}t\,.$$

Fra **a)** vet vi at funksjonen $1/(1+t^2)$ kan tilnærmes med polynomet $p_2(t)=\frac{1}{10}(t^2-6t+10)$. Ved å bruke dette i integralligningen får vi

$$y(x)\approx 1+\int_{0}^{x}\frac{1}{10}(t^2-6t+10)\,\mathrm{d}t=1+\frac{1}{30}(x^3-9x^2+30x).$$

Dette gir $y(5)\approx 8/3\approx 2.66667$.

Integralet kan løses eksakt og løsningen av differensialligningen blir

$$y(x)=1+\tan^{-1}(x).$$

Vi har $y(5)=1+\tan^{-1}(5)\approx 2.37340$, så den absolutte feilen i tilnærmingen er $|e|=|2.66667-2.37340|=0.29327$.

Kildesett: course=TMA4123 term=var year=2013 problem=4 file=eksamen2013v.pdf
