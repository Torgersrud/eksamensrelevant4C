### **Løsning til Oppgave 2**

Setter vi $u = FG$ inn i ligning (1) får vi $t^3 G'F = F''G$ og siden vi ikke er interessert i den trivielle løsningen får vi $\frac{t^3 G'F}{FG} = \frac{F''G}{FG}$ som gir oss at $\frac{t^3 G'}{G} = \frac{F''}{F} = \text{konstant}$.

For å få oppfylt randkravene (2) må vi ha at konstanten kun kan ta verdiene $-n^2$ for $n = 1, 2, \ldots$, og dermed får vi ligningene

$$\frac{F''}{F} = -n^2 \quad \text{for } n = 1, 2, \ldots$$

For verdien $-n^2$ blir løsningen $F_n(x) = \sin nx$ opp til multiplikasjon med en vilkårlig konstant som vi tar inn i løsningen av den andre ligningen, nemlig

$$\frac{t^3 G'}{G} = -n^2 \quad \text{som kan skrives på formen} \quad \frac{dG}{G} = -n^2 \frac{dt}{t^3}.$$

Integrasjon gir oss løsningene

$$G_n(t) = B_n\, e^{\frac{n^2}{2t^2}} \quad \text{for en vilkårlig konstant } B_n.$$

Superposisjonsprinsippet forteller oss at den generelle løsningen av (1) som tilfredstiller randkravene (2), kan skrives som Fourierrekke

$$u(x,t) = \sum_{n=1}^{\infty} B_n\, e^{\frac{n^2}{2t^2}} \sin nx.$$

Setter vi så inn initialkravet $u(x,1) = 4\sin x + \sin 4x$ gir dette at alle $B_n$-ene forsvinner bortsett fra at $B_1 e^{\frac{1}{2}} = 4$ og $B_4\, e^8 = 1$. Løsningen blir

$$u(x,t) = 4e^{\frac{1}{2}\left(\frac{1}{t^2} - 1\right)} \sin x + e^{8\left(\frac{1}{t^2} - 1\right)} \sin 4x.$$

Kildesett: course=TMA4135 term=kont year=2006 problem=2 file=tma4135_06k.pdf
