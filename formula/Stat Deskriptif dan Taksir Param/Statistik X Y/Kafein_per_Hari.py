from cmath import sqrt
import pandas as pd

df = pd.read_csv('sampel_kopi.csv')
column_name = 'Konsumsi Kafein per hari'
sorted_data = df[column_name].sort_values().tolist()

# Total dan Jumlah data
sum_konsumsi = df[column_name].sum()
total_data = len(df[column_name])

# Rata-rata dan Median
rerata = sum_konsumsi / total_data
data_50 = sorted_data[49]
data_51 = sorted_data[50]
median = (data_50 + data_51) / 2

# Variansi dan Standar Deviasi
variansi = 0
for x in sorted_data:
    variansi += (x - rerata) ** 2
variansi /= (total_data - 1)
standar_deviasi = sqrt(variansi).real

# Output
print(f"| Statistik '{column_name}'")
print(f"|-------------------------------")
print(f"| Jumlah: {sum_konsumsi:.4f}")
print(f"| Total Data: {total_data}")
print(f"|------------------------------")
print(f"| Rerata: {rerata:.4f}")
print(f"| Data ke-50: {data_50:.4f}")
print(f"| Data ke-51: {data_51:.4f}")
print(f"| Median: {median:.4f}")
print(f"|------------------------------")
print(f"| Variansi: {variansi:.4f}")
print(f"| Standar Deviasi: {standar_deviasi:.4f}")
print(f"|------------------------------")