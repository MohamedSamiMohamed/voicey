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
for i in range(0,3):
    x[i]=x[i][0:min_shape]
    t[i]=t[i][0:min_shape]




plt.plot(t[0],x[2])
plt.show()
modulating_signal.append(np.cos( (2*np.pi)*5000 * t[0]))
modulating_signal.append(np.cos( (2*np.pi)*15000 * t[0]))
modulating_signal.append(np.sin( (2*np.pi)*15000 * t[0]))
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

x1=butter_bandpass_filter(s_t,7000,samplerate_list[0],12)

x23=s_t-x1
x2=x23*modulating_signal[1]
x3=x23*modulating_signal[2]
x1=x1*modulating_signal[0]

x2=butter_bandpass_filter(x2,7000,samplerate_list[0],12)
x3=butter_bandpass_filter(x3,7000,samplerate_list[0],12)
x1=butter_bandpass_filter(x1,5000,samplerate_list[0],12)
x2=2*x2
x3=2*x3
x1=2*x1

x1=np.array(x1,dtype=np.int16)
x2=np.array(x2,dtype=np.int16)
x3=np.array(x3,dtype=np.int16)

plt.plot(t[0],x[0])
plt.show()

plt.plot(t[0],x1)
plt.show()

plt.plot(t[0],x[1])
plt.show()

plt.plot(t[0], x2)
plt.show()


plt.plot(t[0], x[2])
plt.show()

plt.plot(t[0], x3)
plt.show()



wavfile.write("example.wav",samplerate_list[0],x1)
wavfile.write("example2.wav",samplerate_list[1],x2)
wavfile.write("example3.wav",samplerate_list[2],x3)






