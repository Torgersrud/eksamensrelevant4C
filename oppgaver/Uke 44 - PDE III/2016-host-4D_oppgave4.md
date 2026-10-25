### **Oppgave 4**

La $g$ være den odde utvidelsen til

$$f(x)=\left\{\begin{array}{ll}x&\text{hvis }0\le x<\frac{1}{2},\\ 1-x&\text{hvis }\frac{1}{2}\le x\le1.\end{array}\right.$$

**a)** Skisser grafen til $y=g(x)$ for $-1\le x\le1$. Finn Fourier-sinusrekken til $f$.

**b)** Vis at $\pi^2=8(1+1/3^2+1/5^2+1/7^2+\cdots)$.

**c)** Finn løsningen $u(x,t)$ til varmeligningen

$$u_t=u_{xx},\ 0\le x\le1,\ 0\le t$$

som oppfyller randbetingelsene $u(0,t)=u(1,t)=0$ og startbetingelsen $u(x,0)=f(x)$ ved separasjon av variable. Hint: Start med $u(x,t)=F(x)G(t)$.

**d)** Vis at $v(x,t)=u(x,t)+1-x$ løser varmeligningen $v_t=v_{xx}$ med randbetingelsene $v(0,t)=1$, $v(1,t)=0$ og startbetingelsen $v(x,0)=f(x)+1-x$. Forklar hvordan denne varmeligningen kan løses ved Crank-Nicolson metoden.

**e)** La $X(t)=u(1/4,t)=u(3/4,t)$ og $Y(t)=u(1/2,t)$. Beregn en approximasjon til $X(1/16)$ og $Y(1/16)$ ved å beregne et steg med den implisitte Euler metoden.

Kildesett: course=TMA4135 term=host year=2016 problem=4 file=tma4135_16h.pdf
