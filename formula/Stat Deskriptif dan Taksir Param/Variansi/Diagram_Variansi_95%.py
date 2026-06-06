import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

df = 99

chi90_lower = 77.05
chi90_upper = 123.23

chi95_lower = 73.36
chi95_upper = 128.42

x = np.linspace(40, 170, 2000)
y = chi2.pdf(x, df)

plt.figure(figsize=(10,6))

plt.plot(x, y, linewidth=2)

mask95 = (x >= chi95_lower) & (x <= chi95_upper)
plt.fill_between(x[mask95], y[mask95],
                 alpha=0.35,
                 label='Interval Kepercayaan 95%')

plt.axvline(df, linestyle='--',
            label=f'v = {df}', color='black')
plt.axvline(chi95_lower, linestyle='--',
            label=f'χ²₀.₀₂₅ = {chi95_lower}', color='red')
plt.axvline(chi95_upper, linestyle='--',
            label=f'χ²₀.₉₇₅ = {chi95_upper}', color='green')

plt.title('Distribusi Chi-Square pada Tingkat Kepercayaan 95% untuk Variansi Populasi')
plt.xlabel('χ²')
plt.ylabel('Densitas')
plt.legend()
plt.grid(True)
plt.show()