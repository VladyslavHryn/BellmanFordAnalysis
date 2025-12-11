import time
import csv
import random

try:
    from graph_lib import generate_random_graph, bellman_ford_list, bellman_ford_matrix
except ImportError:
    print("ПОМИЛКА: Не знайдено файл 'graph_lib.py'. Переконайтеся, що основний код збережено у файлі з такою назвою.")
    exit()


def run_experiments():

    # --- Налаштування параметрів---

    sizes = range(10, 251, 10)

    densities = [0.1, 0.3, 0.5, 0.7, 0.9]

    repetitions = 50

    filename = 'results_extended.csv'

    print(f"--- Починаємоексперимент ---")
    print(f"Результати будуть записані у файл: {filename}")
    print(f"Кількість розмірів: {len(sizes)}")
    print(f"Кількість повторень на кожну точку: {repetitions}")

    # Відкриваємо файл для запису
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Заголовки стовпців для CSV
        writer.writerow(['Size (N)', 'Density', 'Avg Time List (sec)', 'Avg Time Matrix (sec)'])

        # Головний цикл по розмірах
        for n in sizes:
            # Цикл по щільності
            for d in densities:

                total_time_list = 0
                total_time_matrix = 0

                # Серія повторень
                for _ in range(repetitions):
                    # Генеруємо граф (min_weight=1)
                    g = generate_random_graph(n, d, min_weight=1, max_weight=10)

                    # Готуємо матрицю
                    matrix = g.to_adjacency_matrix()

                    # Списки суміжності
                    start_time = time.perf_counter()
                    bellman_ford_list(g, 0)
                    end_time = time.perf_counter()
                    total_time_list += (end_time - start_time)

                    # Матриця суміжності
                    start_time = time.perf_counter()
                    bellman_ford_matrix(matrix, 0)
                    end_time = time.perf_counter()
                    total_time_matrix += (end_time - start_time)

                # Рахуємо середній час
                avg_time_list = total_time_list / repetitions
                avg_time_matrix = total_time_matrix / repetitions

                # Записуємо рядок у таблицю
                writer.writerow([n, d, f"{avg_time_list:.6f}", f"{avg_time_matrix:.6f}"])


            print(
                f"--> Завершено для розміру N={n}. Останній час (списки/матриця): {avg_time_list:.5f}s / {avg_time_matrix:.5f}s")

    print(f"\n✅ Експерименти завершено! Дані збережено в '{filename}'.")


if __name__ == "__main__":
    run_experiments()