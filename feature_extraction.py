import numpy as np
from scipy.signal import welch

def extract_features(signal, fs):
    signal = np.asarray(signal)
    freqs, psd = welch(signal, fs=fs, nperseg=min(256, len(signal)))

    dominant_frequency = float(freqs[np.argmax(psd)])
    band = (freqs >= 4) & (freqs <= 6)
    band_power = float(np.trapz(psd[band], freqs[band])) if np.any(band) else 0.0

    power = psd / (psd.sum() + 1e-12)
    spectral_entropy = float(-(power * np.log2(power + 1e-12)).sum())

    return {
        "rms": float(np.sqrt(np.mean(signal ** 2))),
        "std": float(np.std(signal)),
        "variance": float(np.var(signal)),
        "energy": float(np.sum(signal ** 2)),
        "dominant_frequency_hz": dominant_frequency,
        "band_power_4_6hz": band_power,
        "spectral_entropy": spectral_entropy,
    }
