### **Solution to Problem 3**

**Solution:**

(a) Set up the system of linear equations based on the points, i.e. substitute each point into the polynomial equation: For $(-1,3)$:

$$a(-1)^2+b(-1)+c=3\quad\Rightarrow\quad a-b+c=3\ \ \ (1)$$

For $(2,2)$ we get

$$a(2)^2+b(2)+c=2\quad\Rightarrow\quad 4a+2b+c=2.$$

Finally, the point $(1,4)$:

$$a(1)^2+b(1)+c=4\quad\Rightarrow\quad a+b+c=4.$$

We now have the following system of equations:

$$\begin{array}{r}a-b+c=3\\ 4a+2b+c=2\\ a+b+c=4\end{array}$$

The unique solution is $a=-\frac{5}{6}$, $b=\frac{1}{2}$, $\frac{13}{3}$.

Hence, the solution is given by

$$p(x)=-\frac{5}{6}x^2+\frac{1}{2}x+\frac{13}{3}.$$

(b) We set up $A$ like

$$A=\begin{pmatrix}-1&1\\ 2&1\\ 1&1\end{pmatrix},$$

and

$$b=\begin{pmatrix}3\\ 2\\ 4\end{pmatrix}.$$

The least-square solutions of $Ax=b$ are the solutions of the normal equations

$$A^{T}Ax=A^{T}b.$$

Let us find $A^{T}$:

$$A^{T}=\begin{pmatrix}-1&2&1\\ 1&1&1\end{pmatrix}$$

and hence

$$A^{T}A=\begin{pmatrix}-1&2&1\\ 1&1&1\end{pmatrix}\begin{pmatrix}-1&1\\ 2&1\\ 1&1\end{pmatrix}=\begin{pmatrix}6&2\\ 2&3\end{pmatrix}.$$

Furthermore, we have

$$A^{T}b=\begin{pmatrix}5\\ 9\end{pmatrix}.$$

In summary, we have to solve

$$\begin{pmatrix}6&2\\ 2&3\end{pmatrix}\begin{pmatrix}d\\ e\end{pmatrix}=\begin{pmatrix}5\\ 9\end{pmatrix},$$

which has as solution: $d=-\frac{3}{14}$, $\ \ e=\frac{22}{7}$.

Hence, we get as final answer:

$$p(x)=-\frac{3x}{14}+\frac{22}{7}.$$

Kildesett: course=TMA4110 term=host year=2025 problem=3 file=exam_tma4110_correct_solutions.pdf
