import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# Correct 'current' array syntax with elements separated by commas
current = np.array([-24*10**-4, -100*10**-4, -5*10**-4, -2*10**-4, -1*10**-4, 189*10**-4, 1511*10**-4, 0.44, 0.85, 1.16, 1.46, 1.66, 
                    1.80, 1.93, 2.02, 2.05, 1.99, 1.83, 1.58, 1.37, 1.33, 1.49, 1.80, 
                    2.21, 2.44, 2.72, 2.85, 2.81, 2.54, 2.05, 1.50, 1.15, 1.25, 1.69, 
                    2.27, 2.92, 3.36, 3.61, 3.67, 3.48, 2.98, 2.24, 1.52, 1.17, 1.48, 
                    2.12, 2.97, 3.67, 4.12, 4.40, 4.42, 4.17, 3.71, 2.80, 1.98, 1.61, 
                    1.85, 2.61, 3.43, 4.16, 4.73, 5.08, 5.18, 4.99, 4.44, 3.73, 2.95, 
                    2.46, 2.46, 2.90, 3.77, 4.42, 5.08, 5.59, 5.85, 5.86, 5.61, 5.04, 
                    4.32])

current = current * 10 ** -7

# Adjust 'voltage' array to match the length of 'current' (79 elements)
voltage = np.arange(1, 80)  # Generates numbers from 1 to 79

# Find peaks in the current array
peaks, _ = find_peaks(current)

# Plotting the graph
plt.plot(voltage, current, label='Current vs Voltage')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('Voltage vs. Current')
plt.grid(True)

# Mark the peaks
plt.scatter(voltage[peaks], current[peaks], color='red', marker='o', label='Peaks')

# Annotate peaks with their x-axis values
for peak in peaks:
    plt.annotate(f'{voltage[peak]} V', (voltage[peak], current[peak]),
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.legend()
plt.show()
