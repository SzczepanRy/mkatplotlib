import json
import numpy as np

from scipy import signal
from scipy.fft import fft, fftfreq
from scipy.signal import hilbert, chirp
import matplotlib.pyplot as plt



def envelope(signal):
    analytic_signal = hilbert(signal)
    amplitude_envelope = np.abs(analytic_signal)
    amplitude_envelope = amplitude_envelope.tolist()
    return amplitude_envelope


f = open("./1500rpm_misalignment-2.json")
data = json.load(f)
sample_rate = data["sample_rate"]
N = data["number_of_samples"]  # pobieramy ilość próbek z pliku
T = 1.0 / sample_rate

#  -------------- MOZLIWOSC ZMIANY CZYTANEJ OSI --------------
y1 = data["vibrationsZ"]
y1 = y1 - np.mean(y1)

xf = fftfreq(N, T)[: N // 2]
yfx = abs(fft(y1)) / N

yf1 = envelope(yfx)

main_x_list = xf.tolist()
main_y_list = yf1[0:int(len(yf1)/2)]
fig ,[ax1,ax2] = plt.subplots(nrows=2,ncols=1)

ax1.plot(main_x_list,main_y_list)
f, t, Sxx = ax2.specgram(y1, NFFT=sample_rate, Fs=N/20)
plt.show()