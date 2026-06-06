import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x_bar = 252.19
lower = 229.99
upper = 274.39
SE = 133.17 / np.sqrt(100)

x = np.linspace(200, 305, 1000)
y = norm.pdf(x, x_bar, SE)

plt.figure(figsize=(10,6))
plt.plot(x, y)

plt.axvline(x_bar, color='black', linestyle='--',
            label=f'Mean = {x_bar}')
plt.axvline(lower, linestyle='--',
            label=f'Batas Bawah = {lower}', color='red')
plt.axvline(upper, linestyle='--',
            label=f'Batas Atas = {upper}', color='green')

plt.fill_between(
    x,
    y,
    where=(x >= lower) & (x <= upper),
    alpha=0.3,
    label='Interval Kepercayaan 90%'
)

plt.title('Distribusi T pada Tingkat Kepercayaan 90% untuk Rata-rata Populasi')
plt.xlabel('μ')
plt.ylabel('Densitas')
plt.legend()
plt.grid(True)
plt.show()