### **Oppgave 6**

En robot har posisjon $R$ i et rektangulært rom med hjørner $A,B,C,D$ hvor sidekantene har lengde $20$m og $10$m. Roboten finner sin posisjon ved signaler sendt ut fra hjørnene.

**a)** Roboten måler avstandene $|R-A|=15.5$m og $|R-B|=6.5$m. Tegn figur med skala slik at $1$m tegnes som $1$cm og finn posisjonen $R_0^*=(x_0,y_0)$ med en nøyaktighet på $1$m ved å måle på figuren.

De to avstandene gir to ikke-lineære ligninger som kan løses ved Newton's metode. La $R_0^*$ være startverdien og beregn en bedre approximasjon $R_1^*$ ved å utføre et steg med Newton's metode.

**b)** La startverdien være $R_0=C$ hvor $C$ er hjørnet nærmest hjørne $B$. Forklar hvordan en bedre approximasjon $R_1$ kan finnes ved en geometrisk tolkning av Newton's metode i dette tilfellet.

Finn $R_1$ ved å utføre et steg med Newton's metode med den geometriske metoden.

Anta at roboten kun har målingen $|R-B|=6.5$m tilgjengelig. Hvilket punkt $R_B$ vil Newton's metode konvergere mot da?

Anta at roboten har måling av avstanden fra alle fire hjørner tilgjengelig. Forklar hvordan Newton's metode kan brukes til å finne posisjonen $R$.

Kildesett: course=TMA4135 term=host year=2016 problem=6 file=tma4135_16h.pdf
