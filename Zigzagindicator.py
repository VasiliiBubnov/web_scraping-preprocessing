import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Загрузка файла csv
import chardet

def detect_encoding(file_path, num_bytes=1000):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read(num_bytes))
    return result['encoding']

file_path = 'pivots.csv'
encoding = detect_encoding(file_path)

df = pd.read_csv(file_path, encoding=encoding)

# 2. Взятие первой колонки
column = df.iloc[:, 0]

# Находим индексы пиков
peak_indices = [i for i in range(1, len(column)-1) if column[i-1] == 0 and column[i] != 0 and column[i+1] == 0]

# Вычисляем параметры для каждого отрезка между пиками
parameters = []
for i in range(1, len(peak_indices)):
    y_diff = column[peak_indices[i]] - column[peak_indices[i-1]]
    x_diff = peak_indices[i] - peak_indices[i-1]
    parameters.append((y_diff, x_diff))

# Сохранение параметров в файл csv
parameters_df = pd.DataFrame(parameters, columns=['y_diff', 'x_diff'])
parameters_df.to_csv(r'C:\Users\ext17\Downloads\parameters2000.csv', index=False)

# Вывод на график первых трех пиков и подпись параметров
plt.plot(column)
for i in range(1, min(4, len(peak_indices))):
    plt.plot([peak_indices[i-1], peak_indices[i]], [column[peak_indices[i-1]], column[peak_indices[i]]])
    plt.text((peak_indices[i-1]+peak_indices[i])/2, (column[peak_indices[i-1]]+column[peak_indices[i]])/2, f'y_diff={parameters[i-1][0]}, x_diff={parameters[i-1][1]}')

plt.show()
