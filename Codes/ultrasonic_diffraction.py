import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# Data for micro-meter readings and current
micrometer_reading = [22.6, 22.55, 22.5, 22.45, 22.4, 22.35, 22.3, 22.25, 22.2, 22.15, 22.1, 22.05, 22, 21.95, 
                      21.9, 21.85, 21.8, 21.75, 21.7, 21.65, 21.6, 21.55, 21.5, 21.45, 21.4, 21.35, 21.3, 21.25, 
                      21.2, 21.15, 21.1, 21.05, 21, 20.95, 20.9, 20.85, 20.8, 20.75, 20.7, 20.65, 20.6, 20.55, 
                      20.5, 20.45, 20.4, 20.35, 20.3, 20.25, 20.2, 20.15, 20.1, 20.05, 20, 19.95, 19.9, 19.85, 
                      19.8, 19.75, 19.7, 19.65, 19.6, 19.55, 19.5, 19.45, 19.4, 19.35, 19.3, 19.25, 19.2, 19.15, 
                      19.1, 19.05, 19, 18.95, 18.9, 18.85, 18.8, 18.75, 18.7, 18.65, 18.6, 18.55, 18.5, 18.45, 
                      18.4, 18.35, 18.3, 18.25, 18.2, 18.15, 18.1, 18.05, 18, 17.95, 17.9, 17.85, 17.8, 17.75, 
                      17.7, 17.65, 17.6, 17.55, 17.5, 17.45, 17.4, 17.35, 17.3, 17.25, 17.2, 17.15, 17.1, 17.05, 
                      17, 16.95, 16.9, 16.85, 16.8, 16.75, 16.7, 16.65, 16.6, 16.55, 16.5, 16.45, 16.4, 16.35, 
                      16.3, 16.25, 16.2, 16.15, 16.1, 16.05, 16, 15.95, 15.9, 15.85, 15.8, 15.75, 15.7, 15.65, 
                      15.6, 15.55, 15.5, 15.45, 15.4, 15.35, 15.3, 15.25, 15.2, 15.15, 15.1, 15.05, 15, 14.95, 
                      14.9, 14.85, 14.8, 14.75, 14.7, 14.65, 14.6, 14.55, 14.5, 14.45, 14.4, 14.35, 14.3, 14.25, 
                      14.2, 14.15, 14.1, 14.05, 14, 13.95, 13.9, 13.85, 13.8, 13.75, 13.7, 13.65, 13.6, 13.55, 
                      13.5, 13.45, 13.4, 13.35, 13.3, 13.25, 13.2, 13.15, 13.1, 13.05, 13, 12.95, 12.9, 12.85, 
                      12.8, 12.75, 12.7, 12.65, 12.6, 12.55, 12.5, 12.45, 12.4, 12.35, 12.3, 12.25, 12.2, 12.15, 
                      12.1, 12.05, 12, 11.95, 11.9, 11.85, 11.8, 11.75, 11.7, 11.65, 11.6, 11.55, 11.5, 11.45, 11.4]


current = [6, 6.5, 6.7, 7.5, 7.8, 8, 9.5, 11.2, 14.1, 17, 18.1, 18.5, 21.3, 22, 22.4, 23.3, 24.7, 22.6, 20, 18.9, 
           17.9, 18.3, 18.9, 18.19, 20.1, 21.2, 23.4, 25.2, 26.3, 31.3, 35.5, 41.7, 50.6, 56.2, 66.6, 72.6, 82.5, 
           97.5, 120.4, 134.7, 150.3, 177.2, 20, 30, 30, 30, 40, 30, 30, 30, 40, 40, 40, 40, 40, 30, 30, 30, 40, 40, 
           40, 40, 40, 40, 40, 40, 40, 40, 50, 50, 60, 70, 110, 190, 240, 310, 390, 510, 640, 730, 830, 910, 980, 
           1020, 1040, 970, 890, 720, 740, 670, 560, 520, 480, 420, 380, 350, 330, 300, 290, 290, 260, 260, 330, 
           450, 550, 670, 810, 1070, 1450, 1800, 2160, 2710, 3220, 3480, 3660, 3760, 3860, 3910, 3920, 3920, 3920, 
           3880, 3860, 3830, 3780, 3690, 3590, 3510, 3480, 3380, 3250, 3020, 2780, 2590, 2320, 2270, 1690, 1350, 
           1060, 750, 560, 480, 400, 330, 300, 310, 340, 370, 420, 460, 530, 610, 760, 860, 940, 980, 990, 860, 
           820, 800, 740, 710, 690, 610, 600, 580, 540, 490, 440, 390, 350, 300, 220, 180, 150, 100, 60, 40, 40, 
           30, 40, 20, 20, 20, 10, 20, 20, 10, 20, 20, 40, 40, 40, 40, 40, 40, 40, 20, 20, 20, 20, 10, 10, 10, 
           154.1, 134.5, 115.9, 92.5, 82.2, 76.4, 68, 50.5, 37.5, 28.5, 25.2, 22.2, 19.8, 17.2, 16, 15.8, 19, 
           18.9, 17.3, 15.5, 16.3]


micrometer_reading = micrometer_reading[20:]
current = current[20:]

# Find the indices of the peaks in the current data
peaks, _ = find_peaks(current)

# Define the peaks to exclude based on micrometer_reading and current values
excluded_peaks = [
    (11.6, 19), (13.6, 40), (13.35, 20), (12.95, 40), 
    (18.2, 740), (20.3, 40), (20, 40), (21.8, 24.7), (21.5, 18.9)
]

# Filter out excluded peaks
filtered_peaks = [peak for peak in peaks if (micrometer_reading[peak], current[peak]) not in excluded_peaks]

# Plot the current vs micrometer reading
plt.figure(figsize=(10, 6))
plt.plot(micrometer_reading, current, label='Values')
plt.plot([micrometer_reading[peak] for peak in filtered_peaks], 
         [current[peak] for peak in filtered_peaks], 'ro', label='Selected Peaks')

# Highlight the x-values of the filtered peaks
for peak in filtered_peaks:
    plt.text(micrometer_reading[peak], current[peak], 
             f'{micrometer_reading[peak]:.2f}', 
             fontsize=9, ha='right', color='red')

# Set plot labels and title
plt.xlabel('Micrometer Reading (mm)')
plt.ylabel('Current (mA)')
plt.title('Current vs Micrometer Reading with Filtered Peaks')
plt.legend()
plt.grid(True)
plt.show()

# Print the x (micrometer reading) and y (current) values of the filtered peaks
for peak in filtered_peaks:
    print(f"Peak at micrometer reading {micrometer_reading[peak]} mm with current {current[peak]} mA")
