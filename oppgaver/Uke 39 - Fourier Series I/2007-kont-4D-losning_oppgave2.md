### **Løsning til Oppgave 2**

Funksjonen $f(x)$ er kontinuerlig i $x = \pi$. Vi har at $f(\pi) = 4\pi^4$ og at $f(\pi)$ er lik fourierrekken til $f(x)$ innsatt $x = \pi$.

Det er gitt at Fourierrekken til $f(x)$ er

$$4\pi^4 = f(\pi) = \frac{28\pi^4}{15} + \sum_{n=1}^{\infty} \frac{16(-1)^n (n^2\pi^2 - 3)}{n^4} \cos n\pi =$$

$$= \frac{28\pi^4}{15} + 16 \sum_{n=1}^{\infty} \frac{n^2\pi^2 - 3}{n^4} =$$

Dvs at

$$\sum_{n=1}^{\infty} \frac{n^2\pi^2 - 3}{n^4} = \frac{2\pi^4}{15}$$

Andre del av oppgaven: Finn også summen til rekken

$$\sum_{n=1}^{\infty} \frac{n^4\pi^4 - 6n^2\pi^2 + 9}{n^8}.$$

Vi bruker Parsevals identitet:

$$\int_{-\pi}^{\pi} f(x)^2 \, dx = 2\pi \cdot \left( \frac{28\pi^4}{15} \right)^2 + \pi \sum_{n=1}^{\infty} \left( \frac{16(-1)^n (n^2\pi^2 - 3)}{n^4} \right)^2 \tag{15}$$

Det er oppgitt at integralet er $\int_{-\pi}^{\pi} f(x)^2 \, dx = \frac{2656}{315}\pi^9$ Uttrykket (15) og vedien av integralet gir

$$\frac{2656}{315}\pi^9 = \frac{1568}{225}\pi^9 + 256\pi \sum_{n=1}^{\infty} \frac{n^4\pi^2 - 6n^4\pi^2 + 9}{n^8} \tag{16}$$

Løser vi for summen får vi

$$\sum_{n=1}^{\infty} \frac{n^4\pi^2 - 6n^4\pi^2 + 9}{n^8} = \frac{1}{256} \left( \frac{2656}{315} - \frac{1568}{225} \right) \pi^8 = \frac{\pi^8}{175} \tag{17}$$

Godkjent er også $(0.005714\ldots) \cdot \pi^8$ og $54.220177\ldots$.

**Kjeldevarsel:** Teljarane i (16) og (17) er trykte som $n^4\pi^2 - 6n^4\pi^2 + 9$; etter oppgåveteksten og kvadreringa av fourierkoeffisientane skal det vere $n^4\pi^4 - 6n^2\pi^2 + 9$. Sluttresultatet $\pi^8/175$ er rekna frå den rette teljaren og er kontrollert numerisk.

Kildesett: course=TMA4135 term=kont year=2007 problem=2 file=tma4135_07k.pdf
