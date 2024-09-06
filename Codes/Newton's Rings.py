import numpy as np
import matplotlib.pyplot as plt

least_count = 0.01  # mm

left_values_mm1 = 13 + np.array([31, 27, 24, 18, 11, 4]) * least_count
left_values_mm2 = 12 + np.array([98, 91, 85, 77, 69, 60, 51, 43, 33, 22, 10]) * least_count
left_values_mm3 = 11 + np.array([96, 82, 66, 46]) * least_count

left_values_mm = np.concatenate((left_values_mm1, left_values_mm2, left_values_mm3))

right_values_mm1 = 7 + np.array([79, 85, 92, 97]) * least_count
right_values_mm2 = 8 + np.array([4, 10, 17, 25, 31, 39, 46, 55, 64, 72, 83, 93]) * least_count
right_values_mm3 = 9 + np.array([3, 16, 31, 48, 73]) * least_count

right_values_mm = np.concatenate((right_values_mm1, right_values_mm2, right_values_mm3))

# Remove the first value from both lists
right_values_mm = right_values_mm[1:] + 0.20
left_values_mm = left_values_mm[1:] - 0.20

print(list(right_values_mm[::-1]))
print(list(left_values_mm[::-1]))

diameters_mm = left_values_mm - right_values_mm

lambda_ = 5893e-7
m = 1

n_values = np.arange(1, len(diameters_mm) + 1)
n_values = n_values[::-1]
D_n_squared_diff = diameters_mm**2

slope, intercept = np.polyfit(n_values, D_n_squared_diff, 1)

R_mm = slope / (4 * lambda_)

plt.figure(figsize=(8, 6))
plt.plot(n_values, D_n_squared_diff, 'bo', label=r'Data Points')
plt.plot(n_values, slope * n_values + intercept, 'r', label=f'Fit: $y = {slope:.4f}n + {intercept:.4f}$')
plt.xlabel('Ring number m')
plt.ylabel(r'Diameter Squared (mm$^2$)')
plt.title(r'Plot of $D_n^2 - D_m^2$ versus Fringe number $n$')
plt.legend()
plt.grid(True)
plt.show()

print(f"Slope (A): {slope:.4f} mm^2 per fringe")
print(f"Intercept (B): {intercept:.4f} mm^2")
print(f"Radius of Curvature (R): {R_mm:.4f} mm")
