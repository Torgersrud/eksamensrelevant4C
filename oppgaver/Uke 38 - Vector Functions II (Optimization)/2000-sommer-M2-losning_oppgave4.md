### **Løsning til Oppgave 4**

Parameterfremstilling av skjæringskurven:

$$x = \cos t, \quad y = \sin t, \quad z = \ln(1 - \cos t \sin t) - \frac{1}{2}(\cos^2 t + \sin^2 t) = \ln(1 - \frac{1}{2} \sin 2t) - \frac{1}{2}$$

for $0 \le t \le 2\pi$. Vi finner kandidater til max og min ved å sette $dz/dt = 0$.

$$\frac{dz}{dt} = \frac{1}{1 - \frac{1}{2} \sin 2t} \cdot (-\cos 2t) = 0 \quad \text{for} \;\; t = \frac{\pi}{4} + k \frac{\pi}{2}$$

der $k$ er et vilkårlig heltall. Det gir

$$t = \frac{\pi}{4}: \qquad z = \ln(1 - \frac{1}{2} \sin \frac{\pi}{2}) - \frac{1}{2} = \ln \frac{1}{2} - \frac{1}{2}. \quad \text{Min}$$
$$t = \frac{3\pi}{4}: \qquad z = \ln(1 - \frac{1}{2} \sin \frac{3\pi}{2}) - \frac{1}{2} = \ln \frac{3}{2} - \frac{1}{2}. \quad \text{Max}$$
$$t = \frac{5\pi}{4}: \qquad z = z(\frac{\pi}{4}). \qquad \text{Min}$$
$$t = \frac{7\pi}{4}: \qquad z = z(\frac{3\pi}{4}). \qquad \text{Max}$$

De høyeste punktene på skjæringskurveen er derfor $(-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, \ln \frac{3}{2} - \frac{1}{2})$ og $(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}, \ln \frac{3}{2} - \frac{1}{2})$. De laveste punktene er $(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, \ln \frac{1}{2} - \frac{1}{2})$ og $(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}, \ln \frac{1}{2} - \frac{1}{2})$.

<u>Alternativt:</u> På skjæringskurven er

$$z = \ln(1 - xy) - \frac{1}{2}$$

Maksimum inntrer når $xy$ er minst mulig på enhetssirkelen. Det vil si, når $xy = -\frac{1}{2}$. Minimum inntrer når $xy$ er størst mulig på enhetssirkelen. Det vil si, når $xy = \frac{1}{2}$. Derav følger svaret.

<u>Alternativt</u> kan vi bruke Lagranges metode: Vi skal finne max og min for funksjonen $f(x, y, z) = z$ under bibetingelsene

$$g(x, y, z) = x^2 + y^2 - 1 = 0 \quad \text{og} \quad h(x, y, z) = \ln(1 - xy) - \frac{1}{2}(x^2 + y^2) - z = 0$$

Det gir ligningene

$$\begin{array}{ll} (1) & 0 = 2x\lambda + (\dfrac{-y}{1 - xy} - x - 0)\mu \\[3mm] (2) & 0 = 2y\lambda + (\dfrac{-x}{1 - xy} - y - 0)\mu \\[3mm] (3) & 1 = 0\lambda + (-1)\mu \\[1mm] (4) & x^2 + y^2 - 1 = 0 \\[1mm] (5) & \ln(1 - xy) - \dfrac{1}{2}(x^2 + y^2) - z = 0 \end{array}$$

Vi ser med en gang at $x \neq 0$ og $y \neq 0$ fordi $x = 0$ bare når $y = 0$ og vice versa (se ligning (1) og (2)), noe som strider mot ligning (4).

Løser vi ligningssystemet, får vi at $x^2 = y^2 = \frac{1}{2}$. Det gir de samme fire punktene som før.

Flere alternativ finnes naturligvis også. For eksempel, løs $g(x, y, z) = 0$ med hensyn på $y$, sett inn i $h(x, y, z)$ og maksimer/minimer $f(x, y, z)$ under én bibetingelse.

*Kjeldevarsel: i løsningsforslaget er venstre side av ligning (3) trykt som «1 = 0λ + (−1 = µ» — trykkfeil for «1 = 0λ + (−1)µ» (mønsteret frå (1) og (2) og krava til ∇h viser at leddet er (−1)µ, dvs. µ = −1); i tabellen over er òg $z(\pi/4)$ trykt med bokstavane «pi» i matematikk-fonten. Begge stadene er teken vare på som rette her, og matematikken i resten er upåverka.*

Kildesett: course=SIF5005 term=sommer year=2000 problem=4 file=sif5005_00k.pdf
