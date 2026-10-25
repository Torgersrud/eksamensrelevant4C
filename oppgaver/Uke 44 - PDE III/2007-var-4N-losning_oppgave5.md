### **Løsning til Oppgave 5**

a) Vi setter inn approksimasjonene til løsningen inn i de oppgitte approksimasjonene til de deriverte, og setter så lik. Resultatet blir

$$\frac{u_{i}^{j+1}-u_{i}^{j}}{k}=\ \frac{u_{i+1}^{j}-2u_{i}^{j}+u_{i-1}^{j}}{h^{2}}.$$

Om vi omrokerer litt får vi følgende skjema

$$u_{i}^{j+1}=u_{i}^{j}+r(u_{i+1}^{j}-2u_{i}^{j}+u_{i-1}^{j})\quad\mathrm{hvor}\quad r=\frac{k}{h^{2}}.$$

Dette er Eulers eksplisitte metode for varmelikningsligningen.

b) Med $n = 5$ og $k = 0.01$ blir $h = 2/5$ og $r = 0.0625$. De kjente verdiene ved $t = 0$ er

$$[u_{0}^{0},u_{1}^{0},u_{2}^{0},u_{3}^{0},u_{4}^{0},u_{5}^{0}]=[0,0,0.1,1,1,1].$$

gitt ved initialbetingelse og randverdier. Vi legger merke til at $u_{1}^{1}=u_{1}^{0}$ og $u_{4}^{1}=u_{4}^{0}$ på grunn av at den andrederiverte er lik null i $u_{1}^{0}$ og $u_{4}^{0}$. Videre regner vi ut

$$u_{2}^{1}=u_{2}^{0}+r(u_{3}^{0}-2u_{2}^{0}+u_{1}^{0})=0+0.0625(1-0+0)=0.0625$$

Tilsvarende utregning, evt. ved symmetribetraktninger får vi at $u_{4}^{1}=1-0.0625=0.9375$. Tilsammen gir dette oss

$$[u_{1}^{1},u_{2}^{1},u_{3}^{1},u_{4}^{1}]=[0,\ 0.0625,\ 0.9375,\ 1].$$

*Kjeldevarsel: facit er trykt på bokmål (PDF-s. 13–14) og er sitert ordrett. To trykkfeilar i facit står att som trykte: i den kjente verdiraden er tredje talet trykt $0.1$ ($u_{2}^{0}$), men både initialbetingelsen ($x_{2}=-0.2$) og facits eiga utrekning ($0+0.0625(1-0+0)$) seier $0$; og setninga «$u_{4}^{1}=1-0.0625=0.9375$» har galde subscript — talet høyrer til $u_{3}^{1}$, sidan facit like før har slått fast at $u_{4}^{1}=u_{4}^{0}=1$, og svarraden plasserer $0.9375$ på $u_{3}^{1}$-plassen. «Eulers eksplisitte metode» er trykt med avvikande staving (normalt «eksplicitte») og står att som trykt. Svaret $[0,0.0625,0.9375,1]$ er kontrollreikna med sympy frå skjemaet i a) med startraden $[0,0,0,1,1,1]$ og $r=0.0625$.*

Kildesett: course=TMA4123 term=var year=2007 problem=5 file=TMA4123_v07.pdf
