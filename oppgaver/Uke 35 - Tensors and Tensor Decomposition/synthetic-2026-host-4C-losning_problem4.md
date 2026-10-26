### **Solution to Problem 4** (Anatomy of a tensor: order, fibers, slices and storage, 8 points)

a) $Y$ is a $4$-tensor (order $4$) with mode sizes $n_1=4$, $n_2=3$, $n_3=2$, $n_4=5$, so it has
$4\cdot 3\cdot 2\cdot 5=120$ entries. As `float64` that is $120\cdot 8=960$ bytes. (1 P.)

A mode-$2$ fiber keeps the second index free and fixes the other three, so there are
$4\cdot 2\cdot 5=40$ of them, each of length $n_2=3$. A mode-$4$ fiber fixes modes $1,2,3$, so there are
$4\cdot 3\cdot 2=24$ of them, each of length $n_4=5$. In general an $n_1\times\cdots\times n_d$ tensor has
$\prod_{i\neq k}n_i$ mode-$k$ fibers, each of length $n_k$ — the entries with mode $k$ free and all the other indices frozen. (1 P.)

b) A mode-$3$ hyperslice fixes the third index, and the third mode has $n_3=2$ values, so $Y$ has $2$ mode-3 hyperslices, each with $4\cdot 3\cdot 5=60$ entries (a $4\times 3\times 5$ tensor). In general mode $k$ gives $n_k$ hyperslices with $\prod_{i\neq k}n_i$ entries. (1 P.)

Fixing two indices leaves the two remaining modes free, so the matrices come in six families:

$$\begin{array}{c|c|c}\text{fixed modes}&\text{number}&\text{size}\\\hline
1,2&4\cdot 3=12&2\times 5\\
1,3&4\cdot 2=8&3\times 5\\
1,4&4\cdot 5=20&3\times 2\\
2,3&3\cdot 2=6&4\times 5\\
2,4&3\cdot 5=15&4\times 2\\
3,4&2\cdot 5=10&4\times 3
\end{array}$$

 Altogether $12+8+20+6+15+10=71$ matrices. (1 P.)

c) The entries of $X$ are read off the slices with the first index running down the rows and the second along the columns.

$$x_{:12}=\begin{pmatrix}x_{1,1,2}\\ x_{2,1,2}\\ x_{3,1,2}\end{pmatrix}=\begin{pmatrix}1\\ 0\\ 3\end{pmatrix}\ \text{(column fiber, mode 1)},\qquad
x_{2:1}=\begin{pmatrix}x_{2,1,1}&x_{2,2,1}\end{pmatrix}=\begin{pmatrix}-1&3\end{pmatrix}\ \text{(row fiber, mode 2)},$$

$$x_{32:}=\begin{pmatrix}x_{3,2,1}\\ x_{3,2,2}\end{pmatrix}=\begin{pmatrix}1\\ -1\end{pmatrix}\ \text{(tube fiber, mode 3)},\qquad
X_{::1}=\begin{pmatrix}2&0\\ -1&3\\ 4&1\end{pmatrix}\ \text{(frontal slice, mode 3)},$$

$$X_{1::}=\begin{pmatrix}x_{1,1,1}&x_{1,1,2}\\ x_{1,2,1}&x_{1,2,2}\end{pmatrix}=\begin{pmatrix}2&1\\ 0&-2\end{pmatrix}\ \text{(horizontal slice, mode 1)}.$$

The column fibers are the columns of the frontal slices, the row fibers are their rows, and the tube fibers run through the stack of slices at a fixed position. (2 P.)

d) The factor matrices of a rank-$r$ CP representation have sizes $n_1\times r,\dots,n_d\times r$, so the representation stores

$$r\,(n_1+n_2+\cdots+n_d)$$

numbers instead of $n_1n_2\cdots n_d$. For $300\times 250\times 120$ and $r=8$: all entries are
$300\cdot 250\cdot 120=9\,000\,000$ numbers, while the factors take
$8\cdot(300+250+120)=8\cdot 670=5\,360$ numbers — a saving of $8\,994\,640$ numbers, i.e. a factor
$9\,000\,000/5\,360\approx 1\,679$ (the factors use well under one per mille of the full storage). (1 P.)

The representation saves storage exactly when

$$r\,(n_1+\cdots+n_d)<n_1n_2\cdots n_d\qquad\Longleftrightarrow\qquad r<\frac{n_1n_2\cdots n_d}{n_1+\cdots+n_d}.$$

For $Y\in\mathbb{R}^{4\times 3\times 2\times 5}$ the right-hand side is $120/(4+3+2+5)=120/14\approx 8.6$, so a CP representation of $Y$ is smaller than the raw data only for ranks $r\le 8$: rank $8$ stores $112$ numbers against $120$, and rank $9$ already needs $126$. (1 P.)
