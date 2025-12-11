import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('results_extended.csv')
except FileNotFoundError:
    print(" Файл results_extended.csv не знайдено! Спочатку запустіть experiments.py")
    exit()

plt.style.use('ggplot')

densities = df['Density'].unique()
print(f"Знайдено варіантів щільності: {densities}")

for d in densities:
    subset = df[df['Density'] == d]

    plt.figure(figsize=(10, 6))

    plt.plot(subset['Size (N)'], subset['Avg Time List (sec)'],
             label='Список суміжності', marker='o', linewidth=2)

    plt.plot(subset['Size (N)'], subset['Avg Time Matrix (sec)'],
             label='Матриця суміжності', marker='x', linewidth=2)

    plt.title(f'Порівняння швидкості (Щільність: {d})')
    plt.xlabel('Кількість вершин (N)')
    plt.ylabel('Час виконання (сек)')
    plt.legend()
    plt.grid(True)

    filename = f'plot_density_{d}.png'
    plt.savefig(filename)
    print(f"Збережено графік: {filename}")
    plt.close()

print("\n Готово! Зображення збережено у папці проєкту.")