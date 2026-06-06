import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Load data
df = pd.read_csv("sampel_kopi.csv")

X = 'Konsumsi Kafein per hari'
Y = 'Rate Detak Jantung per Menit'

# Parameter regresi dari hasil perhitungan manual
a = 53.41
b = 0.068

# Garis regresi
x_line = np.linspace(X.min(), X.max(), 300)
y_line = a + b * x_line

# ---- Plot ----
fig, ax = plt.subplots(figsize=(10, 6))

# Scatter plot per gender
colors = {"Laki-laki": "#2196F3", "Perempuan": "#E91E63", "Other": "#4CAF50"}
for gender, grp in df.groupby("Gender"):
    ax.scatter(
        grp['Konsumsi Kafein per hari'],
        grp['Rate Detak Jantung per Menit'],
        color=colors.get(gender, "gray"),
        alpha=0.75,
        edgecolors="white",
        linewidths=0.5,
        s=70,
        label=gender,
        zorder=3,
    )

# Garis regresi
ax.plot(x_line, y_line, color="#6F4E37", linewidth=2.5,
        label=r"$\hat{Y} = 53.41 + 0.068X$", zorder=4)

# Anotasi persamaan di dalam plot
ax.text(
    0.97, 0.05,
    r"$\hat{Y} = 53.41 + 0.068X$",
    transform=ax.transAxes,
    fontsize=12,
    ha="right",
    va="bottom",
    color="#6F4E37",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="#6F4E37", alpha=0.8),
)

# Labels & styling
ax.set_title("Scatter Plot & Garis Regresi Linear\nKonsumsi Kafein vs Rate Detak Jantung", 
             fontsize=13, fontweight="bold", pad=14)
ax.set_xlabel("Konsumsi Kafein per Hari (mg)", fontsize=12)
ax.set_ylabel("Rate Detak Jantung per Menit (bpm)", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(fontsize=10, title="Gender", title_fontsize=10, loc="upper left")

# Axis limits dengan sedikit padding
ax.set_xlim(X.min() - 20, X.max() + 20)
ax.set_ylim(Y.min() - 3, Y.max() + 5)

plt.tight_layout()
plt.savefig("regresi_kopi.png", dpi=150, bbox_inches="tight")
plt.show()
print("Plot tersimpan: regresi_kopi.png")
