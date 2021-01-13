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
def butter_bandpass(lowcut, fs, order):
    nyq = 0.5 * fs
    low = lowcut / nyq
    b, a = butter(order, low, btype='low',analog=False)
    return b, a


def butter_bandpass_filter(data, lowcut, fs, order=5):
    b, a = butter_bandpass(lowcut, fs, order=order)
    y = lfilter(b, a, data)
    return y
def read_signal(path):
    samplerate, un_modulated=wavfile.read(path)
    un_modulated=np.array(un_modulated,dtype=np.int16)
    if(un_modulated.shape[1]==2):
        data=np.array((un_modulated[:,0]+un_modulated[:,1])/2,dtype=np.int16)
    else:
        data=un_modulated
    #sample rate=number of samples(data.shape[0])/overall time of the wave    
    T=data.shape[0]/samplerate
    #frequency=1/T
    #time from 0 to T(10 sec for our inputs) and has data.shape[0] samples(bins)
    t.append(np.linspace(0.,T,data.shape[0]))
    x.append(data)
    shape.append(data.shape[0])
    samplerate_list.append(samplerate)

read_signal("output2.wav")
read_signal("output3.wav")
read_signal("output4.wav")
min_shape=min(shape)
print(shape)
for i in range(0,3):
    x[i]=x[i][0:min_shape]
    t[i]=t[i][0:min_shape]

freq_1 = fftpack.fft(x[0])
freq = fftpack.fftfreq(min_shape) * samplerate_list[0]
#wavfile.write("example.wav",samplerate_list[0],x[0])
plt.plot(t[0],x[0])
plt.show()
# plt.plot(t[0],x[1])
# plt.show()
# plt.plot(t[0],x[2])
# plt.show()
modulating_signal.append(np.cos( 5000 * t[0]))
modulating_signal.append(np.cos( 80000 * t[0]))
modulating_signal.append(np.sin( 80000* t[0]))
for i in range(0,3):
    modulated_signal.append(np.multiply(x[i],modulating_signal[i]))
s_t=modulated_signal[0]+modulated_signal[1]+modulated_signal[2]

freq = fftpack.fftfreq(min_shape) * samplerate_list[0]
#freq = fftpack.fftfreq(min_shape)
for i in range(0,3):
    freq_signals.append(fftpack.fft(modulated_signal[i]))
freq_signals.append(fftpack.fft(s_t))
s_t_freq=fftpack.fft(s_t)
plt.plot(freq, s_t_freq.real)
plt.show()
print((1700/2*np.pi))
filtered=butter_bandpass_filter(s_t,int(5000/2*np.pi),samplerate_list[0],3)
filtered_freq=fftpack.fft(filtered)
plt.plot(freq, filtered_freq.real)
plt.show()
x_t=filtered*modulating_signal[0]
x_t=butter_bandpass_filter(x_t,int(5000/2*np.pi),samplerate_list[0],3)
x_t=np.array(x_t,dtype=np.int16)
plt.plot(t[0],x_t)
wavfile.write("example.wav",samplerate_list[0],x_t)
plt.show()



