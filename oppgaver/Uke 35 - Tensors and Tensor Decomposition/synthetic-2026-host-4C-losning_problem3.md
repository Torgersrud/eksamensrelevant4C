### **Solution to Problem 3** (Matricization and k-mode products, 10 points)

a) The columns are indexed by the pairs $(j,k)$, $(i,k)$, $(i,j)$ respectively, running first index fastest:

$$\mathbf{X}^{(1)}=\begin{pmatrix}x_{111}&x_{121}&x_{112}&x_{122}\\ x_{211}&x_{221}&x_{212}&x_{222}\end{pmatrix}=\begin{pmatrix}1&2&5&6\\ 3&4&7&8\end{pmatrix},$$

$$\mathbf{X}^{(2)}=\begin{pmatrix}x_{111}&x_{211}&x_{112}&x_{212}\\ x_{121}&x_{221}&x_{122}&x_{222}\end{pmatrix}=\begin{pmatrix}1&3&5&7\\ 2&4&6&8\end{pmatrix},\qquad
\mathbf{X}^{(3)}=\begin{pmatrix}x_{111}&x_{211}&x_{121}&x_{221}\\ x_{112}&x_{212}&x_{122}&x_{222}\end{pmatrix}=\begin{pmatrix}1&3&2&4\\ 5&7&6&8\end{pmatrix}.$$

(One point each. Note that $\mathbf{X}^{(3)}$ is just the two frontal slices, each read "first index fastest", stacked as rows.) (3 P.)

b) The slices of $Y$ are $Y_{::l}=\sum_k m_{l,k}X_{::k}$, so

$$Y_{::1}=1\cdot X_{::1}+0\cdot X_{::2}=\begin{pmatrix}1&2\\ 3&4\end{pmatrix},\qquad Y_{::2}=1\cdot X_{::1}+1\cdot X_{::2}=\begin{pmatrix}6&8\\ 10&12\end{pmatrix}.$$ (2 P.)

Reading these rows first index fastest gives $Y^{(3)}=\begin{pmatrix}1&3&2&4\\ 6&10&8&12\end{pmatrix}$, and indeed

$$MX^{(3)}=\begin{pmatrix}1&0\\ 1&1\end{pmatrix}\begin{pmatrix}1&3&2&4\\ 5&7&6&8\end{pmatrix}=\begin{pmatrix}1&3&2&4\\ 6&10&8&12\end{pmatrix}=Y^{(3)}.$$ (1 P.)

c) Column by column, $z_{i,k}=x_{i,1,k}-x_{i,2,k}$ is the row difference of slice $X_{::k}$:

$$Z=\begin{pmatrix}1-2&5-6\\ 3-4&7-8\end{pmatrix}=\begin{pmatrix}-1&-1\\ -1&-1\end{pmatrix}.$$ (1 P.)

The $k$-th column of $Z$ is $\mathbf{v}^{\top}$ applied to the corresponding slice from the left, $Z_{:k}=X_{::k}\mathbf{v}=\mathbf{x}_{:1,k}-\mathbf{x}_{:2,k}$, the difference of the two rows of the slice. Multiplying a mode by a vector contracts that mode and lowers the order of the tensor by one. (1 P.)

d) The columns of $C\odot B$ are $\mathbf{c}_1\otimes\mathbf{b}_1$ and $\mathbf{c}_2\otimes\mathbf{b}_2$ with $\mathbf{b}_1=(1,1)^{\top}$, $\mathbf{b}_2=(1,2)^{\top}$, $\mathbf{c}_1=(1,0)^{\top}$, $\mathbf{c}_2=(0,1)^{\top}$:

$$C\odot B=\begin{pmatrix}1&0\\ 1&0\\ 0&1\\ 0&2\end{pmatrix},\qquad (C\odot B)^{\top}=\begin{pmatrix}1&1&0&0\\ 0&0&1&2\end{pmatrix},$$

$$\mathbf{X}^{(1)}=A\,(C\odot B)^{\top}=\begin{pmatrix}1&0\\ 1&1\end{pmatrix}\begin{pmatrix}1&1&0&0\\ 0&0&1&2\end{pmatrix}=\begin{pmatrix}1&1&0&0\\ 1&1&1&2\end{pmatrix}.$$ (2 P.)

(Check: directly, $\mathbf{X}=[\![A,B,C]\!]$ has slices $X_{::1}=\mathbf{a}_1\mathbf{b}_1^{\top}=\begin{pmatrix}1&1\\ 1&1\end{pmatrix}$ and $X_{::2}=\mathbf{a}_2\mathbf{b}_2^{\top}=\begin{pmatrix}0&0\\ 1&2\end{pmatrix}$, whose first-index-fastest rows are exactly $(1,1,0,0)$ and $(1,1,1,2)$.)
