import numpy as np
from scipy.interpolate import CubicSpline

# Definujeme body
x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 0, 0])

# Vytvoříme spline
cs = CubicSpline(x, y, bc_type='natural')

# Vytiskneme koeficienty spline
for i in range(len(x)-1):
    print(f"Spline na intervalu [{x[i]}, {x[i+1]}]:")
    print(f"{cs.c[:,i][0]}*(x-{x[i]})^3 + {cs.c[:,i][1]}*(x-{x[i]})^2 + {cs.c[:,i][2]}*(x-{x[i]}) + {cs.c[:,i][3]}")

print(cs.c)
print("Hodnoty spline v bodech x:")
print(cs(x))