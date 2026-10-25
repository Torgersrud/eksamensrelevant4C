### **Problem 7** **Discrete Fourier Transform, 4D,[10 pts]**

The spectrum of a certain signal $f$, sampled at regular time intervals, is shown below (as usual, the "mirrored" half of the spectrum is omitted from the plot):

[Plot: vertical axis $2|\hat{f}_k|/N$ from 0 to 10, horizontal axis "Frequency [Hz]" from 0 to 50 with ticks every 2. The spectrum is zero except for four spikes: height 4 at 2 Hz, height 8 at 6 Hz, height 10 at 30 Hz and height 2 at 40 Hz.]

The following Python code computes that spectrum using the `fft` function, then applies a certain type of filter to the original signal:

```
import numpy as np

N = f.size #(the signal f was pre-computed elsewhere)
dt = 0.001 #spacing between two samples, in seconds
L = N*dt #length of the sampling interval, in seconds

n = np.arange(N) #vector of indices n = 0,1,...,N-1
nShifted = N/2-np.abs(n-N/2) #vector of shifted indices
shiftedFreq=nShifted/L #shift frequencies to account for mirroring

cutoffFreq = 25 #in Hertz
DFT = np.fft.fft(f)
DFT[shiftedFreq < cutoffFreq] = 0
g = np.fft.ifft(DFT)
```

a) What kind of filter is implemented above?

b) Among the functions below, which one could best represent the *filtered* signal?

$$\begin{array}{ll}\mathrm{i)}&g(t)=4\cos(4\pi t)+8\sin(12\pi t)\\ \mathrm{ii)}&g(t)=\cos(4\pi t)+\sin(12\pi t)\\ \mathrm{iii)}&g(t)=\cos(60\pi t)+\sin(80\pi t)\\ \mathrm{iv)}&g(t)=10\cos(60\pi t)+2\sin(80\pi t)\end{array}$$

**Remember:** if $t$ is measured in seconds, and $\alpha>0$, then the frequency (in Hertz) of a function such as $\cos(2\pi\alpha t)$ or $\sin(2\pi\alpha t)$ is simply $\alpha$.

Kildesett: course=TMA4135 term=host year=2023 problem=7 points=10 file=tma4130_2023h_exam.pdf
