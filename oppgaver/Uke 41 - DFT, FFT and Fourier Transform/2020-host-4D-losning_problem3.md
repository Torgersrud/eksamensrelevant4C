### **Solution to Problem 3**

Take the Fourier transform. The Fourier convolution theorem gives

$$\sqrt{2\pi}\hat{f}(w)\cdot\frac{1}{\sqrt{2}}e^{-w^2/4}=\sqrt{2\pi}\,\widehat{xe^{-x^2/2}}.$$

Now we use that

$$xe^{-x^2/2}=-(e^{-x^2/2})',$$

which implies that

$$\widehat{xe^{-x^2/2}}=-iw\widehat{e^{-x^2/2}}=-iwe^{-w^2/2}.$$

Now the first identity reduces to

$$\sqrt{2\pi}\hat{f}(w)\cdot\frac{1}{\sqrt{2}}e^{-w^2/4}=\sqrt{2\pi}(-iwe^{-w^2/2}),$$

which gives

$$\hat{f}(w)=-iw\sqrt{2}e^{-w^2/4}=-2iw\widehat{e^{-t^2}}=(-2)\widehat{(e^{-t^2})'},$$

(the final identity uses again that $\widehat{g'}=iw\hat{g}$) from which we know that the Fourier transform of $f$ is equal to the Fourier transform of $(-2)(e^{-t^2})'$. Now we know that $f$ must be equal to $(-2)(e^{-t^2})'$ (you can use, for example, the Fourier inversion formula to prove this), hence we get

$$f(t)=(-2)(e^{-t^2})'=4te^{-t^2}.$$

Kildesett: course=TMA4135 term=host year=2020 problem=3 points=10 file=completeexam_nosolutions.pdf
