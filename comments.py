# for i in range(0,3):
#     x[i]=x[i][0:min_shape]
#     t[i]=t[i][0:min_shape]
# modulating_signal.append(np.cos( (2*np.pi)*5000 * t[0]))
# modulating_signal.append(np.cos( (2*np.pi)*15000 * t[0]))
# modulating_signal.append(np.sin( (2*np.pi)*15000 * t[0]))
# for i in range(0,3):
#     modulated_signal.append(np.multiply(x[i],modulating_signal[i]))

# s_t=modulated_signal[0]+modulated_signal[1]+modulated_signal[2]

#---------- freq = fftpack.fftfreq(min_shape)

#-----------------------------------------------------------demodulating
# for i in range(0,3):
#     freq_signals.append(fftpack.fft(modulated_signal[i]))
# freq_signals.append(fftpack.fft(s_t))
# s_t_freq=fftpack.fft(s_t)
# plt.plot(freq, s_t_freq.real)
# plt.show()

# x1=butter_lowpass_filter(s_t,7000,samplerate_list[0],12)

# x23=s_t-x1
# x2=x23*modulating_signal[1]
# x3=x23*modulating_signal[2]
# x1=x1*modulating_signal[0]

# x2=butter_lowpass_filter(x2,7000,samplerate_list[0],12)
# x3=butter_lowpass_filter(x3,7000,samplerate_list[0],12)
# x1=butter_lowpass_filter(x1,5000,samplerate_list[0],12)
# x2=2*x2
# x3=2*x3
# x1=2*x1

# x1=np.array(x1,dtype=np.int16)
# x2=np.array(x2,dtype=np.int16)
# x3=np.array(x3,dtype=np.int16)
