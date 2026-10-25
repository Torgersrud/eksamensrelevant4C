### **Løsning til Oppgave 2**

**a)** Even $2\pi$-periodic prolongation:

[Figur: Handtegna aksesar med vannrett akse merkt $-3\pi$, $-2\pi$, $-\pi$, $0$, $\frac{\pi}{2}$, $\pi$, $\frac{3\pi}{2}$, $2\pi$ og $3\pi$ og loddrett akse med merke for $1$. Den jevne $2\pi$-periodiske utvidinga er teikna tjukt som eit stegmønster på nivå $1$ over $(\frac{\pi}{2},\frac{3\pi}{2})$ og $(-\frac{3\pi}{2},-\frac{\pi}{2)}$ og på nivå $0$ rundt $0$, med korte stipla strekar på nivå $1$ heilt ute mot $\pm3\pi$ som viser den periodiske framhaldet.]

Fourier series:

* Since $f$ is even all sin-coeff. vanish:

$$f(x)\sim a_0+\sum_1^{\infty}a_n\cos nx$$

$$a_0=\frac{1}{\pi}\int_0^{\pi}f(x)\,dx=\frac{1}{2}$$

$$n>0\Rightarrow a_n=\frac{2}{\pi}\int_0^{\pi}f(x)\cos nx\,dx=\frac{2}{\pi}\int\limits_{\pi/2}^{\pi}\cos nx\,dx=\frac{2}{\pi}\left(\frac{\sin nx}{n}\right)\Big|_{x=\pi/2}^{\pi}=-\frac{2}{n\pi}\sin\frac{n\pi}{2}=\begin{cases}0 & n\text{-even}\\[4pt] \dfrac{2}{n\pi}(-1)^{k+1} & \text{if}\ n=2k+1\end{cases}$$

$$\Rightarrow f(x)\sim\frac{1}{2}-\frac{2}{\pi}\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1}\cos(2k+1)x$$

**b)** Find all functions of the form $u(x,t)=X(x)T(t)$ which satisfy the equation $\frac{\partial^2u}{\partial x^2}=\frac{\partial u}{\partial t}-u$, $t>0$, $0<x<\pi$ and also $u_x(0,t)=0$; $u_x(\pi,t)=0$

$$X''(x)\,T(t)=X(x)\,\dot T(t)-X(t)\,T(t)\Rightarrow$$

$$\frac{X''(x)}{X(x)}=\frac{\dot T(t)}{T(t)}-1=k\ \text{-- constant.}$$

$$\Rightarrow X''(x)-kX(x)=0,\quad 0<x<\pi$$

$$\dot T(t)-(k+1)\,T(t)=0,\quad t>0$$

boundary conditions $\Rightarrow$

$$X''(x)-kX(x)=0,\qquad X'(0)=0,\ X'(\pi)=0$$

standard analysis:

$$k=-\rho^2,\quad\rho=0,1,2,\cdots$$

$$\rho=0\Rightarrow X_0(x)=a_0;\quad\rho>0\Rightarrow X_{\rho}(x)=a_{\rho}\cos\rho x$$

(Continuation)

$$\rho=0\ \Rightarrow\ \dot T_0(t)-T(t)=0\ \Rightarrow\ T(t)=e^{t}\cdot\mathrm{const}$$

$$\rho=1\ \Rightarrow\ \dot T_1(t)=0\ \Rightarrow\ T_1(t)=\mathrm{const}$$

$$\rho\geq1\ \Rightarrow\ \dot T_{\rho}(t)+(\rho^2-1)\,T_{\rho}(t)=0\ \Rightarrow\ T_{\rho}(t)=e^{-(\rho^2-1)t}\cdot\mathrm{const}$$

> This formula can be used for all p's. I wrote the cases p = 0 and p = 1 separately, because in these cases the solution does not decay as $t\to+\infty$.

Finally:

$$u_0(x,t)=a_0e^{t}$$

$$u_1(x,t)=a_1\cos x$$

$$u_{\rho}(x,t)=a_{\rho}\,e^{-(\rho^2-1)t}\cos\rho x$$

**c)** Find the function $u(x,t)$ which meets the above equation and also $u(x,0)=f(x)$, $0<x<\pi$

$$u(x,t)=\frac{1}{2}\,e^{t}-\frac{2}{\pi}\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1}\,e^{-k(k+2)t}\cos(2k+1)x$$

* Find the function $u(x,t)$ which meets the above equation and also $u(x,0)=\cos x\ \cos^2x$, $0<x<\pi$.

I do not remember if there is a formula for $\cos^3x$ in Rotman, but

$$\cos^2x=\frac{1}{2}\left(1+\cos 2x\right)\ \Rightarrow$$

$$\cos x\ \cos^2x=\frac{1}{2}\cos x+\frac{1}{2}\cos x\cos 2x=\frac{1}{2}\cos x+\frac{1}{2}\left[\frac{1}{2}(\cos(2x-x)+\cos(2x+x))\right]=\frac{1}{4}\cos 3x+\frac{3}{4}\cos x$$

$$\Rightarrow u(x,t)=\frac{3}{4}\cos x+\frac{1}{4}\cos 3x\cdot e^{-8t}$$

Comment: You may wanted to calculate the Fourier coefficients by the standard formulas, it will lead you to the same result but takes more time.

*Kjeldevarsel: LF er handskriven på engelsk og er transkribert ordrett; overstreka utkast er utelne (eit $\rho$-tilfelle-boks på s. 4, ei $\frac{3}{4\pi}$-brøk i 2c-svar på s. 6), og ordet «the» er innføgt med pott over «function» i 2c-punkta på s. 6. Attmerkingar: (i) første likskap i b) er skriven $X''(x)T(t)=X(x)\dot T(t)-\dot X(t)T(t)$ — det siste leddet må lesast $X(x)T(t)$. (ii) $a_0=\frac{1}{\pi}\int_0^{\pi}f\,dx=\frac{1}{2}$ er rekna ut som middelverdien; med konvensjonen $f\sim a_0+\sum a_n\cos nx$ elles i LF skulle formelen vore $\frac{2}{\pi}\int_0^{\pi}$ — talet $\frac{1}{2}$ og sluttrekka er likevel rette. (iii) I første formel i c) står ledd-exponenten $e^{-k(k+2)t}$, men $T$-formelen i b) med $\rho=2k+1$ gjev $e^{-(\rho^2-1)t}=e^{-4k(k+1)t}$; LF si eiga løysing for $\cos 3x$-leddet (annet punkt i c) bruker $e^{-8t}$, som stadfestar $4k(k+1)$ — for $k=1$ gir den skrivne formelen $e^{-3t}$. (iv) «Rotman» er LF si skrivemåte for formelsamlinga Rottmann, og «You may wanted to calculate» er LF si eiga setningsforming. Alt er kontrollreikna med sympy: $a_0=\frac{1}{2}$, $a_n=-\frac{2}{n\pi}\sin\frac{n\pi}{2}$, rekkja konvergerer mot $f$ (serieverdi $0$ i $x=0$), leddfunksjonane $e^{-(\rho^2-1)t}\cos\rho x$ løyser $u_{xx}=u_t-u$ og $u_x(0,t)=u_x(\pi,t)=0$, og $u=\frac{3}{4}\cos x+\frac{1}{4}e^{-8t}\cos 3x$ løyser både likninga, randvilkåra og startkravet $\cos x\cos^2x$.*

Kildesett: course=TMA4125 term=var year=2006 problem=2 file=eksamen-bok_2006v.pdf
