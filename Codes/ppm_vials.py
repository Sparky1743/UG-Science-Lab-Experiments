import numpy as np
import pandas as pd

# Constants
e_constant = 72646.0410
molar_mass = 319.85  # g/mol

# Original absorbance data from the table
absorbance_data = {
    "Time (minutes)": [0, 10, 20, 30, 40, 50],
    "Vial 1": [0.4185, 0.3173, 0.2798, 0.2549, 0.2411, 0.2284],
    "Vial 2": [0.4185, 0.1994, 0.1848, 0.1799, 0.1913, 0.1922],
    "Vial 3": [0.4185, 0.3696, 0.3563, 0.3589, 0.3526, 0.3495]
}

# Convert the data into a DataFrame for easier processing
df = pd.DataFrame(absorbance_data)

# Calculate molarity (M) by dividing absorbance by e_constant
for vial in ["Vial 1", "Vial 2", "Vial 3"]:
    df[f"{vial} Molarity (M)"] = df[vial] / e_constant

# Convert molarity to ppm using Molarity (M) * Molar Mass * 1000
for vial in ["Vial 1", "Vial 2", "Vial 3"]:
    df[f"{vial} Concentration (ppm)"] = df[f"{vial} Molarity (M)"] * molar_mass * 1000

# Save the results to a text file
output_filename = "molarity_concentration_results.txt"
with open(output_filename, 'w') as file:
    file.write("Molarity and Concentration (ppm) data:\n\n")
    file.write(df.to_string(index=False))  # Write DataFrame to file as plain text

print(f"Results saved to {output_filename}")
