import matplotlib.pyplot as plt

# Data for NaCl solution
time_nacl = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
volume_nacl = [0.0, 0.8, 1.6, 2.3, 3.0, 3.6, 4.3, 5.0, 5.7, 6.4, 7.1]

# Data for MgCl2 solution
time_mgcl2 = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
volume_mgcl2 = [0.0, 1.2, 2.4, 3.9, 5.1, 6.2, 7.4, 8.4, 10.2, 11.4, 13.4]

plt.figure(figsize=(10, 6))
plt.plot(time_nacl, volume_nacl, marker='o', linestyle='-', color='blue', label='NaCl Solution')
plt.plot(time_mgcl2, volume_mgcl2, marker='s', linestyle='-', color='green', label='MgCl$_2$ Solution')

plt.title("Volume of Hydrogen Gas Produced in NaCl vs MgCl$_2$")
plt.xlabel("Time (minutes)")
plt.ylabel("Volume of Hydrogen Gas (ml)")
plt.legend(loc="upper left")
plt.grid(True)

plt.tight_layout()
plt.savefig("hydrogen_gas_production.png")  # Saves the plot as a PNG file
plt.show()
