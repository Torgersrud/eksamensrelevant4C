### **Løsning til Oppgave 5**

**a)** $u(x,t)=F(x)G(t)$ innsatt i PDE-en gir

$$F''(x)G(t)+4F(x)G(t)=F(x)G'(t),$$

som blir

$$\frac{F''(x)}{F(x)}=\frac{G'(t)}{G(t)}-4.$$

Siden venstre side er uavhengig av $t$ og høyre side er uavhengig av $x$, er begge sider lik en konstant $k$. Dette gir oss to ODE-er:

$$F''(x)-kF(x)=0 \qquad (1)$$

$$G'(t)-(k+4)G(t)=0. \qquad (2)$$

Vi betrakter først ligning (1). Dersom $k>0$, er dens løsninger på formen

$$F(x)=Ae^{\sqrt{k}x}+Be^{-\sqrt{k}x}.$$

Venstre randbetingelse gir $0=u(0,t)=F(0)G(t)$ for alle $t$, som gir $0=F(0)=A+B$, altså $A=-B$, så

$$F(x)=A(e^{\sqrt{k}x}-e^{-\sqrt{k}x}).$$

Nå er $F'(x)=\sqrt{k}A(e^{\sqrt{k}x}+e^{-\sqrt{k}x})$, så høyre randbetingelse gir $0=F'(\pi)$, som gir $A=0$. Tilfellet $k>0$ gir altså bare trivielle løsninger.

Hvis $k=0$, er løsningene av ligning (1) på formen

$$F(x)=Ax+B.$$

Venstre randbetineglse gir $0=F(0)=B$, altså $F(x)=Ax$, mens høyre randbetingelse gir $0=F'(\pi)=A$, så også dette tilfellet gir kun trivielle løsninger.

Hvis $k<0$, er løsningene av ligning (1) på formen

$$F(x)=A\cos\sqrt{-k}x+B\sin\sqrt{-k}x.$$

Venstre randbetingelse gir $0=F(0)=A$, altså $F(x)=B\sin\sqrt{-k}x$. Da er $F'(x)=\sqrt{-k}B\cos\sqrt{-k}x$, så høyre randbetingelse gir

$$0=F'(\pi)=\sqrt{-k}B\cos\sqrt{-k}\pi.$$

For å unngå triviell løsning ($B=0$), kan vi velge $\sqrt{-k}=n/2$ for $n=1,3,5,\ldots$ . Løsning av ligning (1) er altså

$$F_n(x)=B_n\sin\left(\frac{2n-1}{2}x\right)$$

for $n=1,2,3,\ldots$ . Med $k=-(2n-1)^2/4$ er løsning av ligning (2)

$$G_n(t)=A_ne^{(4-(2n-1)^2/4)t}.$$

Generell løsning av PDE-en er derfor

$$u(x,t)=\sum_{n=1}^{\infty}F_n(x)G_n(t)=\sum_{n=1}^{\infty}C_ne^{(4-(2n-1)^2/4)t}\sin\left(\frac{2n-1}{2}x\right).$$

**b)** Initialbetingelsen gir

$$\sin\left(\frac{3}{2}x\right)+2\sin\left(\frac{5}{2}x\right)+3\sin\left(\frac{7}{2}x\right)=u(x,0)=\sum_{n=1}^{\infty}C_n\sin nx.$$

Med andre ord er $C_1$, $C_2$, … Fourier-sinus-koeffisientene til funksjonen på venstre side i ligningen over. Disse kan regnes ut på vanlig måte, eller vi kan lese dem av direkte siden venstre side allerede er en Fourier-sinus-rekke:

$$C_2=1,\qquad C_3=2,\qquad C_4=3$$

og $C_n=0$ ellers. Løsningen vi søker er derfor

$$u(x,t)=e^{7t/4}\sin\left(\frac{3}{2}x\right)+2e^{-9t/4}\sin\left(\frac{5}{2}x\right)+3e^{-33t/4}\sin\left(\frac{7}{2}x\right).$$

**c)** (Besvarelsen er her mye mer ordrik enn det som kreves på eksamen. Den er kopiert fra LF til øving 12, med de nødvendige modifikasjoner.)

Vi går frem som i forelesningene og http://www.math.ntnu.no/emner/TMA4135/2015h/notater/crank-nicolson/cn.pdf. Notatet håndterer jo egentlig den vanlige varmeledningsligningen, altså den uten en ekstra $4u(x,t)$, men fremgangsmåten er nøyaktig den samme!

Del $[0,\pi]$ inn i intervaller med noder $x_0,x_1,\ldots,x_N$ i en avstand $h$ fra hverandre, altså $h=\pi/N$. Ved å bruke sentraldifferenstilnærmingen[^1],

$$\frac{\partial^2 u}{\partial x^2}u(x,t)\approx\frac{1}{h^2}\big(u(x+h,t)-2u(x,t)+u(x-h,t)\big),$$

forvandler vi PDE-en fra oppgaven til et system av ligninger

$$\frac{\partial u}{\partial t}(ih,t)\approx\frac{1}{h^2}\big(u(ih+h,t)-2u(ih,t)+u(ih-h,t)\big)+4u(ih,t)$$

for $0<i<N$. Hvis vi skriver $v_i(t)$ for vår tilnærming av $u(ih,t)$, kan dette systemet skrives

$$v_i'(t)=\frac{1}{h^2}\big(v_{i+1}(t)-2v_i(t)+v_{i-1}(t)\big)+4v_i(t)$$

for $0<i<N$. Med denne notasjonen blir randbetingelsene $v_0(t)=u(0,t)=0$ og $v_N(t)=u(Nh,t)=u(\pi,t)=0$.

Med $\mathbf v(t)=(v_1(t),v_2(t),\ldots v_{N-1}(t))$ kan vi skrive systemet som

$$\mathbf v'(t)=\frac{1}{h^2}\begin{pmatrix}v_2(t)-2v_1(t)\\ v_3(t)-2v_2(t)+v_1(t)\\ \vdots\\ v_{N-1}(t)-2v_{N-2}(t)+v_{N-3}(t)\\ -2v_{N-1}(t)+v_{N-2}(t)\end{pmatrix}+4\mathbf v(t)=\mathbf f(t,\mathbf v(t)). \qquad (3)$$

Ligning (3) kan løses med en hvilken som helst Runge–Kutta-metode for systemer av ODE-er. Crank–Nicolson metode fås fra RK-metoden som har Butcher-tabell

$$\begin{array}{c|cc} 0 & 0 & \\ 1 & 1/2 & 1/2 \\ \hline & 1/2 & 1/2 \end{array}.$$

Skriv $k$ for tidsskrittlegnden, og tidsskrittindeks som superskript (altså $\mathbf v^j\approx\mathbf v(jk)$). Da er denne metoden

$$\mathbf v^{j+1}=\mathbf v^j+\frac{k}{2}\mathbf f(t_j,\mathbf v^j)+\frac{k}{2}\mathbf f(t_{j+1},\mathbf v^{j+1}).$$

Anvendt med $\mathbf f$ fra ligning (3) får vi

$$\begin{pmatrix}v^{j+1}_1\\ v^{j+1}_2\\ \vdots\\ v^{j+1}_{N-2}\\ v^{j+1}_{N-1}\end{pmatrix}=\begin{pmatrix}v^{j}_1\\ v^{j}_2\\ \vdots\\ v^{j}_{N-2}\\ v^{j}_{N-1}\end{pmatrix}+\frac{k}{2h^2}\begin{pmatrix}v^{j}_2-2v^{j}_1\\ v^{j}_3-2v^{j}_2+v^{j}_1\\ \vdots\\ v^{j}_{N-1}-2v^{j}_{N-2}+v^{j}_{N-3}\\ -2v^{j}_{N-1}+v^{j}_{N-2}\end{pmatrix}+2k\begin{pmatrix}v^{j}_1\\ v^{j}_2\\ \vdots\\ v^{j}_{N-2}\\ v^{j}_{N-1}\end{pmatrix}$$

$$+\frac{k}{2h^2}\begin{pmatrix}v^{j+1}_2-2v^{j+1}_1)\\ v^{j+1}_3-2v^{j+1}_2+v^{j+1}_1\\ \vdots\\ v^{j+1}_{N-1}-2v^{j+1}_{N-2}+v^{j+1}_{N-3}\\ -2v^{j+1}_{N-1}+v^{j+1}_{N-2}\end{pmatrix}+2k\begin{pmatrix}v^{j+1}_1\\ v^{j+1}_2\\ \vdots\\ v^{j+1}_{N-2}\\ v^{j+1}_{N-1}\end{pmatrix}.$$

Omformer vi til en matriseligning, og innfører $r=k/h^2$, får vi det tridiagonale ligningssystemet

$$\begin{pmatrix}1+r-2k & -r/2 & & \\ -r/2 & 1+r-2k & -r/2 & \\ & -r/2 & \ddots & \ddots & \\ & & \ddots & \ddots & -r/2 \\ & & & -r/2 & 1+r-2k\end{pmatrix}\begin{pmatrix}v^{j+1}_1\\ v^{j+1}_2\\ \vdots\\ v^{j+1}_{N-2}\\ v^{j+1}_{N-1}\end{pmatrix}=(1+2k)\begin{pmatrix}v^{j}_1\\ v^{j}_2\\ \vdots\\ v^{j}_{N-2}\\ v^{j}_{N-1}\end{pmatrix}+\frac{r}{2}\begin{pmatrix}v^{j}_2-2v^{j}_1\\ v^{j}_3-2v^{j}_2+v^{j}_1\\ \vdots\\ v^{j}_{N-1}-2v^{j}_{N-2}+v^{j}_{N-3}\\ -2v^{j}_{N-1}+v^{j}_{N-2}\end{pmatrix}. \qquad (4)$$

Vi skritter fra tidsskritt $j$ til $j+1$ ved å løse dette systemet.

[^1]: Som i forelesningene: legg sammen Taylor-rekken for $u(x+h,t)$ og for $u(x-h,t)$ slik at de odde potensene av $h$ forsvinner, og se bort ifra ledd av orden større enn $h^2$.

Kildesett: course=TMA4135 term=host year=2015 problem=5 file=tma4135_15h.pdf
