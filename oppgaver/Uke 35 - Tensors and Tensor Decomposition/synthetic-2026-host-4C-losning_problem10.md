### **Solution to Problem 10** (Tucker decomposition by hand: reconstruction, norms and one HOOI update, 8 points)

a) The columns of $U$ are $\mathbf{u}_1=\tfrac13(2,1,2)^{\top}$ and $\mathbf{u}_2=\tfrac13(1,2,-2)^{\top}$: $\|\mathbf{u}_1\|^2=\|\mathbf{u}_2\|^2=(4+1+4)/9=1$ and $\mathbf{u}_1\cdot\mathbf{u}_2=(2+2-4)/9=0$, so $U^{\top}U=I_2$. The columns of $W$ are $(\tfrac35,\tfrac45,0,0)^{\top}$ and $(0,0,\tfrac35,\tfrac45)^{\top}$, both of length $(9+16)/25=1$ and orthogonal (disjoint supports), so $W^{\top}W=I_2$. (1 P.)

With $V=I_2$ the slice formula is $T_{::k}=w_{k1}\,UG_{::1}+w_{k2}\,UG_{::2}$, and

$$UG_{::1}=\frac13\begin{pmatrix}2&1\\ 1&2\\ 2&-2\end{pmatrix}\begin{pmatrix}2&2\\ 0&0\end{pmatrix}=\frac13\begin{pmatrix}4&4\\ 2&2\\ 4&4\end{pmatrix},\qquad UG_{::2}=\frac13\begin{pmatrix}2&1\\ 1&2\\ 2&-2\end{pmatrix}\begin{pmatrix}1&0\\ 0&2\end{pmatrix}=\frac13\begin{pmatrix}2&2\\ 1&4\\ 2&-4\end{pmatrix}.$$

Row $1$ of $W$ is $(\tfrac35,0)$ and row $3$ is $(0,\tfrac35)$, so

$$T_{::1}=\frac35\,UG_{::1}=\begin{pmatrix}\tfrac45&\tfrac45\\[2pt] \tfrac25&\tfrac25\\[2pt] \tfrac45&\tfrac45\end{pmatrix},\qquad T_{::3}=\frac35\,UG_{::2}=\begin{pmatrix}\tfrac25&\tfrac25\\[2pt] \tfrac15&\tfrac45\\[2pt] \tfrac25&-\tfrac45\end{pmatrix},$$

exactly the measured slices (rows $2$ and $4$ of $W$ carry the factor $\tfrac45$ and reproduce slices $2$ and $4$). (1 P.)

b) Only $g_{2,2,2}=2$ survives with $i=3$, $j=2$, $k=4$: $t_{3,2,4}=g_{222}\,u_{32}\,v_{22}\,w_{42}=2\cdot\big(-\tfrac23\big)\cdot1\cdot\tfrac45=-\tfrac{16}{15}$, which is the $(3,2)$ entry of $T_{::4}$ above. (1 P.)

For $Y=\mathbf{X}\times_n Q$ the mode-$n$ unfolding satisfies $Y^{(n)}=QX^{(n)}$, and the Frobenius norm of a tensor equals that of any of its unfoldings; if $Q^{\top}Q=I$ then $\|Y^{(n)}\|_F^2=\operatorname{tr}(X^{(n)\top}Q^{\top}QX^{(n)})=\|X^{(n)}\|_F^2$, so the mode product changes no entry-energy. Applying this three times ($\times_2 V$ with $V=I_2$ trivially), $\|\mathbf{T}\|_F=\|\mathbf{G}\times_1U\times_3W\|_F=\|\mathbf{G}\|_F$. And $\|\mathbf{G}\|_F^2=2^2+2^2+1^2+2^2=13$, so $\|\mathbf{T}\|_F^2=13$ — summing the squares of the $24$ printed entries gives $2925/225=13$ as it must. (1 P.)

c) Multiplying the Gram by each candidate:

$$\frac19\begin{pmatrix}40&26&28\\ 26&25&2\\ 28&2&52\end{pmatrix}\begin{pmatrix}2\\1\\2\end{pmatrix}=\frac19\begin{pmatrix}162\\81\\162\end{pmatrix}=9\begin{pmatrix}2\\1\\2\end{pmatrix},\quad
\frac19\begin{pmatrix}40&26&28\\ 26&25&2\\ 28&2&52\end{pmatrix}\begin{pmatrix}1\\2\\-2\end{pmatrix}=\frac19\begin{pmatrix}36\\72\\-72\end{pmatrix}=4\begin{pmatrix}1\\2\\-2\end{pmatrix},$$

and $\frac19(40,26,28;-)\,( -2,2,1)^{\top}=\frac19(0,0,0)^{\top}=0\cdot(-2,2,1)^{\top}$ — three orthonormal eigenvectors with eigenvalues $9>4>0$. For orthonormal $U$ the trace $\operatorname{tr}(U^{\top}\mathbf{T}^{(1)}\mathbf{T}^{(1)\top}U)$ is a sum of two Rayleigh quotients, maximised by the two leading eigenvectors (Eckart–Young), so the HOOI update returns $U_{\text{new}}=\big[\tfrac13(2,1,2)^{\top}\ \ \tfrac13(1,2,-2)^{\top}\big]$ — precisely the factor $U$ printed in the problem statement (the eigenvalues are distinct, so even the column order is forced). The third eigenvalue $0$ is the squared residual of the best rank-$2$ mode-$1$ subspace: the data are *exactly* of multilinear rank $2$ in mode $1$, which is why a format with a $3\times2$ factor fits with residual $0$ — one HOOI sweep from the right $V,W$ lands on the exact representation (and by b) no energy is lost in the other modes either). (2 P.)

The cheap route: the Tucker form obeys the same unfolding machinery as CP, $\mathbf{T}^{(1)}=U\,G^{(1)}(W\odot V)^{\top}$, so with the mixed-product/Hadamard identity of Problem 2 d),

$$\mathbf{T}^{(1)}\mathbf{T}^{(1)\top}=U\,G^{(1)}\underbrace{(W\odot V)^{\top}(W\odot V)}_{(W^{\top}W)\circ(V^{\top}V)=I_2\circ I_2=I_2}G^{(1)\top}U^{\top}=U\,G^{(1)}G^{(1)\top}U^{\top}.$$

Here $G^{(1)}=\begin{pmatrix}2&2&1&0\\ 0&0&0&2\end{pmatrix}$ (rows orthogonal with norms $3$ and $2$), so $G^{(1)}G^{(1)\top}=\begin{pmatrix}9&0\\ 0&4\end{pmatrix}$ and $\mathbf{T}^{(1)}\mathbf{T}^{(1)\top}=9\mathbf{u}_1\mathbf{u}_1^{\top}+4\mathbf{u}_2\mathbf{u}_2^{\top}=\frac19\begin{pmatrix}40&26&28\\ 26&25&2\\ 28&2&52\end{pmatrix}$ — a $3\times3$ matrix built from the $2\times4$ core unfolding alone, never touching the data. (1 P.)

d) The representation stores $\|\mathbf{G}\|$-size $2\cdot2\cdot2=8$ core numbers, $3\cdot2=6$ entries in $U$, $4$ in $V$ and $4\cdot2=8$ in $W$: $8+6+4+8=26$ numbers against $3\cdot2\cdot4=24$ raw entries — at this size the Tucker format is *larger* than the tensor itself and buys nothing but structure. For a $600\times400\times500$ tensor with core $(2,2,2)$: $8+2(600+400+500)=8+3000=3008$ numbers against $600\cdot400\cdot500=120\,000\,000$ entries, a ratio of $120\,000\,000/3008\approx39\,900$ — compression by four orders of magnitude. (1 P.)
