### **Løsning til Oppgave 5**

**a)** Find polynomial of smallest possible degree which solves the interpolation problem:

$$\begin{array}{c|ccccc}t_n&-2&-1&0&1&2\\ \hline p(t_n)&3&1&1&3&7\end{array}$$

$$p(t)=1+t+t^2$$

**b)** Apply the Simpson method for evaluating

$$\int_{-2}^{2}p(t)\,dt$$

with nodes at the points $-2,-1,0,1,2$ and compare the answer with the precise value of the integral.

Simpson:

$$\frac{1}{3}\left(3+4+2+12+7\right)=\frac{28}{3}$$

You need not evaluate the explicit value of the integral because the Simpson method is precise for polynomials of degree two.

Alternatively you may write

$$\int\limits_{-2}^{2}\left(1+t+t^2\right)dt=4+\frac{1}{3}16=\frac{28}{3}.$$

*Kjeldevarsel: LF er handskriven på engelsk (s. 10) og er transkribert ordrett, med det overstreke ordet «precise» i setninga «You need not evaluate the ~~precise~~ explicit value of the integral» utelate. Simpson-ledda $\frac{1}{3}(3+4\cdot1+2\cdot1+4\cdot3+7)=\frac{1}{3}(3+4+2+12+7)=\frac{28}{3}$ og integralet $4+\frac{16}{3}=\frac{28}{3}$ er kontrollreikna med sympy saman med interpolasjonspolynomet $1+t+t^2$ (treffar alle fem nodar; LF oppgjev ikkje utleiinga).*

Kildesett: course=TMA4125 term=var year=2006 problem=5 file=eksamen-bok_2006v.pdf
