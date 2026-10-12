import numpy as np
import matplotlib.pyplot as plt

f = 4
def fun(t):
    y = np.sin(12 * np.pi * f * t + np.pi / 11) + np.sin(10 * np.pi * f * t)
    return y

fm = 24
fd = 24 * 2

samples = np.arange(0, 1, 1 / fd)
ys = fun(samples)

plt.figure('Оцифрованный сигнал')
plt.plot(samples, ys)
plt.show()

N = len(ys)
Y = np.fft.fft(ys)
A = np.abs(Y)
freq = np.fft.fftfreq(N, d=1 / fd)

plt.figure('Амплитудный спектр')
plt.stem(freq[:N // 2], A[:N // 2])
plt.title('Амплитудный спектр')
plt.xlabel('Частота (Гц)')
plt.grid()
plt.show()

print('Объем памяти: ', len(ys) * 8)

ti = np.linspace(0, 1, 1000)
yi = fun(ti)

plt.figure('Исходный и восстановленный сигнал')
plt.subplot(2, 1, 1)
plt.plot(ti, yi, label='Исходный сигнал')
plt.subplot(2, 1, 2)
plt.plot(samples, ys, label='Восстановленный сигнал')
plt.show()

fd_new = 24 * 2 * 4
samples_new = np.arange(0, 1, 1 / fd_new)
ys_new = fun(samples_new)

plt.figure('Оцифрованный сигнал (fd * 4)')
plt.plot(samples_new, ys_new)
plt.show()

N_new = len(ys_new)
Y_new = np.fft.fft(ys_new)
A_new = np.abs(Y_new)
freq_new = np.fft.fftfreq(N_new, d=1 / fd_new)

plt.figure('Амплитудный спектр (fd * 4)')
plt.stem(freq_new[:N_new // 2], A_new[:N_new // 2])
plt.title('Амплитудный спектр')
plt.xlabel('Частота (Гц)')
plt.grid()
plt.show()

print('Объем памяти: ', len(ys_new) * 8)

plt.figure('Исходный и восстановленный сигнал (fd * 4)')
plt.subplot(2, 1, 1)
plt.plot(ti, yi, label='Исходный сигнал')
plt.subplot(2, 1, 2)
plt.plot(samples_new, ys_new, label='Восстановленный сигнал')
plt.show()

y_min = min(yi)
y_max = max(yi)

for i in range(3 , 7):
    m = 2 ** i - 1
    yq = []
    for j in yi:
        norm = (j - y_min) / (y_max - y_min)
        q = round(norm * m)
        qr = y_min + q * (y_max - y_min) / m
        yq.append(qr)

    se = 0
    for j in range(len(yi)):
        error = abs(yi[j] - yq[j])
        se += error

    avg = se / len(yi)
    print('Средняя ошибка квантования ', i, 'бит : ', avg)

N = len(ys)
freq = np.fft.fftfreq(N, d=1/fd)

Y = np.fft.fft(ys)
A = np.abs(Y)

y_min = min(ys)
y_max = max(ys)
m = 2 ** 3 - 1
yq = []

for i in ys:
    norm = (i - y_min) / (y_max - y_min)
    q = round(norm * m)
    qr = y_min + q * (y_max - y_min) / m
    yq.append(qr)

Yq = np.fft.fft(yq)
Aq = np.abs(Yq)

plt.figure(figsize=(10, 5))
plt.plot(freq[:N // 2], A[:N // 2], label='Оригинал')
plt.plot(freq[:N // 2], Aq[:N // 2], label='3 бита', linestyle='--')
plt.title('Сравнение спектров')
plt.xlabel('Частота (Гц)')
plt.legend()
plt.grid()
plt.show()