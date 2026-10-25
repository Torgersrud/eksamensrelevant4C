### **Løsning til Oppgave 3**

**a)** Ved innsetting ser vi at:

$$\frac{\partial}{\partial t}(u_1\pm u_2)-\frac{\partial^2}{\partial x^2}(u_1\pm u_2)=\left(\frac{\partial u_1}{\partial t}-\frac{\partial^2u_1}{\partial x^2}\right)\pm\left(\frac{\partial u_2}{\partial t}-\frac{\partial^2u_2}{\partial x^2}\right)=0,$$

og

$$(u_1+u_2)(0,t)=2a,\qquad\qquad(u_1-u_2)(0,t)=0,$$
$$(u_1+u_2)(1,t)=2b,\qquad\qquad(u_1-u_2)(1,t)=0.$$

Superposisjonsprinsippet holder for (*) dersom $Au_1(x,t)+Bu_2(x,t)$ også løser (*) for alle reelle tall $A$ og $B$:

$$\frac{\partial}{\partial t}(Au_1+Bu_2)-\frac{\partial^2}{\partial x^2}(Au_1+Bu_2)=A\left(\frac{\partial u_1}{\partial t}-\frac{\partial^2u_1}{\partial x^2}\right)+B\left(\frac{\partial u_2}{\partial t}-\frac{\partial^2u_2}{\partial x^2}\right)=0,$$

og

$$(Au_1+Bu_2)(0,t)=(A+B)a\quad\text{og}\quad(Au_1+Bu_2)(1,t)=(A+B)b,$$

dvs. $Au_1(x,t)+Bu_2(x,t)$ løser (*) bare når $a=0=b$. Dermed holder superposisjonsprinsippet ikke for (*) når $a$ eller $b$ er ulik null. Men det holder for (**) siden (**) svarer til (*) med $a=0=b$.

**b)** Legg merke til at $v_t=u_t$, $v_{xx}=v_{xx}$, $v(0,t)=u(0,t)-a$ og $v(1,t)=u(1,t)-b$. Siden $u$ oppfyller (*), ser vi at $v$ må oppfylle (**).

Randverdiproblemet (**) er løst i Kreyszig, se der for detaljer i utregningen. Innsetting av $v(x,y)=F(x)G(t)$ i (**) gir

$$\begin{aligned}G'(t)&=kG(t)&&\text{for }t>0,\\ F''(t)&=kF(t)&&\text{for }0<x<1,\\ F(0)&=0=F(1),\end{aligned}$$

der $k$ er en konstant. Likningene for $F$ har bare løsning forskjellig fra $0$ når $k=-n^2\pi^2$ for $n\in\mathbb{N}$, og da er

$$F_n(x)=K_n\sin(n\pi x)\quad\text{og}\quad G_n(t)=\bar{K}_ne^{-n^2\pi^2t},$$

for vilkårlige konstanter $K_n,\bar{K}_n$. Alle løsninger på formen $v(x,y)=F(x)G(t)$ er da gitt ved

$$v_n(x,t)=F_n(x)G_n(t)=\underline{\underline{A_ne^{-n^2\pi^2t}\sin(n\pi x)}},\quad n\in\mathbb{N},$$

og der $A_n=K_n\bar{K}_n$ er en vilkårlig konstant.

**c)** Husk at $a=-1$ og $b=1$, slik at $u(x,t)=v(x,t)-[-1+2x]$. Vi ser da at $v$ løser randverdiproblemet (**) med initialbetingelse

$$v(x,0)=u(x,0)+[-1+2x]=\sin(\pi x)+[-1+2x].\tag{1}$$

Fra b) og superposisjon har vi følgende kandidat til løsning av (**) og (1),

$$v(x,t)=\sum_{n=1}^\infty A_ne^{-n^2\pi^2t}\sin(n\pi x).$$

Ved å sette $t=0$ får vi

$$\sum_{n=1}^\infty A_n\sin(n\pi x)=v(x,0)=\sin\pi x+[-1+2x].\tag{2}$$

Nå finner vi Fourier sin-rekken til $-1+2x$ for $0\le x\le 1$:

$$-1+2x=\sum_{n=1}^n b_n\sin(n\pi x)\quad\text{for}\quad 0<x<1\quad\text{og}\quad b_n=2\int_0^1(-1+2x)\sin(n\pi x)\,dx.$$

Delvis integrasjon gir at $b_n=\frac{2}{n\pi}(1+(-1)^n)$ for $n\in\mathbb{N}$, og fra (2) ser vi dermed at må vi velge

$$A_1=b_1+1\quad\text{og}\quad A_n=b_n\text{ for }n>1.$$

Dvs. løsningen $v$ av (**) og (1) er

$$v(x,t)=e^{-\pi^2t}\sin\pi x+\frac{4}{\pi}\sum_{m=1}^\infty\frac{1}{2m}e^{-4m^2\pi^2t}\sin(2m\pi x).$$

Her har vi brukt at $b_n=0$ for $n$ odde og $b_n=\frac{4}{n\pi}$ for $n(=2m)$ like. Løsningen $u$ av (*) og (***) er da

$$u(x,t)=v(x,t)-[-1-2x].$$

*Kjeldevarsel: løsningsforslaget har forteiknsfeil i c) (errataet notert på old_exams-sida for dette settet). Sidan $v=u-[-1+2x]$ frå b), bør opningslinja i c) lesast $u(x,t)=v(x,t)+[-1+2x]$ og initialbetingelsen i (1) vere $v(x,0)=\sin(\pi x)-[-1+2x]=\sin(\pi x)+(1-2x)$. Dei trykte koeffisientane $b_n=\frac{2}{n\pi}(1+(-1)^n)$ er korrekte for funksjonen $1-2x$ (kontrollrekna med sympy; for $-1+2x$, som teksten seier rekkja skal finne, skulle det stått $-\frac{2}{n\pi}(1+(-1)^n)$) — altså motseier koeffisientane funksjonsnamnet dei utviklar. Den siste linja trykkjer i tillegg $u(x,t)=v(x,t)-[-1-2x]$, som verken stemmer med opningslinja $[-1+2x]$ på same side eller med det rette $u=v+[-1+2x]$. Teksten over fylgjer løsningsforslaget ordrett.*

Kildesett: course=TMA4135 term=host year=2006 problem=3 file=tma4135_06h.pdf
