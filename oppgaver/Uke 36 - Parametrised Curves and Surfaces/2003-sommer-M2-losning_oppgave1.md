### **Løsning til Oppgave 1**

**a)** Kurven er en spiral som ligger på sylinderen med ligning $x^2 + y^2 = 1$. Spiralen gjør to omdreininger om sylinderen (vinkelen $2t$ vokser fra $0$ til $4\pi$) og strekker seg i lengden $2\pi$ langs sylinderen (fra $z = 0$ til $z = 2\pi$). Figuren i arket viser kurven sammen med sylinderen den ligger på.

Hastighetsvektoren er

$$\mathbf{v}(t) = \mathbf{r}'(t) = -2\sin(2t)\mathbf{i} + 2\cos(2t)\mathbf{j} + \mathbf{k}.$$

Farten (lengden av hastighetsvektoren) er $|\mathbf{v}| = \sqrt{5}$, altså konstant. Derivasjon av ligningen $|\mathbf{v}|^2 = 5$ gir $2\mathbf{v} \cdot \mathbf{a} = 0$, der $\mathbf{a} = \mathbf{v}'$ er akselerasjonsvektoren. Altså er akselerasjonsvektoren normalt på hastighetsvektoren. (Dette kunne vi selvsagt også sett ved å regne ut $\mathbf{a}$ og beregne prikkproduktet.)

**b)** Om kurven hadde vært en sirkel på tvers av aksens retning i sylinderen, ville krumningsradien vært 1. Siden den ligger på skrå, må krumningsradien være større.

Vi kan selvsagt også regne ut dette: Bruk formelen for dekomponering av akselerasjonsvektoren fra formellisten. I dette tilfellet er $v^2(t) = 5$ og $v'(t) = 0$. Spesielt, siden $|\mathbf{N}(t)| = 1$ kan vi ta lengden av hver side i formelen og få $|\mathbf{a}(t)| = 5\kappa(t)$. Direkte utregning gir

$$\mathbf{a}(t) = \mathbf{v}'(t) = -4\cos(2t)\mathbf{i} - 4\sin(2t)\mathbf{j},$$

så $|\mathbf{a}(t)| = 4$. Dermed blir $\kappa(t) = 4/5$, og krumningsradien i ethvert punkt på kurven blir $1/\kappa(t) = 5/4 > 1$.

Kildesett: course=SIF5005 term=sommer year=2003 problem=1 file=sif5005_03k.pdf
