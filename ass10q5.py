import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x - 2 

def bisection_method(a, b, tol=1e-5):
    if f(a) * f(b) > 0:
        print("Invalid interval")
        return None

    iterations = []
    
    while abs(b - a) > tol:
        mid = (a + b) / 2
        iterations.append(mid)

        if f(mid) == 0:
            break
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid

    return np.array(iterations)

a, b = -3, 3
roots = bisection_method(a, b)


x_vals = np.linspace(-3, 3, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x)")
plt.axhline(0, color='black', linestyle='--')
plt.scatter(roots, [0] * len(roots), color='red', label="Bisection Steps")
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Bisection Method Root Finding")
plt.show()
