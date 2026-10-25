### **Løsning til Oppgave 9**

Velg $h$ og $k$ (eller $M$ og $N$), la $x_i=ih$ og $t_n=kh$. For å tilnærme ligningen i et punkt $(x_i,t_n)$, bruk en foroverdifferanse i $t$-retningen og en sentraldifferanse i $x$-retningen. Dvs:

$$\frac{u(x_i,t_n+k)-u(x_i,t_n)}{k}\approx\frac{u(x_i+h,t_n)-2u(x_i,t_n)+u(x_i-h,t_n)}{h^2}$$

La $U_i^n\approx u(x_i,t_n)$ og differenseskjemaet kan skrives som

$$\frac{U_i^{n+1}-U_i^n}{k}=\frac{U_{i+1}^n-2U_i^n+U_{i-1}^n}{h^2}.$$

Ved å inkudere start- og rand-betingelser kan algoritmen skrives som

Oppgi $M$ og $N$.
Sett $h=1/M$, $k=1/N$ og $r=k/h^2$.
Sett inn startverdiene: $U_{i0}=ih(1-ih),\qquad i=0,1,\ldots,M.$
For $n=0,1,\ldots,N-1$:

$$U_0^{n+1}=0,\qquad U_M^{n+1}=0,$$
$$U_i^{n+1}=U_i^n+r(U_{i+1}^n-2U_i^n+U_{i-1}^n),\qquad i=1,2\ldots,M-1$$

Med de oppgitte steglengdene har vi $u(0.4,0.02)\approx U_2^1$. Vi vet at

$$U_1^0=0.16,\qquad U_2^0=0.24,\qquad U_3^0=0.24,$$

og

$$U_2^1=U_2^0+r(U_3^0-2U_2^0+U_1^0)=0.2.$$

Med $h=k$ vil $r=k/h^2=1/h>1$. Vi vet at løsningen er ustabil for $r>0.5$, så i det tilfellet vil den numeriske løsningen eksplodere.

Algoritmen kan skrives som Python-kode:

    import numpy as np

    N = 50       # Number of steps in the t-direction
    M = 5        # Number of steps in the x-direction

    h = 1/M
    k = 1/N
    r = k/h**2

    U = np.zeros((M+1,N+1))
    # Array to store the solution

    # Initial conditions
    for i in range(M+1):
        xi = i*h
        U[i,0] = xi*(1-xi)

    # Time-stepping algorithm
    for n in range(N):
        for i in range(1,M):
            U[i,n+1] = U[i,n] + r*(U[i+1,n]-2*U[i,n]+U[i-1,n])

Kildesett: course=TMA4135 term=kont year=2019 problem=9 file=tma4125-30-35-k19-bm.pdf
