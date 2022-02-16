# 1) Реализовать рекурсивный алгоритм поиска в глубину +
# 2) Реализовать вычисление числа компонент связности. Т.е. кол. не связанных графов.

# Представление графа в виде списка смежностей.

# graph - словарь вершина и множество смежных вершин
graph = {
'A': {'B'},
'B': {'A', 'C'},
'C': {'B', 'D'},
'D': {'C'},
'F': {} # F - обособленная вершина
}

def DFS(graph, start_vertex, visited):
    visited.add(start_vertex)

    # Проход по всем смежным с текущей вершиной
    for neighboor in graph[start_vertex]:
        if neighboor not in visited:
            DFS(graph, neighboor, visited)

# Используем множества, т.к. с ней проверка на наличие происходит быстрее, 
# чем проверка в списке
# visited = set()
# DFS(graph, 'A', visited)
# print(visited) - результат обхода


def count_connectivity_component(graph, visited, count):
    for vertex in graph:
        if vertex not in visited:
            DFS (graph, vertex, visited)
            count += 1
    return count

visited = set()
count_connectivity_components = 0

count_connectivity_components = count_connectivity_component(graph, visited, count_connectivity_components)
print(count_connectivity_components) #  - результат обхода

# Топологическая сортировка
# В следующий раз
# КТ 2 марта

