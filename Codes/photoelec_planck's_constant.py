import matplotlib.pyplot as plt
import numpy as np

colors = ["red", "orange", "yellow", "green", "blue"]
freq = np.array([4.48, 5.08, 5.31, 5.77, 6.25]) * 10**14
stp = np.array([0.32, 0.53, 0.71, 0.83, 1.03]) * -1

coefficients = np.polyfit(freq, stp, 1)
linear_fit = np.poly1d(coefficients)

slope = coefficients[0]
intercept = coefficients[1]
print(f"The slope of the linear fit is: {slope}")
print(f"The intercept of the linear fit is: {intercept}")

fit_line = linear_fit(freq)

plt.plot(freq, stp, 'o', label='Data Points', color='green')  # Changed color of points to green
plt.plot(freq, fit_line, label='Least Squares Fit', color='purple')  # Changed color of fit line to purple

plt.xlabel('Frequency (Hz)')
plt.ylabel('Stopping Potential (V)')
plt.title('Least Squares Fit of Frequency vs Stopping Potential')
plt.legend()
plt.show()
