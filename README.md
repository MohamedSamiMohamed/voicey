# Voicey
Voicey is a project for modulating and demodulating three audio signals by the following formula
```bash
s(t) = x1(t)cos(ω1*t)+ x2(t)cos(ω2*t)+ x3(t)sin(ω2*t)
```
to simulate sending and receiving signals through channels.<br/>
QAM and DBSC techniques are used to solve this problem.
## Signals plots in frquency and time domains
Frequency domain |  Time domain
:-------------------------:|:-------------------------:
![magnitude spectrum for input signals summation](plots/music_signal_spectrum.png) | ![input signals summation in time domain](plots/music_signal_time.png)

## Original Vs demodulated signals
0 degree phase shift:
original signal |  demodulated signal
:-------------------------:|:-------------------------:
![](plots/original1.png) | ![](plots/demodulated1.png)
![](plots/original2.png) | ![](plots/demodulated2.png)
![](plots/original3.png) | ![](plots/demodulated3.png)


30 degree phase shift:
original signal |  demodulated signal
:-------------------------:|:-------------------------:
![](plots/original1.png) | ![](plots/demodulated1_30.png)
![](plots/original2.png) | ![](plots/demodulated2_30.png)
![](plots/original3.png) | ![](plots/demodulated3_30.png)

90 degree phase shift:
original signal |  demodulated signal
:-------------------------:|:-------------------------:
![](plots/original1.png) | ![](plots/demodulated1_90.png)
![](plots/original2.png) | ![](plots/demodulated2_90.png)
![](plots/original3.png) | ![](plots/demodulated3_90.png)
