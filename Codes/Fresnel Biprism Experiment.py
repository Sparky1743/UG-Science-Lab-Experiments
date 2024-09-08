import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

fringe_numbers = np.array([1, 5, 9, 13, 17, 21])
fringe_positions = np.array([10.08, 8.87, 7.60, 6.41, 5.11, 3.79])

coefficients = np.polyfit(fringe_numbers, fringe_positions, 1)
slope = coefficients[0]
intercept = coefficients[1]

pair_indices = list(combinations(range(len(fringe_numbers)), 2))
all_fringe_widths = [(fringe_positions[j] - fringe_positions[i]) / (fringe_numbers[j] - fringe_numbers[i]) 
                     for i, j in pair_indices]

all_fringe_widths = np.array(all_fringe_widths)
average_fringe_width = np.mean(all_fringe_widths)
std_deviation = np.std(all_fringe_widths)

print(f"All Fringe Widths: {all_fringe_widths}")
print(f"Average Fringe Width: {average_fringe_width:.4f} mm")
print(f"Standard Deviation: {std_deviation:.4f} mm")
print(f"Slope of the Linear Fit: {slope:.4f} mm")

plt.figure(figsize=(8, 6))
plt.plot(fringe_numbers, fringe_positions, 'o', label='Measured Positions')
plt.plot(fringe_numbers, np.polyval(coefficients, fringe_numbers), '-', label='Fitted Line')
plt.xlabel('Fringe Number')
plt.ylabel('Position (mm)')
plt.title('Fringe Positions vs. Fringe Numbers')
plt.grid(True)
plt.legend()
plt.show()
