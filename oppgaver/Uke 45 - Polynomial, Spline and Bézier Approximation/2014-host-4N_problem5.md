### **Problem 5**

**a)** Find the polynomial of lowest degree that interpolate the points

$$\begin{array}{c||c|c|c|c|c}x_i&-2&1&0&1&2\\\hline f(x_i)&0&2&0&1&0\end{array}$$

*Kjeldevarsel: tabellen er førd ordrett — ho trykkjer noden $1$ to gonger, med verdi $2$ og $1$, og det finst ikkje noka polynomial som interpolerer dei punkta. Dei gamle eksamenssidene nemner eit errata for «problem 5a interpolation points», og fasiten reknar på punkta $(-2,0)$, $(-1,2)$, $(0,0)$, $(1,1)$, $(2,0)$ — altså med noden $-1$ for verdien $2$. Løysingsfila under følgjer fasiten sin rette nodetolking.*

**b)** We want to numerically evaluate the integral

$$\int_1^3x^2\ln(x)dx$$

with the Simpson method such that the approximation error is smaller than $0.001$. What is the largest value of the step size $h$ that we can choose such that this accuracy is guaranteed? Use this $h$ to compute a numerical approximation of the above integral by the Simpson method. (Use only 4 decimals in your computations)

Kildesett: course=TMA4130 term=host year=2014 problem=5 file=eksam2014.pdf
