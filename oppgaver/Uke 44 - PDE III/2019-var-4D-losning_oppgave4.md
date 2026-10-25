### **Løsning til Oppgave 4**

Apply a change of variable $2c^2t=s$, it is enough to prove the case that $2c^2=1$. Consider Fourier transform of $u_t$ with respect to the $x$ variable

$$\mathcal{F}(u_t)=\widehat{u_t}(w)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}u_t(t,x)e^{-ixw}\,dx.$$

Then we have

$$\mathcal{F}(u_t)=\mathcal{F}\left(\frac{1}{2}u_{xx}\right)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{1}{2}u_{xx}(t,x)e^{-ixw}\,dx.$$

Recall that if $u$ is smooth and rapidly decreasing with respect to $x$ then

$$\int_{-\infty}^{\infty}u_{xx}e^{-ixw}\,dx=\int_{-\infty}^{\infty}e^{-ixw}\,d(u_x)=-\int_{-\infty}^{\infty}u_x\,d(e^{-ixw})=iw\int_{-\infty}^{\infty}u_xe^{-ixw}\,dx,$$

the same computation for $u$ gives

$$\int_{-\infty}^{\infty}u_xe^{-ixw}\,dx=iw\int_{-\infty}^{\infty}ue^{-ixw}\,dx,$$

thus we have

$$\mathcal{F}(u_t)=\frac{-w^2}{2}\mathcal{F}(u),\quad \mathcal{F}(u):=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}u(t,x)e^{-ixw}\,dx$$

Notice that we also have

$$\mathcal{F}(u_t)=(\mathcal{F}(u))_t.$$

Thus $\mathcal{F}(u)$ satisfies the following ODE.

$$(\mathcal{F}(u))_t=\frac{-w^2}{2}\mathcal{F}(u).$$

The general solution is

$$\mathcal{F}(u)(t,w)=c(w)e^{\frac{-w^2}{2}t}.$$

Notice that our initial condition implies

$$\mathcal{F}(u)(0,w)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-ixw}\,dx=\mathcal{F}(f).$$

Thus

$$c(w)=\mathcal{F}(f).$$

Now we have

$$\mathcal{F}(u)(t,w)=\mathcal{F}(f)\cdot e^{\frac{-w^2}{2}t}.$$

Recall that

$$e^{\frac{-u^2}{2}}=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{\frac{-y^2}{2}}e^{-iyu}\,dy.$$

Take

$$u=w\sqrt{t},\ y=\frac{x}{\sqrt{t}},$$

we get

$$e^{\frac{-w^2}{2}t}=\frac{1}{\sqrt{2\pi t}}\int_{-\infty}^{\infty}e^{\frac{-x^2}{2t}}e^{-ixw}\,dx=\frac{1}{\sqrt{t}}\mathcal{F}(e^{\frac{-x^2}{2t}}).$$

Thus

$$\mathcal{F}(u)(t,w)=\mathcal{F}(f)\cdot\left(\frac{1}{\sqrt{t}}\mathcal{F}(e^{\frac{-x^2}{2t}})\right)$$

and the Fourier convolution formula gives

$$u(t,x)=\frac{1}{\sqrt{2\pi t}}(f\star e^{\frac{-x^2}{2t}})=\int_{-\infty}^{\infty}f(p)\frac{1}{\sqrt{2\pi t}}e^{\frac{-(x-p)^2}{2t}}\,dp,$$

i.e. the solution $u(t,x)$ is given by convolution of the initial temperature distribution with the heat kernel.

Kildesett: course=TMA4135 term=var year=2019 problem=4 file=tma4125-30-35-k19-bm.pdf
