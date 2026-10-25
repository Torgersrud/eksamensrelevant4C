### **Løsning til Oppgave 4**

Vi antar løsningen kan skrives

$$u(x,t)=F(x)G(t)$$

og setter inn i varmelikningen, slik at

$$F(x)G'(t)=F''(x)G(t).$$

Vi deler på $F(x)G(t)$, og får

$$\frac{G'(t)}{G(t)}=\frac{F''(x)}{F(x)}$$

Siden den ene siden kun avhenger av $t$ og den andre kun av $x$, må begge sider være konstante, slik at

$$\frac{G'(t)}{G(t)}=\frac{F''(x)}{F(x)}=k.$$

Vi begynner med å analysere

$$F''(x)-kF(x)=0.$$

Kan $k=0$? Nei. Vi får i så fall $F(x)=Ax+B$ og $G(t)=C$, og randkravene blir tilfredsstilt om $A=0$. Men initialkravet kan vi bare glemme, for løsningen $u(x,t)$ blir en konstant.

Vi prøver $k>0$. I så fall blir $G(t)=Ae^{kt}$. Siden $k>0$, vil vi få

$$\lim_{t\to\infty}|u(x,t)|=\lim_{t\to\infty}|F(x)|e^{kt}=\infty.$$

Denne løsningen er åpenbart ufysisk, for dette er en situasjon med en stang som er isolert i endepunktene, og varmeenergien tilstede ved $t=0$ skal helst fordele seg jevnt på stangen, ikke gå mot uendelig. Så om vi skulle slumpe til å finne en løsning av problemet med $k>0$, vil den løsningen ikke ha noen fysisk relevans.

Altså prøver vi $k<0$. Løsningen på $F''(x)-kF(x)=0$ blir

$$F(x)=A\cos\sqrt{-k}x+B\sin\sqrt{-k}x.$$

Den ene randbetingelsen $u_x(0,t)=0$ gir

$$u(0,t)=G(t)F'(0)=G(t)\left(-A\sin\sqrt{-k}\cdot 0+B\cos\sqrt{-k}\cdot 0\right)=0$$

slik at $B=0$. Den andre randbetingelsen gir

$$u(\pi,t)=G(t)F'(\pi)=-AG(t)\sin\sqrt{-k}\pi=0,$$

så setter vi $\sqrt{-k}=n$, eller $k=-n^2$, får vi den tilfredsstilt. Vi kan videre bestemme $G$ fra $G'(t)+n^2G(t)=0$, og får

$$G(t)=B_ne^{-n^2t}$$

Alt i alt får vi en familie av løsninger

$$u_n(x,t)=B_ne^{-n^2t}\cos nx,$$

som alle tilfredsstiller varmelikningene og randbetingelsene. Nå er det langt fra trivielt å vise at vi kan legge sammen alle disse

$$u(x,t)=\sum_{n=0}^{\infty}u_n(x,t)=\sum_{n=0}^{\infty}B_ne^{-n^2t}\cos nx,$$

og i det hele tatt få en deriverbar funksjon. Men det kan vi. Vi hopper over hele problemstillingen, og går umiddelbart videre til å takle initialkravet $u(x,0)=e^{-x}$, som gir

$$u(x,0)=\sum_{n=0}^{\infty}B_n\cos nx=e^{-x},$$

altså må $B_n$ være koeffisientene i cosinusrekken til $e^{-x}$. Denne rekken fant vi i oppgave 2b, og vi kan skrive opp løsningen

$$u(x,t)=\frac{1-e^{-\pi}}{\pi}+\frac{2}{\pi}\sum_{n=1}^{\infty}\frac{(1-e^{-\pi}(-1)^n)}{1+n^2}e^{-n^2t}\cos nx.$$

Kildesett: course=TMA4125 term=var year=2019 problem=4 file=eksamen-TMA4125-v19-BM.pdf
