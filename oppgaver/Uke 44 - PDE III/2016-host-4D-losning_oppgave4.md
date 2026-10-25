### **Løsning til Oppgave 4**

**a)** [Figur: $x$-akse fra $-1$ til $1$ og $y$-akse. Grafen til $y=g(x)$ er en sagtagget, odde kurve: $g$ stiger lineært fra $0$ i $x=0$ til $f(\frac12)=\frac12$, synker lineært til $0$ i $x=1$, og er odde fortstilt med $g(-x)=-g(x)$, med stiplet fortsetting utenfor $[-1,1]$.]

$$\begin{aligned}b_n&=2\int_0^1\sin n\pi x\cdot f(x)\,dx=2\int_0^{1/2}\sin n\pi x\cdot x\,dx+2\int_{1/2}^1\sin n\pi x\cdot(1-x)\,dx\\
&=\frac{4}{(n\pi)^2}\sin\frac{n\pi}{2}-\frac{2}{n\pi}\cos\frac{n\pi}{2}+\frac{2}{n\pi}\cos n\pi-\frac{2}{n\pi}\cos n\pi+\frac{2}{n\pi}\cos\frac{n\pi}{2}\quad\text{(ledd som kansellerer)}\\
&=\frac{4}{(n\pi)^2}\sin\frac{n\pi}{2}.\end{aligned}$$

Dermed er

$$b_{2m+1}=\frac{4}{(2m+1)^2\pi^2}\cdot(-1)^m,\quad m=0,1,2,\ldots,$$

og Fourier-sinusrekken til $f$ er

$$\sum_{m=0}^{\infty}(-1)^m\cdot\frac{4\sin(2m+1)\pi x}{(2m+1)^2\cdot\pi^2}.$$

**b)** $f(\frac12)=\frac12=4\cdot\left(\dfrac{1}{\pi^2}+\dfrac{1}{3^2\pi^2}+\cdots\right)\Rightarrow\pi^2=8\cdot\left(1+\dfrac{1}{3^2}+\dfrac{1}{5^2}+\cdots\right)$

**c)** $F\dot G=F''G$; $\dfrac{F''}{F}=\dfrac{\dot G}{G}=-(n\pi)^2$ etter drøfting som leder til $F=\sin n\pi x$ fordi $F(0)=F(1)=0$. Deretter finnes $G=\exp(-(n\pi)^2t)$ og løsning

$$u=\sum_{n=1}^{\infty}b_n\sin n\pi x\cdot e^{-(n\pi)^2t}.$$

Startbetingelsen gir $b_n$ fra a), så

$$u(x,t)=\sum_{m=0}^{\infty}\frac{4}{\pi^2}\cdot(-1)^m\cdot\frac{\sin(2m+1)x}{(2m+1)^2}\cdot e^{-(2m+1)^2\pi^2t}.$$

**d)** $\dot v=\dot u$; $v_{xx}=u_{xx}$, så $v_t=v_{xx}$. $v(0,t)=u(0,t)+1=1$, $v(1,t)=u(1,t)+0=0$ og $v(x,0)=u(x,0)+1-x=f(x)+1-x$.

Beskriv hvordan et skritt kan beregnes. La $y(t)=[v(x_n,t)]$ med en diskretisering $x=n\cdot\Delta x+x_0$, $n=0,\ldots,N+1$ hvor $x_0=0$ og $x_{N+1}=1$. Videre benyttes

$$v_{xx}(x_n,t)\simeq\frac{1}{\Delta x^2}\left[y_{n-1}-2y_n+y_{n+1}\right].$$

Da finnes ($y_0=1$, $y_{N+1}=0$):

$$\begin{aligned}\dot y(x_n,t)&=v''(x_n,t)\\
\dot{\mathbf y}&\simeq\frac{1}{\Delta x^2}\left[\begin{bmatrix}-2&1&&\\1&-2&1&\\&\ddots&\ddots&\ddots&\\&&1&-2&1\\&&&1&-2\end{bmatrix}\begin{bmatrix}y_1\\y_n\\\vdots\\y_N\end{bmatrix}+\begin{bmatrix}1\\0\\\vdots\\0\end{bmatrix}\right]\\
&=\frac{1}{\Delta x^2}\left[\Delta_x\,\mathbf y+R\right]=f(t,\mathbf y(t))=f(\mathbf y(t)).\end{aligned}$$

Trapez = CN: ($\Gamma=\frac{\Delta t}{\Delta x^2}$)

$$\begin{aligned}\mathbf y(\Delta t)&=\mathbf y(0)+\frac{\Delta t}{2}\left[f(\mathbf y(0))+f(\mathbf y(\Delta t))\right]\\
&=\mathbf y(0)+\frac{\Gamma}{2}\cdot2R+\frac{\Gamma}{2}\left[\Delta_x\,\mathbf y(0)+\Delta_x\,\mathbf y(\Delta t)\right]\end{aligned}$$

$$\left[I-\tfrac{\Gamma}{2}\Delta_x\right]\mathbf y(\Delta t)=\Gamma\cdot R+\left[I+\tfrac{\Gamma}{2}\Delta_x\right]\mathbf y(0)\quad(\star)$$

$(\star)$ gir et tridiagonalt system som kan løses for å finne $\mathbf y(\Delta t)$. Det kan noteres at randbetingelsene gir et bidrag $R\neq0$.

Systemet kan også løses alternativt via $\mathbf y=\mathbf y_p+\mathbf y_u$ hvor $0=A\mathbf y_p+R$, $\dot{\mathbf y}_u=A\mathbf y_u$, $\mathbf y_u(0)=\mathbf y(0)-\mathbf y_p$. Numerisk er det ikke opplagt om dette er gunstig; jf. systemet.

**e)** Bruker diskretiseringen som over, men løser i stedet baktsettende Euler:

$$\mathbf y(\Delta t)=\mathbf y(0)+\Gamma\cdot\Delta_x\,\mathbf y(\Delta t)$$

Her er $\Gamma=\Delta t/\Delta x^2=\frac{1}{16}\cdot4^2=1$ og

$$I-\Delta_x=\begin{bmatrix}1+2&-1&0\\-1&3&-1\\0&-1&3\end{bmatrix},\qquad f(\tfrac14)=\tfrac14,\quad f(\tfrac12)=\tfrac12,\quad f(\tfrac34)=\tfrac14.$$

Utskrevet:

$$\begin{aligned}3y_1-y_2&=1/4\\-y_1+3y_2-y_3&=1/2\\-y_2+3y_3&=1/4\end{aligned}$$

Ved symmetri fås $y_1=y_3$:

$$3y_1-y_2=1/4\ ;\ -2y_1+3y_2=1/2$$

$$6y_1-2y_2=1/2$$

$$-6y_1+9y_2=3/2$$

$$7y_2=2\ ;\quad Y=y_2=\underline{\underline{2/7}}$$

$$y_1=\frac{3}{2}\cdot\frac{2}{7}-\frac{1}{4}=\frac{12-7}{28}=\underline{\underline{\frac{5}{28}}}$$

Altså er $X(1/16)\approx5/28$ og $Y(1/16)\approx2/7$.

Kildesett: course=TMA4135 term=host year=2016 problem=4 file=tma4135_16h.pdf
