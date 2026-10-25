### **Solution to Problem 4** **Discrete Fourier Transform (12 points)**

a) We have
$$\mathcal{F}_5=\left(w_5^{jk}\right)_{j,k=0}^4=\begin{pmatrix}w_5^0&w_5^0&w_5^0&w_5^0&w_5^0\\ w_5^0&w_5^1&w_5^2&w_5^3&w_5^4\\ w_5^0&w_5^2&w_5^4&w_5^1&w_5^3\\ w_5^0&w_5^3&w_5^1&w_5^4&w_5^2\\ w_5^0&w_5^4&w_5^3&w_5^2&w_5^1\end{pmatrix}$$

b) The highest frequency is $k_{\max}=2$,

since periodicity of the discrete Fourier coefficients yields in this case
$$\hat f_0=c_0(g),\quad\hat f_1=c_1(g),\quad\hat f_2=c_2(g),\quad\hat f_3=c_{-2}(g),\quad\hat f_4=c_{-1}(g).$$
If higher frequencies occur we observe the *aliasing effect*

c) This set of discrete Fourier coefficients stems from a bandlimited function $g$ with only $\hat f_0=Nc_0(g)=c$ and hence so we have $c_0(g)=\frac{c}{5}$ and $c_k(g)=0$, $|k|>0$ hence $g$ is a constant function and using the same idea as in b) we get $\mathbf{f}=\frac{1}{5}(c,c,c,c,c)$.

**Grading manual**

a) (4p)

b) (1p) for the highest frequency, (2p) for the periodicity relation, (1p) for the aliasing effect

c) (4p)

Kildesett: course=TMA4125 term=var year=2023 problem=4 points=12 file=tma4125-matematikk-4n-2023v_lf.pdf
