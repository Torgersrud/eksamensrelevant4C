### **Løsning til Oppgave 5**

Området $R$ med grid.

[Figur: Det triangulære området $R$ i første kvadrant med hypotenusen fra $(0,1)$ til $(1,0)$ tegnet som hel linje, og gitterlinjer med stiplede linjer for $h=0.25$. Gitterpunktene er navngitt $U_{i,j}$: langs $x$-aksen $U_{0,0},U_{1,0},U_{2,0},U_{3,0},U_{4,0}$, langs $y$-aksen $U_{0,0},U_{0,1},U_{0,2},U_{0,3},U_{0,4}$, og på hypotenusen $U_{1,3},U_{2,2},U_{3,1}$. De tre indre punktene er merket $X=U_{1,1}$, $Y=U_{2,1}$ og $Z=U_{1,2}$.]

Verdiene på randen er alle lik null, dvs

$$U_{0,0}=U_{1,0}=U_{2,0}=U_{3,0}=U_{4,0}=U_{0,1}=U_{0,2}=U_{0,3}=U_{0,4}=U_{1,3}=U_{2,2}=U_{3,1}=0.$$

Bruk av 5-punktsformelen på de indre punktene $U_{1,1}$, $U_{2,1}$ og $U_{1,2}$ gir:

$$\frac{U_{0,1}+U_{2,1}+U_{1,0}+U_{1,2}-4\,U_{1,1}}{h^2}-16\,U_{1,1}=16(h+h)$$

$$\frac{U_{1,1}+U_{3,1}+U_{2,0}+U_{2,2}-4\,U_{2,1}}{h^2}-16\,U_{2,1}=16(2h+h)$$

$$\frac{U_{0,2}+U_{2,2}+U_{1,1}+U_{1,3}-4\,U_{1,2}}{h^2}-16\,U_{1,2}=16(h+2h)$$

Vi har her valgt å liste opp ligningene i naturlig orden.

Ved å benytte de kjente verdiene på randen, benytte at $h=0.25$ (dvs $16h^2=1$), og definere de ukjente verdiene som $X=U_{1,1}$, $Y=U_{2,1}$ og $Z=U_{1,2}$, reduserer ligningene seg til

$$Y+Z-5X=1/2$$

$$X-5Y=3/4$$

$$X-5Z=3/4$$

Disse ligningene kan også skrives på matriseform som

$$\begin{pmatrix}-5&1&1\\ 1&-5&0\\ 1&0&-5\end{pmatrix}\begin{pmatrix}X\\ Y\\ Z\end{pmatrix}=\begin{pmatrix}1/2\\ 3/4\\ 3/4\end{pmatrix}.$$

Kildesett: course=TMA4135 term=kont year=2010 problem=5 file=tma4135_10k.pdf
