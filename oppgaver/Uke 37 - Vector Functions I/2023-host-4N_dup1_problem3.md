### **Problem 3** **Numerics for Nonlinear Equations [10 pts]**

Consider the initial value problem

$$y'(t)=\cos(2ty)\,,\quad y(0)=0\,.$$

Using a certain Runge–Kutta method with time-step size $h=0.5$, the numerical approximation of $y(t)$ at time $t_{n+1}=(n+1)h$ will be

$$y_{n+1}=y_n+0.5\cos[(n+1)y_{n+1}]\,.$$

a) Which Runge–Kutta method is being used above?

b) To compute the first time step, we have to solve a nonlinear equation:

$$y_1=0.5\cos y_1\,.$$

Renaming $y_1$ as $x$, the nonlinear equation can be written as

$$2x-\cos x=0\,.\tag{6}$$

Using Newton's method to solve Eq. (6) numerically, with initial guess $x_0=0$, iterate until the absolute difference between two consecutive iterations is less than $0.001$ (in other words, iterate until $|x_{k+1}-x_k|<10^{-3}$).

Kildesett: course=TMA4135 term=host year=2023 problem=3 points=10 file=tma4130_2023h_exam.pdf
