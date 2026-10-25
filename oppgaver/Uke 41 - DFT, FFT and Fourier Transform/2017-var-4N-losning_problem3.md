### **Solution to Problem 3**

**a)** The idea is to use the identity $\mathcal{F}(f'(x))=iw\hat{f}(w)$. For this purpose, we define

$$f(x)=C+\int_{-\infty}^{x}g(x)dx,$$

where $C$ is an appropriately chosen constant. Then $f'(x)=g(x)$, and hence $\hat{f}(w)=\frac{\hat{g}(w)}{iw}$, from which we find

$$f(x)=\mathcal{F}^{-1}\left(\frac{\hat{g}(w)}{iw}\right)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{\hat{g}(w)}{iw}e^{iwx}dw$$

In particular we have

$$\int_{a}^{b}g(x)dx=f(b)-f(a)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{\hat{g}(w)(e^{iwb}-e^{iwa})}{iw}dw$$

**b)** Taking Fourier transforms with respect to $x$ gives

$$\hat{u}_{tt}(w,t)=-c^2w^2\hat{u}(w,t),\quad \hat{u}(w,0)=0,\ \hat{u}_t(x,0)=\hat{g}(w),$$

where we have also taken Fourier transforms of the initial conditions. As there are no derivatives with respect to $w$ in the equation, we can solve like an ODE, obtaining

$$\hat{u}=A(w)\cos cwt+B(w)\sin cwt$$

Now $\hat{u}(w,0)=0\Rightarrow A=0$. We then differentiate:

$$\hat{u}_t=cwB\cos cwt$$

and hence $\hat{u}_t(w,0)=cwB$. Setting $cwB(w)=\hat{g}(w)$ to satisfy the other initial condition then gives

$$\hat{u}=\frac{\hat{g}(w)}{cw}\sin cwt$$

**c)** We use the inverse Fourier transform to find

$$u(x,t)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{\hat{g}(w)}{cw}\sin(cwt)e^{iwx}dw$$

Using the identity $\sin cwt=\frac{e^{icwt}-e^{-icwt}}{2i}$, we find

$$u(x,t)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{\hat{g}(w)(e^{iw(x+ct)}-e^{iw(x-ct)})}{2icw}dw$$

Applying the identity from part a) then gives

$$u(x,t)=\frac{1}{2c}\int_{x-ct}^{x+ct}g(x')dx'$$

Kildesett: course=TMA4125 term=var year=2017 problem=3 file=exam.pdf
