### **Løsning til Oppgave 1**

Vi skriver de to flateligningene på formen

$$F_1(x, y, z) = x^2 - y^2 - z = 0 \quad \text{og} \quad F_2(x, y, z) = xyz + 30 = 0,$$

og bruker gradientvektorer for å finne normalvektorene:

$$\nabla F_1(x, y, z) = \langle 2x, -2y, -1 \rangle, \qquad \mathbf{N_1} = \nabla F_1(-3, 2, 5) = \langle -6, -4, -1 \rangle;$$
$$\nabla F_2(x, y, z) = \langle yz, xz, xy \rangle, \qquad \mathbf{N_2} = \nabla F_2(-3, 2, 5) = \langle 10, -15, -6 \rangle.$$

En tangentvektor $\mathbf{T}$ må stå vinkelrett både på $\mathbf{N_1}$ og $\mathbf{N_2}$. Følgelig er

$$\mathbf{T} = \mathbf{N_1} \times \mathbf{N_2} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -6 & -4 & -1 \\ 10 & -15 & -6 \end{vmatrix} = \langle 9, -46, 130 \rangle$$

en tangentvektor i punktet $P(-3, 2, 5)$ for skjæringskurven mellom de to flatene.

*Kjeldevarsel: løsningsforslaget trykkjer funksjonsnotaasjonen $F_1(x, y, x)$ og $F_2(x, y, x)$ i den første linja — trykkfeil for $F_1(x, y, z)$ og $F_2(x, y, z)$, sidan utrekningane av $\nabla F_1$ og $\nabla F_2$ like nedanfor går på $(x, y, z)$; teksten her følgjer den rette notasjonen.*

Kildesett: course=SIF5005 term=sommer year=2002 problem=1 file=sif5005_02k.pdf
