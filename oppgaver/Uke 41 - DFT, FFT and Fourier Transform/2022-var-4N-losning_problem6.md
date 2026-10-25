### **Solution to Problem 6** (Fourier Transform, 8 points)

We can use Eulers identity on the cosine to obtain (2 P.)

$$\begin{aligned}\hat{f}(\omega)&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)\mathrm{e}^{-\mathrm{i}\omega x}\,\mathrm{d}x\\
&=\frac{1}{\sqrt{2\pi}}\int_{-L}^{L}\cos(\lambda x)\mathrm{e}^{-\mathrm{i}\omega x}\,\mathrm{d}x\\
&=\frac{1}{\sqrt{2\pi}}\int_{-L}^{L}\frac{1}{2}\Big(\mathrm{e}^{\mathrm{i}\lambda x}+\mathrm{e}^{-\mathrm{i}\lambda x}\Big)\mathrm{e}^{-\mathrm{i}\omega x}\,\mathrm{d}x\\
&=\frac{1}{2\sqrt{2\pi}}\int_{-L}^{L}\mathrm{e}^{\mathrm{i}x(\lambda-\omega)}+\mathrm{e}^{-\mathrm{i}x(\lambda+\omega)}\,\mathrm{d}x\end{aligned}$$

For $\lambda\neq\pm\omega$ we can compute the antiderivative of both terms (3 P.)

$$\begin{aligned}\hat{f}(\omega)&=\frac{1}{2\sqrt{2\pi}}\left(\frac{1}{\mathrm{i}(\lambda-\omega)}\mathrm{e}^{\mathrm{i}x(\lambda-\omega)}-\frac{1}{\mathrm{i}(\lambda+\omega)}\mathrm{e}^{-\mathrm{i}x(\lambda+\omega)}\right)\Big|_{-L}^{L}\\
&=\frac{1}{\sqrt{2\pi}}\left(\frac{1}{2\mathrm{i}(\lambda-\omega)}\left(\mathrm{e}^{\mathrm{i}L(\lambda-\omega)}-\mathrm{e}^{-\mathrm{i}L(\lambda-\omega)}\right)+\frac{1}{2\mathrm{i}(\lambda+\omega)}\left(\mathrm{e}^{\mathrm{i}L(\lambda+\omega)}-\mathrm{e}^{-\mathrm{i}L(\lambda+\omega)}\right)\right)\end{aligned}$$

where in the last line the second summand has a + upfront since we switched the order of the terms in the inner difference (note that for $x=-L$ the minus sign vanishes but this is the first term). Now both summands, especially already with the $2\mathrm{i}$ in the denominator look like sine functions, so we can rewrite this to (2 P.)

$$\hat{f}(\omega)=\frac{1}{\sqrt{2\pi}}\left(\frac{\sin(L(\lambda-\omega))}{\lambda-\omega}+\frac{\sin(L(\lambda+\omega))}{\lambda+\omega}\right)$$

Extending both fractions by $L$ and using the definition of $\mathrm{sinc}(x)=\frac{\sin x}{x}$ we can simplify this to

$$\hat{f}(\omega)=\frac{1}{\sqrt{2\pi}}\Big(L\,\mathrm{sinc}(L(\lambda-\omega))+\mathrm{sinc}(L(\lambda+\omega))\Big)$$

Since $\mathrm{sinc}(0)=1$ we also obtain the same solution for $\lambda=\pm\omega$ where either the first or the second integral integrates to $2L$. (1 P.)

Kildesett: course=TMA4125 term=var year=2022 problem=6 points=8 file=TMA4125-Matematikk-4N-2022v_lf.pdf
