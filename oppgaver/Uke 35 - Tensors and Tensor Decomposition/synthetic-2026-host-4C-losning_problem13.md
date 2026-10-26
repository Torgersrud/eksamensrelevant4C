### **Solution to Problem 13** (Capstone: a two-analyte fluorescence tensor, 8 points)

a) The two rank-$1$ profile products are

$$\mathbf{a}_1\mathbf{b}_1^{\top}=\begin{pmatrix}1\\2\\1\\0\end{pmatrix}\begin{pmatrix}2&1&1\end{pmatrix}=\begin{pmatrix}2&1&1\\ 4&2&2\\ 2&1&1\\ 0&0&0\end{pmatrix},\qquad
\mathbf{a}_2\mathbf{b}_2^{\top}=\begin{pmatrix}2\\0\\1\\1\end{pmatrix}\begin{pmatrix}1&2&0\end{pmatrix}=\begin{pmatrix}2&4&0\\ 0&0&0\\ 1&2&0\\ 1&2&0\end{pmatrix}.$$

Row $1$ of $C$ is $(1,3)$ and row $2$ is $(2,1)$, so

$$Y_{::1}=1\cdot\mathbf{a}_1\mathbf{b}_1^{\top}+3\cdot\mathbf{a}_2\mathbf{b}_2^{\top}=\begin{pmatrix}8&13&1\\ 4&2&2\\ 5&7&1\\ 3&6&0\end{pmatrix},\qquad
Y_{::2}=2\cdot\mathbf{a}_1\mathbf{b}_1^{\top}+1\cdot\mathbf{a}_2\mathbf{b}_2^{\top}=\begin{pmatrix}6&6&2\\ 8&4&4\\ 5&4&2\\ 1&2&0\end{pmatrix},$$

slice by slice identical to the measurements: $\mathbf{Y}=[\![A,B,C]\!]$ is an exact sum of two rank-$1$ tensors, so $\operatorname{rank}(\mathbf{Y})\le2$. The minor of $Y_{::1}$ on rows $1,2$ and columns $1,2$ is $8\cdot2-13\cdot4=-36\neq0$, so $Y_{::1}$ has matrix rank $2$; a rank-$1$ tensor has all frontal slices of rank $\le1$, hence $\operatorname{rank}(\mathbf{Y})\neq1$ and $\operatorname{rank}(\mathbf{Y})=2$. (2 P.)

b) $y_{3,2,1}=a_{31}b_{21}c_{11}+a_{32}b_{22}c_{12}=1\cdot1\cdot1+1\cdot2\cdot3=7$ — the $(3,2)$ entry of $Y_{::1}$. ✓ For the unfolding, the columns of $A\odot B$ are

$$\mathbf{a}_1\otimes\mathbf{b}_1=(2,4,2,0,\;1,2,1,0,\;1,2,1,0)^{\top},\qquad
\mathbf{a}_2\otimes\mathbf{b}_2=(2,0,1,1,\;4,0,2,2,\;0,0,0,0)^{\top}$$

(entries $a_i b_j$ with $i$ fastest within each emission band $j$). Then $C(A\odot B)^{\top}$ has row $k=\mathbf{c}_{k1}(\mathbf{a}_1\otimes\mathbf{b}_1)^{\top}+\mathbf{c}_{k2}(\mathbf{a}_2\otimes\mathbf{b}_2)^{\top}$:

$$\text{row }1=(\mathbf{a}_1\otimes\mathbf{b}_1)^{\top}+3(\mathbf{a}_2\otimes\mathbf{b}_2)^{\top}=(8,4,5,3,13,2,7,6,1,2,1,0),$$
$$\text{row }2=2(\mathbf{a}_1\otimes\mathbf{b}_1)^{\top}+(\mathbf{a}_2\otimes\mathbf{b}_2)^{\top}=(6,8,5,1,6,4,4,2,2,4,2,0),$$

and these are precisely the two data slices laid out with excitation index fastest, i.e. $\mathbf{Y}^{(3)}=C\,(A\odot B)^{\top}$ — the excitation–emission "fingerprint" of each sample is one row of the unfolding, assembled from the two analyte fingerprints with the concentrations as weights. (2 P.)

c) Using $\|\mathbf{T}_r\|_F^2=\|\mathbf{a}_r\|^2\|\mathbf{b}_r\|^2\|\mathbf{c}_r\|^2$ and $\langle\mathbf{T}_1,\mathbf{T}_2\rangle=(\mathbf{a}_1\cdot\mathbf{a}_2)(\mathbf{b}_1\cdot\mathbf{b}_2)(\mathbf{c}_1\cdot\mathbf{c}_2)$:

$$\|\mathbf{T}_1\|_F^2=(1{+}4{+}1{+}0)(4{+}1{+}1)(1{+}4)=6\cdot6\cdot5=180,\qquad
\|\mathbf{T}_2\|_F^2=(4{+}0{+}1{+}1)(1{+}4{+}0)(9{+}1)=6\cdot5\cdot10=300,$$
$$\langle\mathbf{T}_1,\mathbf{T}_2\rangle=(2{+}0{+}1)(2{+}2{+}0)(3{+}2)=3\cdot4\cdot5=60 .$$

So $\|\mathbf{Y}\|_F^2=180+300+2\cdot60=600$; the $24$ squared data entries give $378$ (slice $1$) $+\,222$ (slice $2$) $=600$ ✓. (The cross term is nonzero — the two analytes' fingerprints are *not* orthogonal, in contrast to Problem 12.) Dropping $B$ leaves exactly $\mathbf{T}_2$: error $=\|\mathbf{T}_2\|_F=\sqrt{300}=10\sqrt3\approx17.3$, relative error $\sqrt{300/600}=1/\sqrt2\approx71\%$; analyte $B$ carries half the total energy of the data, so the one-analyte summary is plainly unjustified. The claim "component $1$ is analyte $A$" is legitimate because this CP decomposition is *unique*: all three factor matrices have full column rank $2$, so $k_A=k_B=k_C=2$ and Kruskal's condition $k_A+k_B+k_C=6\ge2r+2=6$ holds (Problem 6 d)) — up to permutation and scaling of columns there is no other rank-$2$ decomposition, and the columns are pinned down by the physics as the two analytes. (2 P.)

d) A sample with concentrations $(1,1)$ is predicted to show

$$Y_{::3}^{\text{pred}}=\mathbf{a}_1\mathbf{b}_1^{\top}+\mathbf{a}_2\mathbf{b}_2^{\top}=\begin{pmatrix}4&5&1\\ 4&2&2\\ 3&3&1\\ 1&2&0\end{pmatrix}$$

(and the model even predicts its zeros in advance: entry $(4,3)$ must vanish because analyte $A$ is dark at excitation band $4$ and analyte $B$ is dark at emission band $3$ — a falsifiable prediction of the bilinear structure). Storage: the model keeps $4\cdot2+3\cdot2+2\cdot2=18$ numbers against $24$ raw entries ($192$ bytes as `float64`) — a ratio of only $24/18=4/3$, so the compression is incidental at this size, the payoff being the interpretation; on the real instrument, rank $5$ stores $5(240+300+800)=6\,700$ numbers against $240\cdot300\cdot800=57\,600\,000$ entries, a ratio of $\approx8\,600$. (2 P.)
