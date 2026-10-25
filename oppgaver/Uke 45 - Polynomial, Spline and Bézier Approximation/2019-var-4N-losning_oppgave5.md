### **Løsning til Oppgave 5**

Vi kaller punktene $x_k$ og funksjonsverdiene $f_k$, der $0\le k\le n$. Lagrangepolynomet

$$p(x)=\sum_{k=0}^{n}f_k\prod_{i\neq k}\frac{x-x_i}{x_k-x_i}$$

har maksimal grad $n$ og interpolerer tabellen, så vi vet at et interpolerende polynom eksisterer. Vi må vise at det er entydig. La $q$ være et annet interpolerende polynom av maksimal grad $n$. Polynomet $p-q$ har også maksimal grad $n$, og har $n+1$ nullpunkter, for

$$p(x_k)-q(x_k)=0$$

for alle $k$, siden begge polynomer interpolerer den samme tabellen. Men et polynom av grad $n$ kan maksimalt ha $n$ nullpunkter, med mindre det er identisk lik null, og derfor må $p=q$.

Kildesett: course=TMA4125 term=var year=2019 problem=5 file=eksamen-TMA4125-v19-BM.pdf
