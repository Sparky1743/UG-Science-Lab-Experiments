import matplotlib.pyplot as plt
import numpy as np

volumes_of_mb = [2, 1, 1, 1, 1]  # Volume of MB for TT1 to TT5
volumes_of_water = [0, 1, 2, 3, 4]  # Volume of water for TT1 to TT5

initial_concentration_ppm = 5

molecular_weight = 319.85

def calculate_molarity(volume_mb, volume_water, initial_concentration):
    total_volume = volume_mb + volume_water
    final_concentration_ppm = (volume_mb * initial_concentration) / total_volume
    molarity = (final_concentration_ppm * 0.001) / molecular_weight
    return molarity

concentrations = [calculate_molarity(vol_mb, vol_water, initial_concentration_ppm) for vol_mb, vol_water in zip(volumes_of_mb, volumes_of_water)]

print("Concentrations in Molarity (M):")
for i, concentration in enumerate(concentrations, start=1):
    print(f"Test Tube {i}: {concentration:.8e} M")

peak_absorbances = [1.1257, 0.5476, 0.3595, 0.2636, 0.2282]

slope, intercept = np.polyfit(concentrations, peak_absorbances, 1)

fitted_line = np.polyval([slope, intercept], concentrations)

plt.figure(figsize=(8, 6))
plt.plot(concentrations, peak_absorbances, marker='o', linestyle='-', color='b', label='Data')
plt.plot(concentrations, fitted_line, linestyle='--', color='r', label=f'Linear Fit: Slope = {slope:.4f}')

plt.xlabel("Concentration (M)")
plt.ylabel("Peak Absorbance")
plt.title("Peak Absorbance vs Concentration")

plt.grid(True)
plt.legend()
plt.show()

print(f"Slope of the linear fit: {slope:.4f}")
