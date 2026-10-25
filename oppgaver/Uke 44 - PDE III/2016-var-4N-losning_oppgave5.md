### **Løsning til Oppgave 5**

**a)** Vi har

$$b_n=\frac{2}{\pi}\int\limits_0^\pi\left(\pi x-x^2\right)\sin nx\mathrm{d}x=\frac{2}{\pi}\left\{\left[\ -\left(\pi x-x^2\right)\frac{\cos nx}{n}\ \right]_0^\pi+\frac{1}{n}\int\limits_0^\pi(\pi-2x)\cos nx\mathrm{d}x\right\}=$$

$$\frac{2}{\pi}\left\{0+\frac{1}{n}\left(\left[\left(\pi-2x\right)\frac{\sin nx}{n}\ \right]_0^\pi+\frac{2}{n}\int\limits_0^\pi\sin nx\mathrm{d}x\right)\right\}=-\frac{4}{\pi n^3}\left[\cos nx\ \right]_0^\pi=\frac{4}{\pi n^3}\left(1-\cos n\pi\right)\ .$$

Altså er

$$b_n=\left\{\begin{array}{ll}\displaystyle\frac{8}{\pi n^3},&\text{for }n\text{ odde}\\[8pt] 0,&\text{for }n\text{ like}\end{array}\right.$$

Dette gir Fourier sinus-rekke

$$\frac{8}{\pi}\sum_{m=0}^{\infty}\frac{\sin\left(2m+1\right)x}{\left(2m+1\right)^3}\,.$$

Siden den odde periodiske utvidelsen av $f(x)$, $f_{op}(x)$, er kontinuerlig, vil Fourier sinus-rekka til $f(x)$ konvergerer mot $f_{op}(x)$. Denne $2\pi-$ periodiske funksjonen er plottet for $x$ mellom $-2\pi$ og $2\pi$ i figuren under:

[Figur: Plott med tittelen "Fourier sinus-rekka til f(x)". Ei glatt, odd bølgje frå $x=-2\pi$ til $x=2\pi$, med nullpunkt i $0$, $\pm\pi$ og $\pm2\pi$, positiv topp på om lag $2.5$ ved $x=\frac{\pi}{2}$ og $x=-\frac{3\pi}{2}$, og tilsvarande botn på om lag $-2.5$ ved $x=-\frac{\pi}{2}$ og $x=\frac{3\pi}{2}$.]

**b)**

$u(x,t)=F(x)G(t)$ innsatt i differensialligninga gir

$$\frac{G'(t)}{G(t)}=\frac{F''(x)}{F(x)}=k\ .$$

Altså er

$$\begin{array}{c}F''-kF=0\ ,\\[6pt] G'-kG=0\end{array}$$

Randbetingelsene gir $F(0)=F(\pi)=0$ .

Differensialligninga for $F$ har karakteristisk ligning

$r^2-k=0$ . Drøfter ulike $k$ :

$k=\lambda^2>0$, $\lambda>0$ :

Da er $F(x)=C_1e^{\lambda x}+C_2e^{-\lambda x}$ . Vi har $0=F(0)=C_1+C_2\Leftrightarrow C_2=-C_1$ .

Dette gir $F(x)=C_1\left(e^{\lambda x}-e^{-\lambda x}\right)$ . Men $0=F(\pi)=C_1\left(e^{\lambda\pi}-e^{-\lambda\pi}\right)$ er umulig for $C_1\neq0$ og $\lambda>0$ .

$k=0$ : Da er $F(x)=C_1x+C_2$ , og $F(0)=F(\pi)=0$ er umulig for ikke-triviell $F(x)$ .

$k=-\lambda^2<0$, $\lambda>0$ : Vi får $F(x)=C_1\cos\lambda x+C_2\sin\lambda x$ . $F(0)=0$ gir $C_1=0$ . Altså er $F(x)=C_2\sin\lambda x$ . For $\lambda>0$ er $F(\pi)=0$ oppfylt hvis og bare hvis $\lambda=n\pi$, $n=1,2,3,\ldots$, dvs. $k_n=-n^2$ . Vi får $F_n(x)=\sin nx$, $n=1,2,3,..$ . Korresponderende $G_n(t)$ oppfyller $G'+n^2G=0$ , som gir $G_n(t)=A_ne^{-n^2t}$ . Altså er

$$u_n(x,t)=A_n\,\mathrm{e}^{-n^2t}\sin nx,\ n=1,2,3,..$$

alle mulige ikke-trivielle løsninger på randverdiproblemet på formen $F(x)G(t)$ . Her er $A_n$ konstanter.

**c)**

Steady state løsningen, $u_s(x)$, innsatt i differensialligninga gir

$$0=u_s''(x)+2\Leftrightarrow u_s(x)=-x^2+C_1x+C_2\,.$$

Randverdiene $u_s(0)=u_s(\pi)=0$ gir $C_1=\pi$, $C_0=0$ . Altså er

$$u_s(x)=\pi x-x^2\,.$$

Skriver

$u(x,t)=u_s(x)+v(x,t)$ , og bestemmer randverdiproblemet for $v(x,t)$ :

Innsatt i differensialligninga gir dette

$\left(u_s(x)+v(x,t)\right)_t=\left(u_s(x)+v(x,t)\right)_{xx}+2\Leftrightarrow\ v_t(x,t)=-2+v_{xx}(x,t)+2\Leftrightarrow\ v_t=v_{xx}$ .

Randbetingelsene: Siden $u_s(0)=u_s(\pi)=0$ får vi

$0=u(0,t)=u_s(0)+v(0,t)=v(0,t)\Leftrightarrow v(0,t)=0$

$0=u(\pi,t)=u_s(\pi)+v(\pi,t)=v(\pi,t)\Leftrightarrow v(\pi,t)=0$ .

Altså oppfyller $v(x,t)$ det homogene randverdiproblemet i **b)**. Det vil si at $v(x,t)$ er gitt som

$$v(x,t)=\sum_{n=1}^{\infty}A_ne^{-n^2t}\sin nx\ ,$$

for konstanter $A_n$, $n=1,2,3,\ldots$ .

Dermed er

$$u(x,t)=u_s(x)+v(x,t)=\pi x-x^2+\sum_{n=1}^{\infty}A_ne^{-n^2t}\sin nx$$

(formell) løsning på randverdiproblemet i **c)**.

Startverdien $u(x,0)=0$ gir

$$0=u(x,0)=u_s(x)+v(x,0)\Leftrightarrow v(x,0)=-u_s(x)\,.$$

Vi har da

$$v(x,0)=\sum_{n=1}^{\infty}A_n\sin nx=-\left(\pi x-x^2\right)\,.$$

Fra **a)** finner vi da

$$A_n=\left\{\begin{array}{ll}\displaystyle\frac{-8}{\pi n^3},&\text{for }n\text{ odde}\\[8pt] 0,&\text{for }n\text{ like}\end{array}\right.\,.$$

Altså er løsninga

$$u(x,t)=u_s(x)+v(x,t)=\pi x-x^2-\frac{8}{\pi}\sum_{m=0}^{\infty}\frac{e^{-\left(2m+1\right)^2t}\sin\left(2m+1\right)x}{\left(2m+1\right)^3}\,.$$

Kildesett: course=TMA4125 term=var year=2016 problem=5 file=tma4123_4125.pdf
