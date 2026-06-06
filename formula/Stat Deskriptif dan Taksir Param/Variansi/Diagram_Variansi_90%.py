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

mask90 = (x >= chi90_lower) & (x <= chi90_upper)
plt.fill_between(x[mask90], y[mask90],
                 alpha=0.35,
                 label='Interval Kepercayaan 90%')

plt.axvline(df, linestyle='--',
            label=f'v = {df}', color='black')
plt.axvline(chi90_lower, linestyle='--',
            label=f'χ²₀.₀₅ = {chi90_lower}', color='red')
plt.axvline(chi90_upper, linestyle='--',
            label=f'χ²₀.₉₅ = {chi90_upper}', color='green')

plt.title('Distribusi Chi-Square pada Tingkat Kepercayaan 90% untuk Variansi Populasi')
plt.xlabel('χ²')
plt.ylabel('Densitas')
plt.legend()
plt.grid(True)
plt.show()