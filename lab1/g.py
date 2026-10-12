import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
Fs, y = wavfile.read('zapis.wav')

print(len(y))
print(Fs)

Fss = int(len(y) / 6)
print(Fss)
y1 = y[::10]
Fs1 = int(Fs / 10)
wavfile.write('z.wav', Fs1, y1)

T = 1 / Fs
Y = np.fft.fft(y)
N = len(y)
A = np.abs(Y) / N
freq = np.fft.fftfreq(N, d = T)
freq_pos = freq[:N // 2]
A_pos = A[:N // 2]

plt.plot(freq_pos, A_pos)
plt.title('Амплитудный спектр оригинала')
plt.grid()
plt.show()

T = 1 / Fs1
Y = np.fft.fft(y1)
N = len(y1)
A = np.abs(Y) / N
freq = np.fft.fftfreq(N, d = T)
freq_pos = freq[:N // 2]
A_pos = A[:N // 2]

plt.plot(freq_pos, A_pos)
plt.title('Амплитудный спектр прореженного сигнала')
plt.grid()
plt.show()