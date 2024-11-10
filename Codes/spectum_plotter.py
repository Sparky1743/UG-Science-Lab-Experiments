import os
import glob
import matplotlib.pyplot as plt

folder_path = r"C:\Users\birud\Downloads\Group5-20241110T121813Z-001\Group5"
file_pattern = os.path.join(folder_path, "G5_V3_T*_Absorbance_*.txt")

peak_data = {}

plt.figure(figsize=(10, 6))

for file_path in glob.glob(file_pattern):
    wavelengths = []
    absorbance = []

    with open(file_path, "r") as file:
        data_started = False
        for line in file:
            if ">>>>>Begin Spectral Data<<<<<" in line:
                data_started = True
                continue
            if not data_started:
                continue
            try:
                wl, ab = map(float, line.split())
                wavelengths.append(wl)
                absorbance.append(ab)
            except ValueError:
                continue

    filtered_wavelengths = []
    filtered_absorbance = []

    for wl, ab in zip(wavelengths, absorbance):
        if 450 <= wl <= 900:
            filtered_wavelengths.append(wl)
            filtered_absorbance.append(ab)

    if filtered_absorbance:
        max_absorbance = max(filtered_absorbance)
        peak_wavelength = filtered_wavelengths[filtered_absorbance.index(max_absorbance)]
        file_name = os.path.basename(file_path)
        sample_label = file_name.split("_")[1] + "_" + file_name.split("_")[2] # Extract T1, T2, etc. from the file name
        peak_data[sample_label] = (peak_wavelength, max_absorbance)
        print(f"{sample_label} - Peak Absorbance: {max_absorbance} at Wavelength: {peak_wavelength} nm")

        plt.plot(filtered_wavelengths, filtered_absorbance, label=f"{sample_label}_absorbance")

plt.xlabel("Wavelength (nm)")
plt.ylabel("Absorbance")
plt.title("Absorbance Spectrum")
plt.legend()
plt.grid(True)
plt.show()

print("\nSummary of Peak Absorbances:")
for sample, (peak_wl, peak_abs) in peak_data.items():
    print(f"{sample}: Peak Absorbance = {peak_abs} at Wavelength = {peak_wl} nm")
