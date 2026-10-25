### **Oppgave 7**

I denne oppgåva ser vi på den partielle differensiallikninga

$$\frac{\partial u}{\partial t}=\frac{\partial^2u}{\partial x^2},\quad-\infty<x<\infty,\quad t>0,$$

krava

$$\lim_{x\to\pm\infty}u(x,t)=\lim_{x\to\pm\infty}u_x(x,t)=0,$$

og startvilkåret

$$u_t(x,0)=f(x).$$

Funksjonen $f$ er gitt ved

$$f(x)=g''(x),$$

der $g$ er ein to gonger derivierbar funksjon, og vi antar at dei fouriertransformerte til $f$ og $g$ eksisterer.

**a)** Vis at den partielle differensiallikninga gitt over kan skrivast, ved å anvende fouriertransformasjon, som initialverdiproblemet

$$\frac{\partial\hat{u}}{\partial t}=-\omega^2\hat{u},\quad\hat{u}_t(\omega,0)=\hat{f}(\omega).\tag{$*$}$$

**b)** Ved å fikser $\omega$ så kan vi skrive ($*$) som den ordinære differensiallikninga

$$\frac{\mathrm{d}\hat{u}}{\mathrm{d}t}=-\omega^2\hat{u},\quad\hat{u}_t(\omega,0)=\hat{f}(\omega),\tag{$**$}$$

Vis at ($**$) har løysing

$$\hat{u}(\omega,t)=\hat{g}(\omega)e^{-\omega^2t}.$$

**c)** Vis at løysinga til problemet kan skrivast på forma

$$u(x,t)=\int_{-\infty}^{\infty}g(x-p)h(p,t)\,\mathrm{d}p\quad\text{for}\quad t>0,$$

og finn $h(p,t)$.

Kildesett: course=TMA4135 term=kont year=2013 problem=7 file=tma4135_13k.pdf
