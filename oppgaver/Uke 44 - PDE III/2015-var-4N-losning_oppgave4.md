### **Løsning til Oppgave 4**

a) Med $u(x,t)=X(x)T(t)$ blir den partielle differensialligningen til

$$\frac{T'(t)}{T(t)}=\frac{X''(x)}{X(x)}.$$

Siden venstre side ikke avhenger av $x$, og høyre side ikke avhenger av $t$, må begge sider være lik en konstant. Vi får derfor de to ODE-ene

$$X''(x)-kX(x)=0 \tag{1}$$

$$T'(t)-kT(t)=0 \tag{2}$$

for en ukjent konstant $k$.

Vi har tre mulighet for $k$:

- $k=0$: Da er løsningen av ligning (1) $X(x)=Ax+B$. Venstre randbetingelse gir da at $A=0$, og vi har derfor konstantløsning.
- $k>0$: Da er løsningen av ligning (1)

$$X(x)=Ce^{\sqrt kx}+De^{-\sqrt kx}.$$

Dermed er

$$X'(x)=C\sqrt ke^{\sqrt kx}-D\sqrt ke^{-\sqrt kx},$$

og venstre randbetingelse gir $0=X'(0)=C-D$, så $C=D$ Høyre randbetingelse gir så

$$0=X'(\pi)=C\sqrt k\left(e^{\sqrt k\pi}-e^{-\sqrt k\pi}\right)$$

som bare kan skje dersom $C=0$ Vi har derfor bare triviell løsning i dette tilfellet.

- $k<0$: Da er løsningen av ligning (1)

$$X(x)=M\cos\sqrt{-k}x+N\sin\sqrt{-k}x,$$

så

$$X'(x)=-M\sqrt{-k}\sin\sqrt{-k}x+N\sqrt{-k}\cos\sqrt{-k}x.$$

Venstre randbetingelse gir $0=X'(0)=N\sqrt{-k}$, som vil si $N=0$. Høyre randbetingelse gir

$$0=X'(\pi)=-M\sqrt{-k}\sin\sqrt{-k}\pi.$$

Dette er oppfylt hvis $M=0$ (triviell løsning) eller hvis $\sqrt{-k}\pi=\pi,2\pi,3\pi,\ldots$. Vi har derfor $X_n(x)=M_n\cos nx$ for $n=0,1,2,...$ ($n=0$ tar hånd om konstantløsningen). Ligning (2) har løsning

$$T_n(t)=Ee^{-n^2t},$$

så

$$u_n(x,t)=X_n(x)T_n(t)=A_ne^{-n^2t}\cos nx$$

for (omdøpte og sammenslåtte) konstanter $A_n$.

b) Fra oppgave 4a vet vi at den generelle løsningen er

$$u(x,t)=\sum_{n=0}^{\infty}A_ne^{-n^2t}\cos nx.$$

Initialbetingelsen er

$$u(x,0)=\sum_{n=0}^{\infty}A_n\cos nx=(\cos 2x-1)^2$$

Dette viser at $A_n$ er Fourier-cosinusrekke-koeffisientene til (den like periodiske utvidelsen til) funksjonen på høyre side. Skriver vi denne om som

$$(\cos 2x-1)^2=\frac{3}{2}-2\cos 2x+\frac{1}{2}\cos 4x,$$

kan koeffisientene leses rett av: $A_0=3/2$, $A_2=-2$, $A_4=1/2$, og $A_n=0$ for $n\ne0,2,4$. Dermed blir løsningen

$$u(x,t)=\frac{3}{2}-2e^{-4t}\cos 2x+\frac{1}{2}e^{-16t}\cos 4x.$$

Kildesett: course=TMA4123 term=var year=2015 problem=4 file=eksamen-nb.pdf
