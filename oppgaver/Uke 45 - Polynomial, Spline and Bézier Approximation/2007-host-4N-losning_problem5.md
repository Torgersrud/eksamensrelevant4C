### **Solution to Problem 5**

**a)** Find the polynomial $p_{2}(x)$ which interpolates

$$\begin{array}{c|ccc}x_{k}&-2&-1&2\\ \hline f_{k}&-13&-5&7\end{array}$$

using Lagrangian interpolation.

We need the cardinal polynomials, they are given by

$$l_{0}(x)=\frac{(x+1)(x-2)}{(-2+1)(-2-2)}=\frac{1}{4}(x+1)(x-2)$$

$$l_{1}(x)=\frac{(x+2)(x-2)}{(-1+2)(-1-2)}=-\frac{1}{3}(x+2)(x-2)$$

$$l_{2}(x)=\frac{(x+2)(x+1)}{(2+2)(2+1)}=\frac{1}{12}(x+2)(x+1).$$

We now find our polynomial as

$$p_{2}(x)=f_{0}l_{0}(x)+f_{1}l_{1}(x)+f_{2}l_{2}(x)=-x^{2}+5x+1.$$

**b)** We then add another datapoint. We now want to find the polynomial $p_{3}(x)$ of the lowest

$$\begin{array}{c|cccc}x_{k}&-2&-1&2&3\\ \hline f_{k}&-13&-5&7&4\end{array}.$$

You can choose how you find this polynomial yourself.

In order to save ourself some work here, we can use the fact that a polynomial is uniquely given by its data and nodal values. This means that we can reuse $p_{2}(x)$. We use Newtonian interpolation to find the polynomial as

$$p_{3}(x)=p_{2}(x)+f[x_{0},x_{1},x_{2},x_{3}]\left(x-x_{0}\right)\left(x-x_{1}\right)\left(x-x_{2}\right).$$

This yields

$$\begin{array}{cc|ccc}x_{k}&f_{k}&&&\\ \hline -2&-13&8&-1&-3/20\\ -1&-5&4&-7/4&\\ 2&7&-3&&\\ 3&4.&&&\end{array}$$

We now insert this to get

$$p_{3}(x)=p_{2}(x)-\frac{3}{20}\left(x+2\right)\left(x+1\right)\left(x-2\right)=-\frac{3}{20}x^{3}-\frac{23}{20}x^{2}+\frac{28}{5}x+\frac{8}{5}.$$

*Kjeldevarsel: LF er på engelsk og er transkribert ordrett, inkludert setninga «In order to save ourself some work here». Attmerkingar: (i) LF gjentek oppgåva i b) men droppar fragmentet «possible degree which interpolates the data set» — i LF sluttar setninga på «of the lowest» og tabellen kjem direkte etter; i eksamensarket står den fulle ordlyden, og LF si avkortede form er bevart ordrett; (ii) LF tabellen i b) har indeks $x_{k}$ der eksamensarket har $t_{k}$. Alt er kontrollreikna med sympy: $p_{2}=-x^{2}+5x+1$ treffer alle tre nodar, cardinalpolynoma $l_{0},l_{1},l_{2}$ gir same $p_{2}$, delt differens-tabellen har $f[x_{0},x_{1}]=8$, $f[x_{1},x_{2}]=4$, $f[x_{2},x_{3}]=-3$, $f[x_{0},x_{1},x_{2}]=-1$, $f[x_{1},x_{2},x_{3}]=-7/4$, $f[x_{0},x_{1},x_{2},x_{3}]=-3/20$, og $p_{3}=-\frac{3}{20}x^{3}-\frac{23}{20}x^{2}+\frac{28}{5}x+\frac{8}{5}$ treffer alle fire nodar.*

Kildesett: course=TMA4130 term=host year=2007 problem=5 file=exam-en_2007.pdf
