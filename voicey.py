#from pydub import AudioSegment
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import wave
from scipy import fftpack
from scipy.signal import butter, lfilter
from scipy.signal import freqz
t=[]
x=[]
shape=[]
samplerate_list=[]
freq_signals=[]
modulated_signal=[]
modulating_signal=[]
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
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
    frequency=1/T
    t.append(np.linspace(0.,T,data.shape[0]))
    x.append(data)
    shape.append(data.shape[0])
    samplerate_list.append(samplerate)

read_signal("output2.wav")
read_signal("output3.wav")
read_signal("output4.wav")
min_shape=min(shape)

for i in range(0,3):
    x[i]=x[i][0:min_shape]
    t[i]=t[i][0:min_shape]


# plt.plot(t[0],x[0])
# plt.show()
# plt.plot(t[0],x[1])
# plt.show()
# plt.plot(t[0],x[2])
# plt.show()
modulating_signal.append(np.cos(2 * np.pi * 5000 * t[0]))
modulating_signal.append(np.cos(2 * np.pi * 20000 * t[0]))
modulating_signal.append(np.sin(2 * np.pi * 20000 * t[0]))
for i in range(0,3):
    modulated_signal.append(np.multiply(x[i],modulating_signal[i]))

freq = fftpack.fftfreq(min_shape) * samplerate_list[0]
for i in range(0,3):
    freq_signals.append(fftpack.fft(modulated_signal[i]))

plt.plot(freq, freq_signals[0].real,freq, freq_signals[1].real,freq, freq_signals[2].real)
plt.show()








# freq_signal=fftpack.fft(modulated_signal)
# freq = fftpack.fftfreq(modulated_signal.shape[0]) * samplerate

# plt.plot(freq, freq_signal.real)
# plt.show()


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

