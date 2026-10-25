### **Oppgave 6**

To metodar for å rekne ut ei løysing til likninga

$$x^4-2x-1=0\tag{$*$}$$

er implementert som følgjer i Python. Vi kan anta som kjent at likninga har ei løysing i intervallet $[1,2]$.

```python
def metodeEin(N):
    x = 1.39

    def g(x):
        return 0.5*(x**4 - 1)        # x**4 betyr x^4

    for n in range(0, N):            # 0 <= n <= N-1
        x = g(x)
    return x

def metodeTo(N):
    x = 1.39

    def g(x):
        return (1 + 2*x)**0.25       # (...)**0.25 betyr (...)^0.25

    for n in range(0, N):            # 0 <= n <= N-1
        x = g(x)
    return x
```

Kva for ein av dei to metodane kan vi garantere at konvergerer mot løysinga? Grunngi svaret.

Bruk den metoden du meiner konvergerer mot svaret og rekn ut løysinga til ($*$) (til fem signifikante siffer) der du bruker same startverdi som i koden.

Kildesett: course=TMA4135 term=kont year=2013 problem=6 file=tma4135_13k.pdf
