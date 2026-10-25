### **Løsning til Oppgave 5**

Området $R$ med grid.

[Figur: Det triangulære området $0 < y < x < 1$ med hjørne i $(0,0)$, $(1,0)$ og $(1,1)$. Gitterpunkter med $h = 0.25$ er merka: på y-aksen/nedenfor $U_{1,0}$, $U_{2,0}$, $U_{3,0}$; langs hypotenusen $U_{1,1}$, $U_{2,2}$, $U_{3,3}$; langs høgresida $U_{4,1}$, $U_{4,2}$, $U_{4,3}$; dei tre indre punkta $X$ i $(0.5, 0.25)$, $Y$ i $(0.75, 0.25)$ og $Z$ i $(0.75, 0.5)$, stipla linjer frå naboane.]

Verdiene på randen er

$$U_{4,1} = U_{4,2} = U_{4,3} = U_{1,1} = U_{2,2} = U_{3,3} = 0, \quad U_{1,0} = U_{3,0} = 3 \quad \text{og} \quad U_{2,0} = 4.$$

Bruk av 5-punktsformelen på de indre punktene $U_{2,1}$, $U_{3,1}$ og $U_{3,2}$ gir:

$$
\begin{aligned}
U_{3,1} + U_{1,1} + U_{2,2} + U_{2,0} - 4U_{2,1} &= 0 \\
U_{4,1} + U_{2,1} + U_{3,2} + U_{3,0} - 4U_{3,1} &= 0 \\
U_{4,2} + U_{2,2} + U_{3,3} + U_{3,1} - 4U_{3,2} &= 0
\end{aligned}
$$

Vi har her valgt å liste opp ligningene i naturlig orden.

Ved å benytte de kjente verdiene på randen og definere de ukjente verdiene som $X = U_{2,1}$, $Y = U_{3,1}$ og $Z = U_{3,2}$, reduserer ligningene seg til

$$
\begin{aligned}
4X - \phantom{X}Y \phantom{{}-Z} &= 4 \\
-X + 4Y - \phantom{4}Z &= 3 \\
\phantom{-X + {}} - \phantom{4}Y + 4Z &= 0
\end{aligned}
$$

Disse ligningene kan også skrives på matriseform som

$$\begin{pmatrix} 4 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 4 \end{pmatrix} \begin{pmatrix} X \\ Y \\ Z \end{pmatrix} = \begin{pmatrix} 4 \\ 3 \\ 0 \end{pmatrix}.$$

Kildesett: course=TMA4135 term=host year=2009 problem=5 file=tma4135_09h.pdf
