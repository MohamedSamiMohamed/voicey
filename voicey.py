import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import wave
from scipy import fftpack
from scipy.signal import butter, filtfilt
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

#the following two functions apply a low pass filter on the data which will be needed to cut the first signal which has
#a carrier with omega= 5000 away from the other two signals which are modulated by QAM with a carrier of omega = 15000
#----------------------------------------------------------------------------------------------------------------------------------
def butter_lowpass(lowcut, fs, order):
    nyq = 0.5 * fs
    low = lowcut / nyq
    b, a = butter(order, low, btype='low',analog=False)
    return b, a

#-----------------------------------------------------------------------------------------------------------------------------------
def butter_lowpass_filter(data, lowcut, fs, order=5):
    b, a = butter_lowpass(lowcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

#read signal is a function to read a sound signal and store its data which will be needed in modulation and demodulation
#-----------------------------------------------------------------------------------------------------------------------------------
def read_signal(path):
    samplerate, un_modulated=wavfile.read(path)
    un_modulated=np.array(un_modulated,dtype=np.int16)
    #if it's a stereo signal
    if(un_modulated.shape[1]==2):
        data=np.array((un_modulated[:,0]+un_modulated[:,1])/2,dtype=np.int16)
    else:
        data=un_modulated
    #sample rate equals number of samples which is data.shape[0] divided by time taken by the signal
    T=data.shape[0]/samplerate
    #to draw x-axis in time domain
    t.append(np.linspace(0.,T,data.shape[0]))
    x.append(data)
    shape.append(data.shape[0])
    samplerate_list.append(samplerate)

#to modulate the three signals we need to use DBSC for x1(t) and QAM for x2(t) and x3(t)
#-----------------------------------------------------------------------------------------------------------------------------------
def modulation(f,min_shape):
    #we need to make sure that the three signals have the same shape
    for i in range(0,3):
        x[i]=x[i][0:min_shape]
        t[i]=t[i][0:min_shape]
    #creat the carrier with frequencies equals to 5000HZ for x1(t), 15000 HZ for x2(t),x3(t)
    #the frequencies choice was made after looking carefully to the spectrum of each one of them
    modulating_signal.append(np.cos((2*np.pi)*(f[0])* t[0]))
    modulating_signal.append(np.cos((2*np.pi)*(f[1])* t[0]))
    modulating_signal.append(np.sin((2*np.pi)*(f[2])* t[0]))
    #apply modulation
    for i in range(0,3):
        modulated_signal.append(np.multiply(x[i],modulating_signal[i]))
    #get s(t) by adding all three modulated signals to be sent over the channel
    s_t=modulated_signal[0]+modulated_signal[1]+modulated_signal[2]

    return s_t

#here the demodulation part is implemented with parameters of s(t) "modulated signal" , low_pass_freq which will be sent to the 
#low pass filter to extract x1(t), freqs are the frequenicies which will be used to apply low pass filter on each of each of demodulated signals
#f is a list of frequencies to create the simultaneous part of demodulation
#-----------------------------------------------------------------------------------------------------------------------------------
def demodulation(s_t,low_pass_freq,freqs,f,phase_shift):
    #apply transform to frequency domain on all the modulated signals
    for i in range(0,3):
        freq_signals.append(fftpack.fft(modulated_signal[i]))
    freq_signals.append(fftpack.fft(s_t))
    #apply low pass filter on s(t) to extract x1(t)
    x1=butter_lowpass_filter(s_t,low_pass_freq,samplerate_list[0],12)
    #get x2(t) and x3(t) by subtacting s(t) from the extracted signal
    x23=s_t-x1
    #create the demodulating signals
    demodulating_signal.append(np.cos( (2*np.pi)*(f[0])* t[0] + np.radians(phase_shift[0]) ) )
    demodulating_signal.append(np.cos( (2*np.pi)*(f[1])* t[0] + np.radians(phase_shift[1]) ) )
    demodulating_signal.append(np.sin( (2*np.pi)*(f[2])* t[0] + np.radians(phase_shift[2]) ) )
    #apply demodulation by multiplying every modulated signal by its carrier 
    x1=x1*demodulating_signal[0]
    x2=x23*demodulating_signal[1]
    x3=x23*demodulating_signal[2]
    #apply low pass filter on each of the unmodulated signal
    x1=butter_lowpass_filter(x1,freqs[0],samplerate_list[0],12)
    x2=butter_lowpass_filter(x2,freqs[1],samplerate_list[0],12)
    x3=butter_lowpass_filter(x3,freqs[2],samplerate_list[0],12)
    #multiply every signal by two to restore its original values
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
s_t=modulation([5000,15000,15000],min_shape)
plt.plot(t[0],s_t)
plt.xlabel('time')
plt.ylabel('signal')
plt.title('modulated signal in time domain')
plt.show()
freq = fftpack.fftfreq(min_shape) * samplerate_list[0]
s_t_freq=fftpack.fft(s_t)
plt.plot(freq, s_t_freq.real)
plt.xlabel('frequency (HZ)')
plt.title('magnitude spectrum of the modulated signal')
plt.show()

phase_0=[0,0,0]
phase_10=[10,10,10]
phase_30=[30,30,30]
phase_90=[90,90,90]
x1,x2,x3=demodulation(s_t,9000,[4000,4000,4000],[5000,15000,15000],phase_0)



#plotting original signals and demodulated signal
plt.plot(t[0],x[0])
plt.title('original signal 1')
plt.show()

plt.plot(t[0],x1)
plt.title('demodulated signal 1')
plt.show()

plt.plot(t[0],x[1])
plt.title('original signal 2')
plt.show()

plt.plot(t[0], x2)
plt.title('demodulated signal 2')
plt.show()

plt.plot(t[0], x[2])
plt.title('original signal 3')
plt.show()

plt.plot(t[0], x3)
plt.title('demodulated signal 3')
plt.show()

wavfile.write("outputSignal1.wav",samplerate_list[0],x1)
wavfile.write("outputSignal2.wav",samplerate_list[1],x2)
wavfile.write("outputSignal3.wav",samplerate_list[2],x3)
