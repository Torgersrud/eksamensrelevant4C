### **Løsning til Oppgave 4**

a) Vi må vise at $f^{\text{even}}(-x) = f^{\text{even}}(x)$ og at $f^{\text{odd}}(-x) = -f^{\text{odd}}(x)$. Dette sees umiddelbart ved innsetting. Vi har at $e^{ix} = \cos x + i \sin x$. Vi vet at $\cos x$ er en likefunksjon og $\sin x$ er en oddefunksjon. Funksjonen $e^{-|x|}$ er en likefunksjon. Siden produktet av to likefunksjoner er en likefunksjon og produktet av en likefunksjon og en oddefunksjon er en oddefunksjon har vi

$$e^{-|x|} e^{-ix} = e^{-|x|} \cos x - i e^{-|x|} \sin x.$$

Alternativt kan vi konstruere

$$
\begin{aligned}
f^{\text{even}}(x) &= \frac{1}{2} \bigg( e^{-|x|} e^{-ix} + e^{-|-x|} e^{-i(-x)} \bigg) = e^{-|x|} \cos x, \\
f^{\text{odd}}(x) &= \frac{1}{2} \bigg( e^{-|x|} e^{-ix} - e^{-|-x|} e^{-i(-x)} \bigg) = -i e^{-|x|} \sin x.
\end{aligned}
$$

Siden $f(x) = f^{\text{even}}(x) + f^{\text{odd}}(x)$ får vi samme resultat som ovenfor.

b) Anta at $f$ er odde. Da er $f(x)e^{-ixw} = -if(x)\sin xw + f(x)\cos xw$. Her er $f(x)\cos xw$ en oddefunksjon, så $\int_{-\infty}^{\infty} f(x) \cos xw \, dx = 0$. Følgelig er

$$\mathcal{F}(f(x)) = -i \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(x) \sin xw \, dx,$$

og dette er en oddefunksjon siden $\sin xw$ er en oddefunksjon av $w$ for alle $x$. Tilsvarende for en likefunksjon.

c)

$$
\begin{aligned}
\mathcal{F}(f(x)e^{-iax})(w) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(x) e^{-iax} e^{-ixw} dx = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(x) e^{-ix(w+a)} dx
\end{aligned}
$$

$$= \mathcal{F}(f(x))(w + a).$$

d) Inversjon gir

$$
\begin{aligned}
e^{-|x|} \cos x = \sqrt{\frac{2}{\pi}} \mathcal{F}^{-1}\left( \frac{w^2 + 2}{w^4 + 4} \right)(x) = \sqrt{\frac{2}{\pi}} \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \left( \frac{w^2 + 2}{w^4 + 4} \right) e^{ixw} dw \\
= \frac{1}{\pi} \int_{-\infty}^{\infty} \frac{w^2 + 2}{w^4 + 4} \cos xw \, dw = \frac{2}{\pi} \int_0^{\infty} \frac{w^2 + 2}{w^4 + 4} \cos xw \, dw.
\end{aligned}
$$

Setter vi $x = 0$ får vi

$$\int_0^{\infty} \frac{w^2 + 2}{w^4 + 4} dw = \frac{\pi}{2}.$$

Kildesett: course=TMA4135 term=host year=2009 problem=4 file=tma4135_09h.pdf
