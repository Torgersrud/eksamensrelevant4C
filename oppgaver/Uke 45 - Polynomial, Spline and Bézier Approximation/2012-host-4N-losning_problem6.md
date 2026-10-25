### **Solution to Problem 6**

**a)** We need to calculate Lagrange's interpolation polynomial. With the notation

$$P_{1}=(x-\frac{1}{2})(x-1)(x-\frac{3}{2})(x-2),$$

$$P_{2}=x(x-1)(x-\frac{3}{2})(x-2),$$

$$P_{3}=x(x-\frac{1}{2})(x-\frac{3}{2})(x-2),$$

$$P_{4}=x(x-\frac{1}{2})(x-1)(x-2),$$

$$P_{5}=(x-\frac{1}{2})(x-1)(x-\frac{3}{2}),$$

the interpolating polynomial is given by

$$-11P_{1}(x)/P_{1}(0)-7P_{2}(x)/P_{2}(\frac{1}{2})+3P_{3}(x)/P_{3}(1)+25P_{4}(x)/P_{4}(\frac{3}{2})+65P_{5}(x)/P_{5}(2).$$

This simplifies to

$$P(x)=8x^{3}+6x-11.$$

Alternatively, **we can use Newton's divided-difference formula** for Lagrange's interpolation polynomial.

**b)** Since Simpson's method is *exact* for polynomials of degree less than or equal to three, the error is zero.

*Kjeldevarsel: Eksamen-PDF-en for dette haustsettet blei aldri publisert; løysingsfila `solutions_2012h.pdf` er difor Kildesett, og oppgåveteksten er ikkje gjenteken i løysinga — nodane $(0,\ldots,2)$ og tabellverdiane $-11,-7,3,25,65$ følgjer berre av fasiten. Setninga om Newton-varianten er trykt som «Newton's divided-difference formula for Lagrange's interpolation polynomial» og er bevart ordrett; interpolasjonspolynomet $P(x)=8x^3+6x-11$ er kontrollrekna med sympy og treffer nodane nøyaktig.*

Kildesett: course=TMA4130 term=host year=2012 problem=6 file=solutions_2012h.pdf
