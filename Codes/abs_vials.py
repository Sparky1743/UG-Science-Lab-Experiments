import matplotlib.pyplot as plt

time_minutes = [0, 10, 20, 30, 40, 50]

peak_absorbances = [0.4185, 0.3696, 0.3563, 0.3589, 0.3526, 0.3495]

plt.figure(figsize=(8, 6))
plt.plot(time_minutes, peak_absorbances, marker='o', color='r', label="Vial3 Peak Absorbance")
plt.xlabel("Time (minutes)")
plt.ylabel("Vial3 Peak Absorbance")
plt.title("Vial3 Peak Absorbance vs Time")
plt.grid(True)
plt.legend()
plt.show()
