import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load data
df = pd.read_csv("sampel_kopi.csv")

# Nama kolom
col_x = "Konsumsi Kafein per hari"
col_y = "Rate Detak Jantung per Menit"

# Buat figure dengan 2 subplot berdampingan
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Distribusi Variabel Konsumsi Kopi", fontsize=14, fontweight="bold", y=0.95)

# --- Histogram X: Konsumsi Kafein per Hari ---
axes[0].hist(df[col_x], bins=15, color="#6F4E37", edgecolor="white", linewidth=0.8)
axes[0].set_title("Histogram Konsumsi Kafein per Hari (X)", fontsize=12, fontweight="bold")
axes[0].set_xlabel("Kafein (mg)", fontsize=11)
axes[0].set_ylabel("Frekuensi", fontsize=11)
axes[0].yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
axes[0].grid(axis="y", linestyle="--", alpha=0.5)

# Tambahkan garis mean
mean_x = df[col_x].mean()
axes[0].axvline(mean_x, color="red", linestyle="--", linewidth=1.5, label=f"Mean: {mean_x:.1f} mg")
axes[0].legend(fontsize=10)

# --- Histogram Y: Rate Detak Jantung per Menit ---
axes[1].hist(df[col_y], bins=15, color="#C1440E", edgecolor="white", linewidth=0.8)
axes[1].set_title("Histogram Rate Detak Jantung per Menit (Y)", fontsize=12, fontweight="bold")
axes[1].set_xlabel("Detak Jantung (bpm)", fontsize=11)
axes[1].set_ylabel("Frekuensi", fontsize=11)
axes[1].yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
axes[1].grid(axis="y", linestyle="--", alpha=0.5)

# Tambahkan garis mean
mean_y = df[col_y].mean()
axes[1].axvline(mean_y, color="blue", linestyle="--", linewidth=1.5, label=f"Mean: {mean_y:.1f} bpm")
axes[1].legend(fontsize=10)

plt.tight_layout()
plt.savefig("histogram_kopi.png", dpi=150, bbox_inches="tight")
plt.show()

print("Statistik Deskriptif:")
print(df[[col_x, col_y]].describe().round(2))
