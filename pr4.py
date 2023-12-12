import json
import numpy as np

from scipy import signal
from scipy.fft import fft, fftfreq

import matplotlib.pyplot as plt


f = open("./1500rpm_misalignment-2.json")
data = json.load(f)

# duration = 5  # seconds



sample_rate = 2000
# sample_rate = data["sample_rate"]

f0 =100  # Hz
# amplitude1 = 10


# N = int(data["number_of_samples"] ) # pobieramy ilość próbek z pliku
N = int(10* sample_rate/ f0)
tstep = 1.0 / sample_rate


# y1 = data["vibrationsZ"]  # 8192

# y1 = y1 - np.mean(y1)

t = np.linspace(0,(N-1)*tstep ,N) #time steps 
fstep = sample_rate/N

f= np.linspace(0,(N-1)*fstep ,N) # freq steps


sig = 1 * np.sin(2*np.pi * f0 * t) + 5 * np.sin(2*np.pi* 5* f0 * t)
# sig = 1 * np.sin(2*np.pi * f0 * t)


# xf = fftfreq(N, T)[: N // 2]
# yf1 = abs(fft(y1)) / N


# https://www.youtube.com/watch?v=O0Y8FChBaFU


# plt.specgram(y1, Fs=sample_rate, cmap='viridis', NFFT=1024, noverlap=512)
# plt.xlabel('Time (s)')




#preforming fft

X= np.fft.fft(sig)
#magnitude of x

X_mag = np.abs(X) /N


f_plot = f[0:int(N/2+1)]


x_mag_plot = 2*X_mag[0:int(N/2+1)]

x_mag_plot[0]=x_mag_plot[0]/2#DC componenet to multiply by 2




fig ,[ax1,ax2,ax3] = plt.subplots(nrows=3,ncols=1)
ax1.plot(t,sig)
ax2.plot(f_plot,x_mag_plot)

# spectrogram = librosa.feature.melspectrogram(y=f_plot, sr=1024)
# librosa.display.specshow(librosa.power_to_db(spectrogram, ref=np.max), y_axis='mel', x_axis='time')
ax3.specgram(sig, NFFT=sample_rate, Fs=N*10, cmap="rainbow")
#x feeq y magnitude
plt.show()