### **Løsning til Oppgave 3**

Riktig svar er **Col $A$**.

Vektorene i kolonnerommet Col $A$ er alltid ortogonale til $\mathbf{w}$, fordi det er slik vi velger $\hat{\mathbf{x}}$.

Mer presist: Siden kolonnene i $A$ er lineært uavhengige, er matrisen $A^TA$ inverterbar. Vektoren $\hat{\mathbf{x}}$ er dermed den unike løsningen til

$$A^T(A\hat{\mathbf{x}}-\mathbf{b})=\mathbf{0}.$$

Dette betyr at $\mathbf{w}=A\hat{\mathbf{x}}-\mathbf{b}$ (opp til fortegn) er i Null $A^T$. Alle vektorer som er ortogonale til Null $A^T$, er dermed også ortogonale til $\mathbf{w}$. Med andre ord har vi alltid

$$\operatorname{Col} A = (\operatorname{Null} A^T)^{\perp} \subseteq (\operatorname{Span}\{\mathbf{w}\})^{\perp}.$$

Siden $\dim\operatorname{Col} A=2$ og $\dim\operatorname{Span}\{\mathbf{w}\}=1$, har vi $\operatorname{Col} A=(\operatorname{Span}\{\mathbf{w}\})^{\perp}$.

*Kjeldevarsel: kjelda er eksamensarket med løysingsforslag innline; påstandane $\operatorname{Col}A=(\operatorname{Null}A^T)^{\perp}$, $A^T\mathbf{w}=\mathbf{0}$ og $\operatorname{Null}A^T=\operatorname{Span}\{\mathbf{w}\}$ er kontrollerte med sympy på eit dømesme.*

Kildesett: course=TMA4110 term=host year=2020 problem=3 file=TMA4110_h2020.pdf
