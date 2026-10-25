### **Løsning til Oppgave 8**

La oss først vise at $\langle \sin x,\sin 2x\rangle=0$. Husk at $\sin 2x=2\sin x\cos x$ så

$$\langle \sin x,\sin 2x\rangle=\int_0^{\pi}2\sin^2 x\cos x\,dx=\int_0^{\pi}\frac{2}{3}\frac{d}{dx}\sin^3 x\,dx=\left.\frac{2}{3}\sin^3 x\right|_0^{\pi}=0,$$

så $f_1(x)=\sin x$ og $f_2(x)=\sin 2x$ er ortogonale.

Den ortogonale projeksjonen av $f(x)=x$ på $W$ er gitt som

$$(Pf)(x)=\frac{\langle f(x),f_1(x)\rangle}{\langle f_1(x),f_1(x)\rangle}f_1(x)+\frac{\langle f(x),f_2(x)\rangle}{\langle f_2(x),f_2(x)\rangle}f_2(x).$$

Det gjenstår å beregne indreproduktene. Merk at $\sin^2 kx$ og $\cos^2 kx$ må ha samme integral mellom $0$ og $\pi$ siden begge er $\pi$-periodiske og kun faseforskjøvet i forhold til hverandre. Derfor er

$$\int_0^{\pi}\sin^2 kx\,dx=\int_0^{\pi}\frac{1}{2}(\sin^2 kx+\cos^2 kx)=\frac{1}{2}\int_0^{\pi}dx=\frac{\pi}{2}$$

for alle heltallige $k$, og tilsvarende ved delvis integrasjon er

$$\langle f,f_k\rangle=\int_0^{\pi}x\sin kx\,dx=\left.-x\frac{\cos kx}{k}\right|_0^{\pi}+\frac{1}{k}\int_0^{\pi}\cos kx\,dx=(-1)^{k+1}\frac{\pi}{k}.$$

Setter vi dette inn i uttrykket for $(Pf)(x)$ finner vi

$$(Pf)(x)=\frac{\pi}{\pi/2}\sin x+\frac{(-\pi/2)}{\pi/2}\sin 2x=2\sin x-\sin 2x.$$

*Kjeldevarsel: ortogonaliteten $\langle \sin x,\sin 2x\rangle=0$, lengdene $\|\sin kx\|^2=\frac{\pi}{2}$, koeffisientane $2$ og $-1$ og projeksjonen $2\sin x-\sin 2x$ er kontrollrekna med sympy.*

Kildesett: course=TMA4110 term=kont year=2022 problem=8 file=EksamenTMA4110-15Kont.pdf
