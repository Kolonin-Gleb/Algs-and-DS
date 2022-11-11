# Объяснение на английском: https://youtu.be/3tjngP-X7hE
# Алгоритм Флойда-Уоршалла = алгоритм поиска кратчайшего пути в взвешенном графе с отрицательными ребрами.
'''
'''

def floyd_warshall(nodes: list, edges: dict):
    # Инициализация ребер. Расстояний между вершинами
    d = {(u, v): float('inf') if u != v else 0 for u in nodes for v in nodes}
    for (u, v), w_uv in edges.items():
        d[(u, v)] = w_uv
    
    for k in nodes:
        for u in nodes:
            for v in nodes:
                d[(u, v)] = min(d[(u, v)], d[(u, k)] + d[(k, v)])
    
    if any(d[(u, v)] < 0 for u in nodes):
        print("В графе имеется отрицательный цикл!")

    return d


# 2. Граф с 1 отрицательным ребром
'''
'''
nodes = [0, 1, 2, 3, 4, 5] # Названия вершин
edges = {(0, 1): 1.0, (0, 2): 1.5, (0, 3): 2.0, (1, 0): 1.0, (1, 3): 0.5,
        (1, 4): 2.5, (2, 3): 1.5, (3, 1): 0.5, (4, 5): 2.0, (5, 3): -4.5}

shortest_path_lengths = floyd_warshall(nodes, edges)
print(shortest_path_lengths)
