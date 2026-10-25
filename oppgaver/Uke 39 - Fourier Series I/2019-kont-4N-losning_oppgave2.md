### **Løsning til Oppgave 2**

Since Fourier series of a $2\pi$ periodic function is an orthogonal decomposition wrt the orthogonal basis $\{1,\cos nt,\sin nt\}_{n\geq 1}$, we know that

$$f(x)=\sin(3x)+\sin(x)+1$$

already gives the Fourier series of $f$.

Recall that $\mathcal{F}(f'(x))(w)=iw\mathcal{F}(f(x))(w)$ and observe that

$$f(x)=6x\exp(-5x^2)=-\frac{6}{10}\frac{d}{dx}\exp(-5x^2).$$

Then

$$\begin{aligned}
\mathcal{F}\bigl(6x\exp(-5x^2)\bigr) &= \mathcal{F}\Bigl(-\frac{6}{10}\frac{d}{dx}\exp(-5x^2)\Bigr) \\
&= -\frac{6}{10}iw\mathcal{F}\Bigl(\exp(-5x^2)\Bigr) \\
&= \frac{6iw}{10\sqrt{10}}\exp\Bigl(-w^2/20\Bigr).
\end{aligned}$$

*Kjeldevarsel (losningsfila): siste lija er teken ordrett — mellomsteget over er negativt medan det utgitte svaret er positivt. Dette er en av to feil merkta på old_exams-sida.*

Kildesett: course=TMA4135 term=kont year=2019 problem=2 file=tma4125-30-35-k19-bm.pdf
