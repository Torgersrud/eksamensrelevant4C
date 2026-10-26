### **Problem 4** (Anatomy of a tensor: order, fibers, slices and storage, 8 points)

A measurement campaign records the reading of $4$ catalysts at $3$ temperatures, under $2$ pressure levels, at $5$ time points. The $120$ numbers are stored in one $4$-way tensor
$Y\in\mathbb{R}^{4\times 3\times 2\times 5}$ with entries $y_{i,j,k,\ell}$ (catalyst, temperature, pressure, time).

A second, smaller data set is the $3$-tensor $\mathbf{X}\in\mathbb{R}^{3\times 2\times 2}$ given by its two frontal slices

$$X_{::1}=\begin{pmatrix}2&0\\ -1&3\\ 4&1\end{pmatrix},\qquad X_{::2}=\begin{pmatrix}1&-2\\ 0&4\\ 3&-1\end{pmatrix}.$$

a) State the order, the mode sizes and the number of entries of $Y$, and say how many bytes $Y$ occupies when every entry is stored as a `float64` (8 bytes per number). How many mode-2 fibers $y_{i,:,k\ell}$ and how many mode-4 fibers $y_{ijk:}$ does $Y$ have, and how long is each of them? Give the general formula for the number of mode-$k$ fibers of an $n_1\times\cdots\times n_d$ tensor.

b) A *mode-$k$ hyperslice* of a tensor is obtained by fixing the index in mode $k$ and leaving all the other indices free. How many mode-3 hyperslices does $Y$ have, and how many entries does each of them contain? Fixing the indices in **two** modes instead gives an ordinary matrix; for each of the six pairs of modes, say how many such matrices $Y$ contains and what size they have.

c) For $\mathbf{X}$ above, write out the five subparts below as vectors or matrices, and say for each whether it is a column fiber, a row fiber, a tube fiber, a frontal slice or a horizontal slice:

$$x_{:12},\qquad x_{2:1},\qquad x_{32:},\qquad X_{::1},\qquad X_{1::}.$$

d) A rank-$r$ CP representation $[\![A_1,\dots,A_d]\!]$ of a $d$-way tensor stores the $d$ factor matrices instead of all the entries. How many numbers does such a representation store? For a $300\times 250\times 120$ tensor represented with rank $8$, give the number of stored numbers, the saving against keeping every entry, and the ratio between the two storages. What inequality must $r$ satisfy for a factor representation to save storage at all, and what is the largest rank for which a CP representation of the campaign tensor $Y$ still saves storage?

*Kjeldevarsel: Syntetisk oppgåve — oppgåveforma er tilpassa frå øvingsoppgåver i Ballard & Kolda, «Tensor Decompositions for Data Science» (Cambridge University Press, final draft mars 2025), kap. 1–2; ingen tekst eller tal er henta frå utkastet, og definisjonane og formlane oppgåva byggjer på er standardstoff som òg står i den offentleg utgitte rapporten Kolda & Bader, «Tensor Decompositions and Applications», SAND2007-6702 (2007).*
