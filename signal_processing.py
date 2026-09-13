import numpy as np
from scipy.signal import butter, filtfilt

def bandpass_filter(signal, fs, low=0.5, high=12.0, order=4):
    nyquist = fs / 2
    b, a = butter(order, [low / nyquist, high / nyquist], btype="band")
    return filtfilt(b, a, signal)

def frequency_spectrum(signal, fs):
    freqs = np.fft.rfftfreq(len(signal), 1 / fs)
    spectrum = np.abs(np.fft.rfft(signal))
    return freqs, spectrum
