### **Løsning til Oppgave 7**

Differansetabellen blir seende slik ut.

$$\begin{array}{|cc|cccc|}\hline x_j&f_j\!=\!f[x_j]&f[x_j,x_{j+1}]&f[x_j,x_{j+1},x_{j+2}]&f[x_j,x_{j+1},x_{j+2},x_{j+3}]&f[x_j,x_{j+1},x_{j+2},x_{j+3},x_{j+4}]\\\hline -1&-7&&&&\\ & &3&&&\\ 1&-1&&-2&&\\ & &-3&&1&\\ 2&-4&&2&&0\\ & &1&&1&\\ 3&-3&&6&&\\ & &19&&&\\ 5&35&&&&\\\hline\end{array}$$

Dividerte differanser på det gitte datasettet gir:

$$f_0=-7$$

$$f[x_0,x_1]=3$$

$$f[x_0,x_1,x_2]=-2$$

$$f[x_0,x_1,x_2,x_3]=1$$

$$f[x_0,x_1,x_2,x_3,x_4]=0$$

Interpolasjonspolynomet er dermed gitt som:

$$p(x)=f_0+(x-x_0)f[x_0,x_1]+(x-x_0)(x-x_1)f[x_0,x_1,x_2]$$

$$\qquad+(x-x_0)(x-x_1)(x-x_2)f[x_0,x_1,x_2,x_3]$$

$$\qquad+\,(x-x_0)(x-x_1)(x-x_2)(x-x_3)f[x_0,x_1,x_2,x_3,x_4]$$

$$=1+(x-(-1))\cdot 3+(x-(-1))(x-1)\cdot(-2)$$

$$\quad+\,(x-(-1))(x-1)(x-2)\cdot 1+(x-(-1))(x-1)(x-2)(x-3)\cdot 0$$

$$=-7+3(x+1)-2(x^2-1)+(x^2-1)(x-2)$$

$$=x^3-4x^2+2x.$$

*Kjeldevarsel: I den nest øverste linja i løsningsforslaget står det "$=1+(x-(-1))\cdot 3+\cdots$", men det første leddet skal være $f_0=-7$, ikke $1$. De påfølgende leddene og sluttsvaret $p(x)=x^3-4x^2+2x$ er korrekte; vi har kontrollert at dette polynomet passerer alle fem datapunktene $(-1,-7)$, $(1,-1)$, $(2,-4)$, $(3,-3)$ og $(5,35)$.*

Kildesett: course=TMA4135 term=kont year=2010 problem=7 file=tma4135_10k.pdf
