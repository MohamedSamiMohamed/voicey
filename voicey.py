#from pydub import AudioSegment
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
#from plotly.offline import init_notebook_mode
#import plotly.graph_objs as go
#import plotly

samplerate, un_modulated=wavfile.read("output2.wav")
un_modulated =np.array(un_modulated)
t = np.linspace(0., 1., samplerate)
print(samplerate)
print(un_modulated[:,0].max())
modulating_signal=np.cos(2. * np.pi * 200000 * t)
plt.plot(t,modulating_signal)
print(modulating_signal)
#modulated_signal=np.multiply(un_modulated,modulating_signal)
#wavfile.write("example.wav", samplerate, modulated_signal)

#print(fs)
#print(data.shape)
# samplerate = 44100
# fs = 100

# amplitude = np.iinfo(np.int16).max
# data = amplitude * np.sin(2. * np.pi * fs * t)
# wavfile.write("example.wav", samplerate, data)
