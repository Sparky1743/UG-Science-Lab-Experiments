import numpy as np
import matplotlib.pyplot as plt

def inverse_sqr(dis):
    return 1 / (dis) ** 2

dis = np.array([40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20])
distance = inverse_sqr(dis)
current = np.array([0.568, 0.618, 0.670, 0.738, 0.819, 0.979, 1.015, 1.146, 1.194, 1.508, 1.830])*10**(-6)

coefficients = np.polyfit(distance, current, 1)
linear_fit = np.poly1d(coefficients)

slope = coefficients[0]
print(f"The slope of the linear fit is: {slope}")

fit_line = linear_fit(distance)

plt.plot(distance, current, 'o', label='Data Points', color='green')  # Changed color of points to green
plt.plot(distance, fit_line, label='Least Squares Fit', color='purple')  # Changed color of fit line to purple

plt.xlabel('Inverse Square of Distance (1/d²) in cm⁻²')
plt.ylabel('Photocurrent (A)')
plt.title('Least Squares Fit of Current vs. (1/Distance^2)')
plt.legend()
plt.show()
