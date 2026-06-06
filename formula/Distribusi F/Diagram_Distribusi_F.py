import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Parameter
d1, d2 = 49, 49
f_hitung = 1.15
f_crit_05 = 1.61
f_crit_01 = 1.96

# Generate nilai x dan y untuk kurva
x = np.linspace(0.01, 3.5, 500)
y = stats.f.pdf(x, d1, d2)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot kurva utama
ax.plot(x, y, color='#378ADD', linewidth=2, label='Distribusi F')

# Area penerimaan H0 (x <= f_crit_05)
x_accept = x[x <= f_crit_05]
y_accept = stats.f.pdf(x_accept, d1, d2)
ax.fill_between(x_accept, y_accept, alpha=0.35, color='blue', label='Area penerimaan H₀')

# Area penolakan H0 (x >= f_crit_05)
x_reject = x[x >= f_crit_05]
y_reject = stats.f.pdf(x_reject, d1, d2)
ax.fill_between(x_reject, y_reject, alpha=0.45, color='red', label='Area penolakan H₀')

# Garis vertikal
ax.axvline(f_hitung, color='black', linewidth=2, linestyle='--',
           label=f'F hitung = {f_hitung}')
ax.axvline(f_crit_05, color='red', linewidth=2, linestyle='--',
           label=f'f₀.₀₅(49,49) = {f_crit_05}')
ax.axvline(f_crit_01, color='green', linewidth=2, linestyle='--',
           label=f'f₀.₀₁(49,49) = {f_crit_01}')

# Label pada garis vertikal
y_max = max(y)
ax.text(f_hitung + 0.03, y_max * 0.85, f'F={f_hitung}',
        color='#1D9E75', fontsize=10)
ax.text(f_crit_05 + 0.03, y_max * 0.70, f'f₀.₀₅={f_crit_05}',
        color='#E24B4A', fontsize=10)
ax.text(f_crit_01 + 0.03, y_max * 0.55, f'f₀.₀₁={f_crit_01}',
        color='#BA7517', fontsize=10)

# Styling
ax.set_xlabel('F', fontsize=13)
ax.set_ylabel('Densitas', fontsize=13)
ax.set_title('Distribusi F(49, 49) — Uji Validasi Perbedaan Variansi', fontsize=14, pad=15)
ax.legend(loc='upper right', fontsize=9)
ax.set_xlim(0, 3.5)
ax.set_ylim(0, y_max * 1.1)
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('f_distribution.png', dpi=150, bbox_inches='tight')
plt.show()

# Print ringkasan hasil
print("=" * 45)
print("  Uji Validasi Perbedaan Variansi (F-Test)")
print("=" * 45)
print(f"  S²Y1          = 92.46")
print(f"  S²Y2          = 80.43")
print(f"  F hitung      = {f_hitung}")
print(f"  f₀.₀₅(49,49)  = {f_crit_05}")
print(f"  f₀.₀₁(49,49)  = {f_crit_01}")
print("-" * 45)
print(f"  F hitung < f₀.₀₅ : {f_hitung < f_crit_05}")
print(f"  F hitung < f₀.₀₁ : {f_hitung < f_crit_01}")
print("-" * 45)
print("  Kesimpulan: H₀ DITERIMA")
print("  Kedua variansi memiliki kesamaan.")
print("=" * 45)