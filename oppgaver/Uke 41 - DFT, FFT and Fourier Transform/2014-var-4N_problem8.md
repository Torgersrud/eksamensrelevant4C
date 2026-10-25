### **Problem 8**

A signal is stored in the vector $\mathbf{y}=[y_{0},y_{1},\ldots,y_{N-1}]$, where $y_{i}$ are real numbers. $\mathbf{\hat{y}}=\text{fft}(\mathbf{y})$ is such that

$$y_{k}=\sum_{n=0}^{N-1}\frac{1}{N}\hat{y}_{n}e^{inx_{k}},$$

where $x_{k}=\frac{2\pi k}{N}$.

**a)** The signal represents a sound signal that is $T$ seconds long. What is the frequency of the component described by $\frac{1}{N}\hat{y}_{n}e^{inx_{k}}$? You do not have to consider aliasing in this task.

**b)** The following matlab-function takes a vector $\mathtt{y}$ and a positive integer $\mathtt{k}(<N/2)$ as input, and returns a vector $\mathtt{ynew}$. Given that $\mathtt{y}$ represents a sound signal that is $T$ seconds long, describe $\mathtt{ynew}$.

```
function ynew = mystery(y,k)
  N = numel(y); % number of elements in y.
  z = fft(y);
  znew = zeros(N,1);
  for i = 1:k
    znew(i) = z(i);
  end
  znew(N:-1:floor(N/2)+2) = conj(znew(2:ceil(N/2)));
  % ensures that ynew is real
  ynew = ifft(znew);
end
```

*Kjeldevarsel: Eksamen-PDF-en for dette vårsettet blei aldri publisert; oppgåveteksten er difor ordrett avtrykk frå løysingsfila `v14-english.pdf` («Matematikk 4M and 4N - Solutions»), som gjentek kvar oppgåve før fasiten. Løysingsvedtaket i same fil er den kjende sensur-LF-en.*

Kildesett: course=TMA4123 term=var year=2014 problem=8 file=v14-english.pdf
