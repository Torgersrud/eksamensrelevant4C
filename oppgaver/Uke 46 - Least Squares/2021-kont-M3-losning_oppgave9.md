### **Løsning til Oppgave 9**

**a)** Underrommet $U$ er planet gitt av ligningen $x=y$. Det oppnås fra planet som er utspent av $x$-aksen og $z$-aksen ved å rotere rundt $z$-aksen med vinkelen $\pi/4$.

**b)** En ortonormal basis av $U$ er gitt ved

$$\mathbf{u}_1=\begin{bmatrix}0\\ 0\\ 1\end{bmatrix},\quad \mathbf{u}_2=\begin{bmatrix}\sqrt{2}/2\\ \sqrt{2}/2\\ 0\end{bmatrix}.$$

Det nærmeste punktet er gitt av den ortogonale projeksjonen, og det kan beregnes som

$$\langle \mathbf{v},\mathbf{u}_1\rangle\mathbf{u}_1+\langle \mathbf{v},\mathbf{u}_2\rangle\mathbf{u}_2=3\begin{bmatrix}0\\ 0\\ 1\end{bmatrix}+\frac{3}{\sqrt{2}}\begin{bmatrix}\sqrt{2}/2\\ \sqrt{2}/2\\ 0\end{bmatrix}=\begin{bmatrix}3/2\\ 3/2\\ 3\end{bmatrix}.$$

**c)** Transformasjonen $T$ er en rotasjon rundt $z$-aksen med vinkelen $\pi/4$. Bildet av $U$ er gitt av planet som utspennes av $y$-aksen og $z$-aksen.

**d)** Den tredje standardbasisvektoren $\mathbf{e}_3$ er en egenvektor med egenverdi $1$. Siden $T$ beskriver en rotasjon med en vinkel ulik $0$ og ulik $\pi$, vil $T(\mathbf{u})$ og $\mathbf{u}$ ikke være parallelle, unntatt når $\mathbf{u}$ ligger på rotasjonsaksen, og da vil $T(\mathbf{u})=\mathbf{u}$. (Merk at hvis $T(\mathbf{u})=\lambda\mathbf{u}$ for en $\lambda$ ulik $0$, er $T(\mathbf{u})$ og $\mathbf{u}$ parallelle).

*Kjeldevarsel: den ortogonale basisen, projeksjonskoeffisientane $3$ og $3/\sqrt{2}$ og projeksjonspunktet $(3/2,3/2,3)$ er kontrollrekna med sympy.*

Kildesett: course=TMA4110 term=kont year=2021 problem=9 file=eksamen-TMA4110-TMA4115-2021Kont.pdf
