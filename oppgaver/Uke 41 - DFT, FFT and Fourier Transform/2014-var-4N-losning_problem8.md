### **Solution to Problem 8**

**a)** The component $\frac{1}{N}\hat{y}_{n}e^{inx_{k}}$ is an interpolant for the function $\frac{1}{N}\hat{y}_{n}e^{inx}$. This function completes $n$ periods when $x$ goes from $0$ to $N$. Thus, the frequency is

$$f_{n}=\frac{n}{T}.$$

**b)** The function computes the Fourier transform $z=\text{fft}(y)$. Then it copies the first $k$ components of $z$ to $znew$, enforces the symmetry and calculates $ynew=\text{fft}^{-1}(znew)$

This corresponds to copying the $k$ lowest frequencies from $y$ to $ynew$. (This operation is known as a high-pass filter.) $ynew$ is a sound signal of the same length as $y$ and consists of the frequency components with $f<f_{k}=\frac{k}{T}$.

*Kjeldevarsel: LF-en kallar operasjonen ein «high-pass filter», men koden beheld nettopp dei $k$ lågaste frekvenskomponentane ($znew(i)=z(i)$ for $i=1,\ldots,k$, resten null) og fjernar dei høgaste — det vil seie eit lågpassfilter (low-pass filter). Frekvensomgrepet elles er korrekt; merknaden om misneminga ligg òg i SPOT-CHECK.*

Kildesett: course=TMA4123 term=var year=2014 problem=8 file=v14-english.pdf
