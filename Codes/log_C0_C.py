import numpy as np
import pandas as pd

concentration_data = {
    "Time (minutes)": [0, 10, 20, 30, 40, 50],
    "Vial 1 (ppm)": [1.842595, 1.397026, 1.231919, 1.122288, 1.061528, 1.005612],
    "Vial 2 (ppm)": [1.842595, 0.877929, 0.813648, 0.792074, 0.842266, 0.846229],
    "Vial 3 (ppm)": [1.842595, 1.627295, 1.568737, 1.580185, 1.552447, 1.538798]
}

df = pd.DataFrame(concentration_data)

for vial in ["Vial 1 (ppm)", "Vial 2 (ppm)", "Vial 3 (ppm)"]:
    # Set C0 for each vial
    C0 = df[vial][0]
    # Calculate ln(C0 / C) for each row
    df[f"ln(C0/C) {vial}"] = np.log(C0 / df[vial])

output_filename = "ln_C0_over_C_results.txt"
with open(output_filename, 'w') as file:
    file.write("ln(C0 / C) values for each vial over time:\n\n")
    file.write(df.to_string(index=False))  # Write DataFrame to file as plain text

print(f"Results saved to {output_filename}")
