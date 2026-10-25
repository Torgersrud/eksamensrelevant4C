### **Løsning til Oppgave 4**

a)  Fourier-sinus rekka finner en ved å utvide $g(x)$ til en odde funksjon $\tilde{g}(x)$ på intervallet $[-\pi,\pi]$ og deretter bestemme Fourier-rekka til $\tilde{g}(x)$. Vi får da

$$\tilde{g}(x)=\left\{\begin{array}{rl}1,&x\in(0,\pi]\\ -1,&x\in[-\pi,0)\end{array}\right.$$

$$\tilde{g}(x)=\sum_{n=1}^{\infty}b_n\sin(nx),$$

$$b_n=\frac{1}{\pi}\int\limits_{-\pi}^{\pi}\tilde{g}(x)\sin(nx)dx=\frac{2}{\pi}\int\limits_0^{\pi}\sin(nx)dx=\frac{-2}{n\pi}\cos(nx)\left|_{x=0}^{x=\pi}\right.$$

$$=\frac{-2}{n\pi}[(-1)^n-1]=\left\{\begin{array}{ll}\frac{4}{n\pi},&\mathrm{n\ odde}\\ 0,&\mathrm{n\ jevn}\end{array}\right.$$

Derfor er Fourier-sinus rekka til g(x) gitt ved

$$g(x)=\frac{4}{\pi}\sum_{\mathrm{n\ odde}}\frac{\sin(nx)}{n}=\frac{4}{\pi}\sum_{k=0}^{\infty}\frac{\sin((2k+1)x)}{2k+1}$$

Videre er, ifølge Parsevals identitet,

$$2=\frac{1}{\pi}\int\limits_{-\pi}^{\pi}\tilde{g}(x)^2dx=\sum b_n^2=\frac{16}{\pi^2}\sum_{k=0}^{\infty}\frac{1}{(2k+1)^2}$$

$$\sum_{k=0}^{\infty}\frac{1}{(2k+1)^2}=\frac{\pi^2}{8}$$

b)  Vi ser på bølgeligningen $u_{tt}=4u_{xx}$ med rand-og initialbetingelser

$$(i)\ \ u(0,t)=u(\pi,t)=0$$

$$(ii)\ \ u(x,0)=0,u_t(x,0)=1$$

og benytter som vanlig separasjon av variable som først gir oss alle løsninger på forma $u(x,t)=F(x)G(t)$. Det gir

$$F(x)G''(t)=4F''(x)G(t)$$

$$\frac{F''(x)}{F(x)}=\frac{G''(t)}{4G(t)}=k\ (\mathrm{konstant})$$

eller

$$(1)\ F''(x)=kF(x),\ \ (2)\ G''(t)=4kG(t)$$

La oss først bestemme de løsningene av disse differensialligningene som er slik at $u=F(x)G(t)$ oppfyller randbetingelsen (i). Vi må ha da

$$F(0)=F(\pi)=0$$

og differensialligningen (1) må ha $k=-\lambda^2<0$ ($\lambda>0$).Løsningen må være på forma

$$F(x)=\sin(\lambda x),\ \mathrm{med}\ \sin(\lambda\pi)=0$$

Det gir $\lambda=1,2,3,...,n,...$og vi setter $F_n(x)=\sin(nx)$.

Dernest løser vi differensialligningen (2) for $G(t)$, med $k=-n^2$, som gir løsningene

$$G_n(t)=A_n\cos(2nt)+B_n\sin(2nt)$$

Initialbetingelsen (ii) gir at $G_n(0)=0$, $G_n'(0)=1$, derav $A_n=0$. Vi prøver derfor å finne en løsning på forma

$$u(x,t)=\sum_{n=1}^{\infty}B_nF_n(x)G_n(t)=\sum_{n=1}^{\infty}B_n\sin(nx)\sin(2nt)$$

Den siste initialbetingelsen $u_t(x,0)=1$ gir da

$$1=\sum_{n=1}^{\infty}2nB_n\sin(nx)\cos(2nt)|_{t=0}=\sum_{n=1}^{\infty}2nB_n\sin(nx)$$

som forteller oss at rekka på høyre side må være Fourier-sinus rekka til den konstante funksjonen 1 på intervallet $[0,\pi]$, nemlig funksjonen $g(x)$ i punkt a). Følgelig må

$$2nB_n=b_n=\left\{\begin{array}{ll}\frac{4}{n\pi},&\mathrm{n\ odde}\\ 0,&\mathrm{n\ jevn}\end{array}\right.$$

$$B_n=\frac{b_n}{2n}=\left\{\begin{array}{ll}\frac{2}{n^2\pi},&\mathrm{n\ odde}\\ 0,&\mathrm{n\ jevn}\end{array}\right.$$

Endelig løsning er

$$u(x,t)=\frac{2}{\pi}\sum_{n\ \mathrm{odde}}\frac{1}{n^2}\sin(nx)\sin(2nt)$$

c)  De tidsuavhengige løsningene $u(x,t)=v(x)$ av ligningen $u_{tt}+8=4u_{xx}$ får en ved å ignorere leddet $u_{tt}$. Da må $v(x)$ være en løsning av ligningen $v''(x)=2$, dvs.

$v(x)=x^2+bx+c$. Med randbetingelsen $v(0)=v(\pi)=0$ blir da

$$v(x)=x(x-\pi)$$

Merk at ligningen $u_{tt}+8=4u_{xx}$ er inhomogen, og $v(x)$ er en (partikulær) løsning av denne. Ved å fjerne konstantleddet 8 får en den tilhørende homogene ligningen $u_{tt}=4u_{xx}$. La nå $w(x,t)$ være den løsningen av denne ligningen som vi fant i punkt b), og sett

$$u(x,t)=w(x,t)+v(x)$$

$$=\frac{2}{\pi}\sum_{n\ \mathrm{odde}}\frac{1}{n^2}\sin(nx)\sin(2nt)+x(x-\pi)$$

Siden $w(x,t)$ tilfredsstiller betingelsene i punkt b), er det nå enkelt å sjekke at funksjonen $u(x,t)$ tilfredsstiller betingelsene (i), (ii) gitt i punkt c) i oppgaven.

Kildesett: course=TMA4135 term=host year=2011 problem=4 file=tma4135_11h.pdf
