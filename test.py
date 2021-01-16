import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import wave
from scipy import fftpack 
import numpy as np
from scipy.signal import butter, lfilter
from scipy.signal import freqz
t=[]
x=[]
shape=[]
samplerate_list=[]
freq_signals=[]
modulated_signal=[]
modulating_signal=[]
demodulating_signal=[]
def butter_lowpass(lowcut, fs, order):
    nyq = 0.5 * fs
    low = lowcut / nyq
    b, a = butter(order, low, btype='low',analog=False)
    return b, a

#-----------------------------------------------------------------------------------------------------------------------------------
def butter_lowpass_filter(data, lowcut, fs, order=5):
    b, a = butter_lowpass(lowcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def read_signal(path):
    samplerate, un_modulated=wavfile.read(path)
    un_modulated=np.array(un_modulated,dtype=np.int16)
    if(un_modulated.shape[1]==2):
        data=np.array((un_modulated[:,0]+un_modulated[:,1])/2,dtype=np.int16)
    else:
        data=un_modulated
    T=data.shape[0]/samplerate
    t.append(np.linspace(0.,T,data.shape[0]))
    x.append(data)
    shape.append(data.shape[0])
    samplerate_list.append(samplerate)

# lowcut = 500.0
# highcut = 1250.0

# fs = 5000.0
# T = 0.05
# nsamples = int(T * fs)
# t = np.linspace(0, T, nsamples, endpoint=False)
# #Plot the frequency response for a few different orders.
# plt.figure(1)
# plt.clf()
# for order in [3, 6, 12]:
#     b, a = butter_bandpass(lowcut, highcut, fs, order=order)
#     w, h = freqz(b, a, worN=2000)
#     plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)

# plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],
#             '--', label='sqrt(0.5)')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Gain')
# plt.grid(True)
# plt.legend(loc='best')
# plt.show()

# # a = 0.02
# f0 = 600.0
# x = 0.1 * np.sin(2 * np.pi * 1.2 * np.sqrt(t))
# x += 0.01 * np.cos(2 * np.pi * 312 * t + 0.1)
# x += a * np.cos(2 * np.pi * f0 * t + .11)
# x += 0.03 * np.cos(2 * np.pi * 2000 * t)
# plt.figure(2)
# plt.clf()
# plt.plot(t, x, label='Noisy signal')




# y = butter_bandpass_filter(x, lowcut, highcut, fs, order=6)
# plt.plot(t, y, label='Filtered signal (%g Hz)' % f0)
# plt.show()
# freq = fftpack.fftfreq(t.shape[-1])
# x_freq=fftpack.fft(x)
# plt.plot(freq, x_freq.real)
# plt.show()
# y_freq=fftpack.fft(y)
# plt.plot(freq, y_freq.real)
# plt.show()

# plt.plot(t, y, label='Filtered signal (%g Hz)' % f0)
# plt.xlabel('time (seconds)')
# plt.hlines([-a, a], 0, T, linestyles='--')
# plt.grid(True)
# plt.axis('tight')
# plt.legend(loc='upper left')

plt.show()

#-------------------------------
read_signal("output2.wav")
modulating_signal.append(np.cos( (2*np.pi)*(5000)* t[0]) )
modulated_signal.append(np.multiply(x[0],modulating_signal[0]))
freq = fftpack.fftfreq(t[0].shape[-1]) * samplerate_list[0]
freq_signals.append(fftpack.fft(modulated_signal[0]))
x1=modulated_signal[0]
demodulating_signal.append(np.cos( (2*np.pi)*5000* t[0]  ) )
x1=x1*demodulating_signal[0]
x1=butter_lowpass_filter(x1,5000,samplerate_list[0],12)
x1=2*x1
x1=np.array(x1,dtype=np.int16)
wavfile.write("signal1.wav",samplerate_list[0],x1)



