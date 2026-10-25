### **Løsning til Oppgave 4**

**a)** En skisse av funksjonen er gjengitt i figuren under.

[Figur: Grafen til $f$: for $x$ fra $-3\pi$ til $3\pi$ ei sinusboge av høyde $1$ på kvart intervall $(2k\pi,(2k+1)\pi)$ (positiv del av $\sin x$), og $f=0$ elles; $x$-aksen merkt $-3\pi$, $-2\pi$, $-\pi$, $0$, $\pi$, $2\pi$, $3\pi$, $y$-aksen merkt $0.2$–$1$.]

Fourierkoeffisientene er gitt ved

$$a_0=\frac{1}{2\pi}\int_0^{\pi}\sin(x)dx=\frac{1}{\pi}$$

$$a_n=\frac{1}{\pi}\int_0^{\pi}\sin(x)\cos(nx)dx=\frac{1}{\pi}\int_0^{\pi}\frac{1}{2}\big(\sin(1-n)x+\sin(1+n)x\big)dx$$

$$=\begin{cases}0,&n=1\\ -\frac{1}{\pi}\frac{(-1)^n+1}{n^2-1},&n\ge 2\end{cases}$$

$$b_n=\frac{1}{\pi}\int_0^{\pi}\sin(x)\sin(nx)dx=\frac{1}{\pi}\int_0^{\pi}\frac{1}{2}\big(\cos(1-n)x-\cos(1+n)x\big)dx$$

$$=\begin{cases}\frac{1}{2},&n=1,\\ 0,&n\ge 2.\end{cases}$$

Alle $a_n$ for $n$ odder er altså lik 0. Sett $n=2m$, og vi får

$$f(x)\sim\frac{1}{\pi}+\frac{1}{2}\sin(x)-\frac{2}{\pi}\sum_{m=1}^{\infty}\frac{1}{4m^2-1}\cos 2mx\,.$$

**b)** La $u(x,t)=G(t)F(x)$ slik at

$$u_t=\dot{G}\cdot F,\qquad u_{xx}=G\cdot F''$$

med $\dot{G}=dG/dt$, $F''=d^2F/dx^2$. Sett inn i ligningen, del med $F\cdot G$ på begge sider, slik at

$$\frac{\dot{G}}{G}=\frac{F''}{F}=k$$

der $k$ er en foreløbig ukjent konstant. Vi ender altså med 2 første ordens differensialligninger

$$F''=kF,\qquad\dot{G}=kG.$$

For den første av disse har vi også randbetingelser, siden

$$u_x(0,t)=u_x(\pi,t)=0,\qquad\text{må}\qquad F'(0)=F'(\pi)=0,$$

så vi løser ligningen for $F$ først. Løsningen av denne avhenger av vår ukjente konstant $k$, og følgende 3 tilfeller kan oppstå:

- $k=\gamma^2>0$. Da er

$$F(x)=C_1e^{\gamma x}+C_2e^{-\gamma x},$$

for vilkårlige konstanter $C_1$ og $C_2$. Setter inn randbetingelsene:

$$\begin{aligned}F'(x)&=C_1\gamma e^{\gamma x}-C_2\gamma e^{-\gamma x}\\ F'(0)&=\gamma(C_1-C_2)=0&&\Rightarrow\qquad C_1=C_2\\ F'(\pi)&=\gamma(C_1e^{\gamma\pi}-C_2e^{-\gamma\pi})=0&&\Rightarrow\qquad C_1(e^{\gamma\pi}-e^{-\gamma\pi})=0\,\Rightarrow\,C_1=0.\end{aligned}$$

For $k>0$ er det altså bare den trivielle løsningen $F=0$ som både oppfyller differensialligningen for $F$ og grensebetingelsene.

- $k=0$. I dette tilfellet er løsningene gitt ved

$$F=B_0x+A_0.$$

Hvor igjen $A_0$ og $B_0$ er vilkårlige konstanter. Setter vi inn randbetingelsene, får vi

$$F'=B_0,\qquad F'(0)=B_0=0,\qquad F'(\pi)=B_0=0.$$

Løsningen $F(x)=A_0$ tilfredstiller altså differensialligningen for $F$ og randbetingelsene for alle konstanter $A_0$.

- $k=-\mu^2<0$. Gentar vi prosessen får vi løsningen

$$F(x)=A\cos\mu x+B\sin\mu x$$

med vilkårlige konstanter $A$ og $B$. Randbetingelsene:

$$\begin{aligned}F'(x)&=\mu(-A\sin\mu x+B\cos\mu x)\\ F'(0)&=\mu B=0,&&\Rightarrow\qquad B=0\\ F'(\pi)&=0=-A\sin\mu\pi=0&&\end{aligned}$$

Den siste av disse er oppfylt dersom $\mu=n\pi$, der $n$ er et heltall, dvs. $n=1,2,3,\ldots$.

Vi kan da løse differensialligningen for $G$, som med $k=-n^2$ har løsningen

$$G_n(t)=C_ne^{-n^2t}.$$

Det betyr at

$$u_n(x,t)=e^{-n^2t}\cos nx,\qquad n=0,1,2,3,\ldots$$

alle er løsninger av den partielle differensialligningen med grensebetingelser. Den generelle løsningen er da

$$u(x,t)=\sum_{n=1}^{\infty}A_ne^{-n^2t}\cos nx.$$

**c)** Vi skal altså bestemme $A_n$, $n=0,1,2,\ldots$, slik at

$$u(x,0)=\sin x=\sum_{n=0}^{\infty}A_n\cos nx,\qquad 0<x<\pi.$$

Fra punktet **a)** vet vi at

$$\sin x=\frac{1}{\pi}+\frac{1}{2}\sin(x)-\frac{2}{\pi}\sum_{m=1}^{\infty}\frac{1}{4m^2-1}\cos 2mx$$

for $0<x<\pi$. Denne må skrives om litt: ta sinusleddet på høyre side og flytt over på venstre side av likhetstegnet, og multipliser med 2. Da er

$$\sin x=\frac{2}{\pi}-\frac{4}{\pi}\sum_{m=1}^{\infty}\frac{1}{4m^2-1}\cos 2mx,\qquad 0<x<\pi.$$

Sammenlign ledd for ledd: $A_0=\frac{2}{\pi}$, $A_n=0$ for $n$ odde, og $A_n=\frac{4}{\pi(n^2-1)}$ for $n$ like, dvs.

$$u(x,t)=\frac{2}{\pi}-\frac{4}{\pi}\sum_{m=1}^{\infty}\frac{1}{4m^2-1}e^{-4m^2t}\cos 2mx.$$

*Kjeldevarsel: forteiknet i $A_n=\frac{4}{\pi(n^2-1)}$ i løysingsforslaget er feil — det stemmer ikkje med cosinusrekkja for $\sin x$ like over, og strir mot det avsluttande uttrykket for $u(x,t)$, som korrekt har $-\frac{4}{\pi}$ foran summen (retta verdi: $A_n=-\frac{4}{\pi(n^2-1)}$ for like $n$).*

Kildesett: course=TMA4135 term=kont year=2012 problem=4 file=tma4135_12k.pdf
