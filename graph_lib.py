import random
import time


# ---Структура графа ---
class Graph:
    def __init__(self, num_vertices: int):
        self.V = num_vertices
        self.adj_list = {i: [] for i in range(self.V)}

    def add_edge(self, u: int, v: int, weight: int):
        if 0 <= u < self.V and 0 <= v < self.V:
            self.adj_list[u].append((v, weight))

    def to_adjacency_matrix(self):
        matrix = [[float('inf')] * self.V for _ in range(self.V)]
        for i in range(self.V):
            matrix[i][i] = 0
            for neighbor, weight in self.adj_list[i]:
                matrix[i][neighbor] = weight
        return matrix


# --- Генератор ---
def generate_random_graph(num_vertices: int, density: float, min_weight: int = 1, max_weight: int = 10) -> Graph:
    g = Graph(num_vertices)
    max_edges = num_vertices * (num_vertices - 1)
    target_edges_count = int(max_edges * density)
    existing_edges = set()
    current_edges_count = 0

    while current_edges_count < target_edges_count:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        if u != v and (u, v) not in existing_edges:
            weight = random.randint(min_weight, max_weight)
            g.add_edge(u, v, weight)
            existing_edges.add((u, v))
            current_edges_count += 1
    return g


# Алгоритм Беллмана-Форда

# Версія для списків суміжності
def bellman_ford_list(graph, src: int):
    dist = [float('inf')] * graph.V
    dist[src] = 0

    for _ in range(graph.V - 1):
        changed = False
        for u in range(graph.V):
            for v, weight in graph.adj_list[u]:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    changed = True
        if not changed: break

    # Перевірка на наявність циклів від'ємної ваги
    for u in range(graph.V):
        for v, weight in graph.adj_list[u]:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                return None  # Знайдено цикл від'ємної ваги
    return dist


# Версія для матриці суміжності
def bellman_ford_matrix(matrix, src: int):
    V = len(matrix)
    dist = [float('inf')] * V
    dist[src] = 0

    for _ in range(V - 1):
        changed = False
        for u in range(V):
            for v in range(V):
                if matrix[u][v] != float('inf'):
                    if dist[u] != float('inf') and dist[u] + matrix[u][v] < dist[v]:
                        dist[v] = dist[u] + matrix[u][v]
                        changed = True
        if not changed: break

    for u in range(V):
        for v in range(V):
            if matrix[u][v] != float('inf'):
                if dist[u] != float('inf') and dist[u] + matrix[u][v] < dist[v]:
                    return None
    return dist