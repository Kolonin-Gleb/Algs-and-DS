# Представление графа в виде списка смежностей.

graph = {
'A': ['B'],
'B': ['A', 'C'],
'C': ['B', 'D'],
'D': ['C'],
'F': [] # F - обособленная вершина
}

# Рекурсивный алгоритм поиска в глубину +
def DFS(graph, start_vertex, visited):
    visited.add(start_vertex)

    # Проход по всем смежным с текущей вершиной
    for neighboor in graph[start_vertex]:
        if neighboor not in visited:
            DFS(graph, neighboor, visited)

visited = set()
DFS(graph, 'A', visited)
print(visited)

# Подсчёт числа компонент связности
def count_connectivity_component(graph, visited, count = 0):
    for vertex in graph:
        if vertex not in visited:
            DFS (graph, vertex, visited)
            count += 1
    return count

visited = set()
print(count_connectivity_component(graph, visited))

