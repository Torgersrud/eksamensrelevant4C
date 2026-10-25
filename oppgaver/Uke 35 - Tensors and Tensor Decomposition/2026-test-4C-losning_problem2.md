### **Solution to Problem 2** (Tensor decomposition, 8 points)

a) For ranks $r,s,t$ the Tucker decomposition approximates $\mathbf{X}$ by (2 P.)

$$\mathbf{G}\times_1 A\times_2 B\times_3 C=\sum_{i,j,k=1}^{r,s,t}g_{i,j,k}\,\mathbf{a}_i\circledast\mathbf{b}_j\circledast\mathbf{c}_k$$

with a core tensor $\mathbf{G}\in\mathbb{R}^{r\times s\times t}$ and $A\in\mathbb{R}^{m\times r}$, $B\in\mathbb{R}^{n\times s}$, $C\in\mathbb{R}^{p\times t}$. The canonical polyadic decomposition (CPD) of rank $r$ approximates $\mathbf{X}$ by (1 P.)

$$[\![A,B,C]\!]=\sum_{i=1}^{r}\mathbf{a}_i\circledast\mathbf{b}_i\circledast\mathbf{c}_i$$

with $A\in\mathbb{R}^{m\times r}$, $B\in\mathbb{R}^{n\times r}$, $C\in\mathbb{R}^{p\times r}$. Hence the CPD is the special case of the Tucker decomposition with $r=s=t$ and a superdiagonal core, i. e. $g_{i,j,k}=1$ if $i=j=k$ and $g_{i,j,k}=0$ otherwise. (1 P.)

b) The SVD of a matrix can be written in both forms,

$$U\Sigma V^{\top}=\sum_i\sigma_i\mathbf{u}_i\mathbf{v}_i^{\top}=\Sigma\times_1 U\times_2 V.$$

The CPD generalises the first form, a sum of rank-1 tensors, whose smallest possible number is the rank. (2 P.)

The Tucker decomposition generalises the second form, a core multiplied in each mode by a factor matrix, where the factor matrices can be chosen with orthonormal columns like $U$ and $V$. (2 P.)

*Furthermore*, for matrices both forms coincide, since $\Sigma$ is diagonal. For tensors this is in general not the case, since the core $\mathbf{G}$ is in general not superdiagonal.

Kildesett: course=TMA4432 term=test year=2026 problem=2 points=8 file=test-exam-math4c_web.pdf
