

import numpy as np
import matplotlib.pyplot as plt

# Create two sine waves with different amplitudes
duration = 5  # seconds
sample_rate = 44100  # Hz
frequency1 =1000  # Hz
amplitude1 = 10

frequency2 = 500  # Hz
amplitude2 = 5

t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
signal1 = amplitude1 * np.sin(2 * np.pi * frequency1 * t)
signal2 = amplitude2 * np.sin(2 * np.pi * frequency2 * t)

# Combine the two signals
combined_signal = signal1 + signal2

# Create a spectrogram
plt.specgram(combined_signal, Fs=sample_rate, cmap='viridis', NFFT=1024, noverlap=512)
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')

plt.show()