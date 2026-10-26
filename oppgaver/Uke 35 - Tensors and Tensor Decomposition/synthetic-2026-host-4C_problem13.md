### **Problem 13** (Capstone: a two-analyte fluorescence tensor, 8 points)

A fluorimeter records each sample at $4$ excitation bands (rows) and $3$ emission bands (columns). Two samples are measured, giving the tensor $\mathbf{Y}\in\mathbb{R}^{4\times3\times2}$ with frontal slices

$$Y_{::1}=\begin{pmatrix}8&13&1\\ 4&2&2\\ 5&7&1\\ 3&6&0\end{pmatrix},\qquad Y_{::2}=\begin{pmatrix}6&6&2\\ 8&4&4\\ 5&4&2\\ 1&2&0\end{pmatrix}.$$

The lab suspects the samples are mixtures of two known analytes $A$ and $B$, and fits the bilinear model $\mathbf{Y}=[\![A,B,C]\!]$ with one CP term per analyte:

$$A=\begin{pmatrix}1&2\\ 2&0\\ 1&1\\ 0&1\end{pmatrix}_{4\times2}\ \text{(excitation profiles)},\qquad B=\begin{pmatrix}2&1\\ 1&2\\ 1&0\end{pmatrix}_{3\times2}\ \text{(emission profiles)},\qquad C=\begin{pmatrix}1&3\\ 2&1\end{pmatrix}_{2\times2}\ \text{(concentrations)}.$$

Columns $\mathbf{a}_1,\mathbf{a}_2$; $\mathbf{b}_1,\mathbf{b}_2$; rows of $C$ are the samples, so analyte $A$ sits at concentration $1$ in sample $1$ and $2$ in sample $2$.

a) Reconstruct both frontal slices from the model using $Y_{::k}=\sum_{r} c_{kr}\,\mathbf{a}_r\mathbf{b}_r^{\top}$ and check them against the measured data. What upper bound on $\operatorname{rank}(\mathbf{Y})$ follows? Rule out $\operatorname{rank}(\mathbf{Y})=1$ with a $2\times2$ minor and state $\operatorname{rank}(\mathbf{Y})$. (2 P.)

b) Compute the single entry $y_{3,2,1}$ from the CP entry formula $y_{ijk}=\sum_r a_{ir}b_{jr}c_{kr}$ and check it against the data. Then verify the mode-$3$ unfolding identity $\mathbf{Y}^{(3)}=C\,(A\odot B)^{\top}$: form the $12\times2$ product $A\odot B$ (columns $\mathbf{a}_r\otimes\mathbf{b}_r$, entries stacked with $i$ fastest), and multiply out both rows of $\mathbf{Y}^{(3)}$; the first must be $(8,4,5,3,13,2,7,6,1,2,1,0)$. (2 P.)

c) The component tensors are $\mathbf{T}_r=\mathbf{a}_r\circledast\mathbf{b}_r\circledast\mathbf{c}_r$. Compute $\|\mathbf{T}_1\|_F^2$, $\|\mathbf{T}_2\|_F^2$ and their inner product $\langle \mathbf{T}_1,\mathbf{T}_2\rangle$ as products of vector inner products, deduce $\|\mathbf{Y}\|_F^2$ and check it by summing the $24$ squared data entries. The intern reports a one-analyte ("drop analyte $B$") summary of the data: compute the Frobenius error and the relative error of that truncation, and say in one sentence whether the numbers justify keeping both components. Why is it legitimate here to say "component $1$ *is* analyte $A$" rather than merely "a rank-$1$ fit", cf. Problem 6? (2 P.)

d) A third sample is prepared with concentrations $(1,1)$ of the two analytes. Predict its full excitation–emission slice from the model. Finally, count the numbers the CP model stores here against the raw $4\times3\times2$ data (and the raw data as `float64` bytes), and give the storage ratio for the real instrument: rank $5$ on a $240\times300\times800$ measurement tensor. (2 P.)

*Kjeldevarsel: Syntetisk oppgåve — oppgåveforma er tilpassa frå øvingsoppgåver i Ballard & Kolda, «Tensor Decompositions for Data Science» (Cambridge University Press, final draft mars 2025), kap. 6 og 9–10; ingen tekst eller tal er henta frå utkastet, og scenarioet er ein heilt eigen oppdikta datagjengje, medan CP-modellen, unfoldingsidentiteten og lagringstala er standardstoff som òg står i den offentleg utgitte rapporten Kolda & Bader, «Tensor Decompositions and Applications», SAND2007-6702 (2007).*
