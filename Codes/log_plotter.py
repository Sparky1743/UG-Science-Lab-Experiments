import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Data
time = np.array([0, 10, 20, 30, 40, 50])
ln_c0_c_vial1 = np.array([0.0000, 0.2768, 0.4026, 0.4958, 0.5514, 0.6055])
ln_c0_c_vial2 = np.array([0.0000, 0.7413, 0.8174, 0.8442, 0.7828, 0.7781])
ln_c0_c_vial3 = np.array([0.0000, 0.1242, 0.1609, 0.1536, 0.1713, 0.1801])

# Linear fit for each vial
slope1, intercept1, _, _, _ = linregress(time, ln_c0_c_vial1)
slope2, intercept2, _, _, _ = linregress(time, ln_c0_c_vial2)
slope3, intercept3, _, _, _ = linregress(time, ln_c0_c_vial3)

# Generate linear fit lines
fit_line1 = slope1 * time + intercept1
fit_line2 = slope2 * time + intercept2
fit_line3 = slope3 * time + intercept3

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(time, fit_line1, label=f"Vial 1 Fit (slope={slope1:.4f})", color='blue')
plt.plot(time, fit_line2, label=f"Vial 2 Fit (slope={slope2:.4f})", color='orange')
plt.plot(time, fit_line3, label=f"Vial 3 Fit (slope={slope3:.4f})", color='green')
plt.scatter(time, ln_c0_c_vial1, color='blue', marker='o')  # Data points for Vial 1
plt.scatter(time, ln_c0_c_vial2, color='orange', marker='o') # Data points for Vial 2
plt.scatter(time, ln_c0_c_vial3, color='green', marker='o')  # Data points for Vial 3

plt.xlabel("Time (minutes)")
plt.ylabel("ln(C₀ / C)")
plt.title("ln(C₀ / C) over Time with Linear Fit for Different Vials")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Display plot
plt.show()

# Print slopes
print(f"Slope of Vial 1 Fit Line: {slope1:.4f}")
print(f"Slope of Vial 2 Fit Line: {slope2:.4f}")
print(f"Slope of Vial 3 Fit Line: {slope3:.4f}")
