import pandas as pd
import matplotlib.pyplot as plt
from signal_processing import bandpass_filter, frequency_spectrum

FS = 100
data = pd.read_csv("data/synthetic_accelerometer.csv")
sample = data[data["sample_id"] == 0]["accel_x"].to_numpy()

filtered = bandpass_filter(sample, FS)
freqs, spectrum = frequency_spectrum(filtered, FS)

plt.figure(figsize=(8, 4))
plt.plot(filtered)
plt.xlabel("Sample")
plt.ylabel("Acceleration")
plt.title("Filtered Wearable Accelerometer Signal")
plt.tight_layout()
plt.savefig("results/tremor_signal.png", dpi=160)
plt.close()

plt.figure(figsize=(8, 4))
plt.plot(freqs, spectrum)
plt.xlim(0, 12)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Frequency Spectrum")
plt.tight_layout()
plt.savefig("results/frequency_spectrum.png", dpi=160)
plt.close()

print("Saved signal plots.")
