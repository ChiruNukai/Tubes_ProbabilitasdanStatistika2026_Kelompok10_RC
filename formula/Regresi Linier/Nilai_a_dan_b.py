from cmath import sqrt
import pandas as pd

df = pd.read_csv('sampel_kopi.csv')
column_name = 'Konsumsi Kafein per hari'
column_name2 = 'Rate Detak Jantung per Menit'
sorted_data1 = df[column_name].sort_values().tolist()
sorted_data2 = df[column_name2].sort_values().tolist()

x_total = 0
for x in sorted_data1:
    x_total += x

x_total_squared = 0
for x in sorted_data1:
    x_total_squared += x ** 2

y_total = 0
for y in sorted_data2:
    y_total += y

xy_total = 0
for x, y in zip(sorted_data1, sorted_data2):
    xy_total += x * y


b = 0
b = ((len(sorted_data1) * xy_total) - (x_total * y_total)) / ((len(sorted_data1) * x_total_squared) - x_total ** 2)
a = (y_total - (b * x_total)) / len(sorted_data1)

# Output
print(f"| Statistik '{column_name}'")
print(f"|-------------------------------")
print(f"| Jumlah X: {x_total:.4f}")
print(f"| Jumlah Y: {y_total:.4f}")
print(f"| Jumlah X^2: {x_total_squared:.4f}")
print(f"| X^2: {x_total ** 2:.4f}")
print(f"| Jumlah XY: {xy_total:.4f}")
print(f"| Total Data: {len(sorted_data1)}")
print(f"|------------------------------")
print(f"| Nilai a: {a:.4f}")
print(f"| Nilai b: {b:.4f}")
print(f"|------------------------------")