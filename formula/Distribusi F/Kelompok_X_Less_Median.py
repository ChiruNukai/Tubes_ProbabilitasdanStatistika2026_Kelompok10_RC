from cmath import sqrt
import pandas as pd

df = pd.read_csv('split_dataset_median.csv')
column_name = 'Y1'
sorted_data = df[column_name].sort_values().tolist()

# Total dan Jumlah data
sum_konsumsi = df[column_name].sum()
total_data = len(df[column_name])

# Rata-rata
rerata = sum_konsumsi / total_data

# Variansi dan Standar Deviasi
variansi = 0
for x in sorted_data:
    variansi += (x - rerata) ** 2

standar_deviasi = sqrt(variansi).real

# Output
print(f"| Statistik '{column_name}'")
print(f"|-------------------------------")
print(f"| Jumlah: {sum_konsumsi:.4f}")
print(f"| Total Data: {total_data}")
print(f"|------------------------------")
print(f"| Rerata: {rerata:.4f}")
print(f"|------------------------------")
print(f"| Variansi: {variansi:.4f}")
print(f"| Standar Deviasi: {standar_deviasi:.4f}")
print(f"|------------------------------")