# Voicey
Voicey is a project for modulating and demodulating three audio signals by the following formula
```bash
s(t) = x1(t)cos(ω1*t)+ x2(t)cos(ω2*t)+ x3(t)sin(ω2*t)
```
to simulate sending and receiving signals through channels.
## Signals plots in frquency and time domains
Frequency domain |  Time domain
:-------------------------:|:-------------------------:
![magnitude spectrum for input signals summation](plots/music_signal_spectrum.png) | ![input signals summation in time domain](plots/music_signal_time.png)

### Original and demodulated signals
0 degree phase shift:
original signal |  demodulated signal
:-------------------------:|:-------------------------:
![magnitude spectrum for input signals summation](plots/music_signal_spectrum.png) | ![input signals summation in time domain](plots/music_signal_time.png)
![magnitude spectrum for input signals summation](plots/music_signal_spectrum.png) | ![input signals summation in time domain](plots/music_signal_time.png)
![magnitude spectrum for input signals summation](plots/music_signal_spectrum.png) | ![input signals summation in time domain](plots/music_signal_time.png)

30 degree phase shift:
original signal |  demodulated signal
:-------------------------:|:-------------------------:
![magnitude spectrum for input signals summation](plots/music_signal_spectrum.png) | ![input signals summation in time domain](plots/music_signal_time.png)
![magnitude spectrum for input signals summation](plots/music_signal_spectrum.png) | ![input signals summation in time domain](plots/music_signal_time.png)
![magnitude spectrum for input signals summation](plots/music_signal_spectrum.png) | ![input signals summation in time domain](plots/music_signal_time.png)

90 degree phase shift:
original signal |  demodulated signal
:-------------------------:|:-------------------------:
![magnitude spectrum for input signals summation](plots/music_signal_spectrum.png) | ![input signals summation in time domain](plots/music_signal_time.png)
![magnitude spectrum for input signals summation](plots/music_signal_spectrum.png) | ![input signals summation in time domain](plots/music_signal_time.png)
![magnitude spectrum for input signals summation](plots/music_signal_spectrum.png) | ![input signals summation in time domain](plots/music_signal_time.png)
