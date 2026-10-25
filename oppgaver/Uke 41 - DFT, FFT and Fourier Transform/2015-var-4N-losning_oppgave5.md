### **Løsning til Oppgave 5**

La $g_a(x)=e^{-a|x|}$. Integralet i oppgaven er en konvolusjon, så ligningen kan skrives

$$f(x)=g_2(x)-3(f*g_2)(x).$$

Teoremet for Fourier-transformasjon av konvolusjoner gir

$$\hat f(\omega)=\hat{g_2}(\omega)-3\sqrt{2\pi}\hat f(\omega)\hat{g_2}(\omega).$$

Formelarket gir

$$\hat{g_2}(\omega)=\mathcal F(g_2)(\omega)=\sqrt{\frac{2}{\pi}}\frac{2}{\omega^2+2^2},$$

så vi har

$$\hat f(\omega)=\sqrt{\frac{2}{\pi}}\frac{2}{\omega^2+4}\left(1-3\sqrt{2\pi}\hat f(\omega)\right),$$

slik at

$$\hat f(\omega)=\frac{1}{2}\sqrt{\frac{2}{\pi}}\frac{4}{\omega^2+4^2}=\frac{1}{2}\hat{g_4}(\omega).$$

Formelarket gir så

$$f(x)=\frac{1}{2}g_4(x)=\frac{1}{2}e^{-4|x|}.$$

Kildesett: course=TMA4123 term=var year=2015 problem=5 file=eksamen-nb.pdf
