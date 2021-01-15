import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import wave
from scipy import fftpack
from scipy.signal import butter, lfilter
from scipy.signal import freqz
import math
t=[]
x=[]
shape=[]
samplerate_list=[]
freq_signals=[]
modulated_signal=[]
modulating_signal=[]
demodulating_signal=[]

#-----------------------------------------------------------------------------------------------------------------------
def butter_bandpass(lowcut, fs, order):
    nyq = 0.5 * fs
    low = lowcut / nyq
    b, a = butter(order, low, btype='low',analog=False)
    return b, a

#-----------------------------------------------------------------------------------------------------------------------------------
def butter_lowpass_filter(data, lowcut, fs, order=5):
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
    T=data.shape[0]/samplerate
    t.append(np.linspace(0.,T,data.shape[0]))
    x.append(data)
    shape.append(data.shape[0])
    samplerate_list.append(samplerate)


#-----------------------------------------------------------------------------------------------------------------------------------
def modulation(f,min_shape):
    for i in range(0,3):
        x[i]=x[i][0:min_shape]
        t[i]=t[i][0:min_shape]
    modulating_signal.append(np.cos((2*np.pi)*(f[0])* t[0]))
    modulating_signal.append(np.cos((2*np.pi)*(f[1])* t[0]))
    modulating_signal.append(np.sin((2*np.pi)*(f[2])* t[0]))
    for i in range(0,3):
        modulated_signal.append(np.multiply(x[i],modulating_signal[i]))
    # freq = fftpack.fftfreq(min_shape) * samplerate_list[0]
    # x1_freq=fftpack.fft(modulated_signal[0])
    # plt.plot(freq, x1_freq.real)
    # plt.show()
    s_t=modulated_signal[0]+modulated_signal[1]+modulated_signal[2]
    # freq_signals.append(fftpack.fft(s_t))
    # s_t_freq=fftpack.fft(s_t)
    # plt.plot(freq, s_t_freq.real)
    # plt.show()
    return s_t

#-----------------------------------------------------------------------------------------------------------------------------------
def demodulation(s_t,freqs_first,freqs,f,phase_shift):
    for i in range(0,3):
        freq_signals.append(fftpack.fft(modulated_signal[i]))
    # freq = fftpack.fftfreq(min_shape) * samplerate_list[0]
    x1=butter_lowpass_filter(s_t,freqs_first,samplerate_list[0],12)
    # x1_freq_de=fftpack.fft(x1)
    # plt.plot(freq, x1_freq_de.real)
    # plt.show()
    x23=s_t-x1
    demodulating_signal.append(np.cos(((2*np.pi)*(f[0])* t[0])+ np.radians(phase_shift[0])))
    demodulating_signal.append(np.cos(((2*np.pi)*(f[1])* t[0])+ np.radians(phase_shift[1])))
    demodulating_signal.append(np.sin(((2*np.pi)*(f[2])* t[0])+ np.radians(phase_shift[2])))
    x1=x1*demodulating_signal[0]
    x2=x23*demodulating_signal[1]
    x3=x23*demodulating_signal[2]
    x1=butter_lowpass_filter(x1,freqs[0],samplerate_list[0],12)
    x2=butter_lowpass_filter(x2,freqs[1],samplerate_list[0],12)
    x3=butter_lowpass_filter(x3,freqs[2],samplerate_list[0],12)
    x1=2*x1
    x2=2*x2
    x3=2*x3

    x1=np.array(x1,dtype=np.int16)
    x2=np.array(x2,dtype=np.int16)
    x3=np.array(x3,dtype=np.int16)
    return x1,x2,x3

#-----------------------------------------------------------------------------------------------------------------------------
read_signal("input1.wav")
read_signal("input2.wav")
read_signal("input3.wav")
min_shape=min(shape)


# s_t=modulation([5000,15000,15000],min_shape)

# x1,x2,x3=demodulation(s_t,7000,[5000,7000,7000],[5000,15000,15000],[0,0,0])
# plt.plot(t[0],x[0])
# plt.show()

# plt.plot(t[0],x1)
# plt.show()

# plt.plot(t[0],x[1])
# plt.show()

# plt.plot(t[0], x2)
# plt.show()

# plt.plot(t[0], x[2])
# plt.show()

# plt.plot(t[0], x3)
# plt.show()

# wavfile.write("output0_1.wav",samplerate_list[0],x1)
# wavfile.write("output0_2.wav",samplerate_list[1],x2)
# wavfile.write("output0_3.wav",samplerate_list[2],x3)



# s_t=modulation([5000,15000,15000],min_shape)
# x1,x2,x3=demodulation(s_t,7000,[5000,7000,7000],[5000,15000,15000],[10,10,10])
# plt.plot(t[0],x[0])
# plt.show()

# plt.plot(t[0],x1)
# plt.show()

# plt.plot(t[0],x[1])
# plt.show()

# plt.plot(t[0], x2)
# plt.show()

# plt.plot(t[0], x[2])
# plt.show()

# plt.plot(t[0], x3)
# plt.show()

# wavfile.write("output10_1.wav",samplerate_list[0],x1)
# wavfile.write("output10_2.wav",samplerate_list[1],x2)
# wavfile.write("output10_3.wav",samplerate_list[2],x3)





# s_t=modulation([5000,15000,15000],min_shape)
# x1,x2,x3=demodulation(s_t,7000,[5000,7000,7000],[5000,15000,15000],[30,30,30])
# plt.plot(t[0],x[0])
# plt.show()

# plt.plot(t[0],x1)
# plt.show()

# plt.plot(t[0],x[1])
# plt.show()

# plt.plot(t[0], x2)
# plt.show()

# plt.plot(t[0], x[2])
# plt.show()

# plt.plot(t[0], x3)
# plt.show()

# wavfile.write("output30_1.wav",samplerate_list[0],x1)
# wavfile.write("output30_2.wav",samplerate_list[1],x2)
# wavfile.write("output30_3.wav",samplerate_list[2],x3)

s_t=modulation([5000,15000,15000],min_shape)

x1_90,x2_90,x3_90=demodulation(s_t,7000,[5000,7000,7000],[5000,15000,15000],[90,90,90])
plt.plot(t[0],x[0])
plt.show()

plt.plot(t[0],x1_90)
plt.show()

plt.plot(t[0],x[1])
plt.show()

plt.plot(t[0], x2_90)
plt.show()

plt.plot(t[0], x[2])
plt.show()

plt.plot(t[0], x3_90)
plt.show()

wavfile.write("output90_1.wav",samplerate_list[0],x1_90)
wavfile.write("output90_2.wav",samplerate_list[1],x2_90)
wavfile.write("output90_3.wav",samplerate_list[2],x3_90)
