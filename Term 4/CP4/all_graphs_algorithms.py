# Дек для алгоритмов с поиском в ширину
from collections import deque
'''
Эффективная реализация очереди - 2х связный список
enqueue - вход в очередь
dequeue - выход из очереди
'''

# Рекурсивный алгоритм поиска в глубину от заданной вершины +
def DFS(graph, start_vertex, visited = set()):
    visited.add(start_vertex)

    # Проход по всем смежным с текущей вершиной
    for neighboor in graph[start_vertex]:
        if neighboor not in visited:
            DFS(graph, neighboor, visited)
    
    return visited # Порядок каждый раз разный, из-за использования множеств.

# Подсчёт числа компонент связности
def count_connectivity_component(graph, visited = set(), count = 0):
    for vertex in graph:
        if vertex not in visited:
            DFS (graph, vertex, visited)
            count += 1
    return count

# Поиск / Обход в ширину
def bfs(graph, vertex_start):
    visited = [] # Как список, чтобы видеть порядок. (Можно делать через множество)
    queue = deque() # Дек - очередь с двух сторон
    queue.append(vertex_start)
    visited.append(vertex_start)

    while queue: # Пока все вершины не обойдём
        vertex = queue.popleft()

        # Обход смежных вершин
        for u in graph[vertex]: # Идём по ключам текущей вершины
            if u not in visited:
                visited.append(u)
                queue.append(u)

    return visited

# Поиск / Обход в ширину с расстояниями
def bfs_distances(graph, start):
    distances = {}
    # Изначально расстояние до всех вершин - неопределено
    for v in graph:
        distances[v] = 0
    
    visited = []
    visited.append(start)
    queue = deque()
    queue.append(start)

    while queue:
        cur = queue[0]
        queue.popleft()

        for u in graph[cur]: # Для каждой смежной с текущей вершиной
            if u not in visited:
                visited.append(u) # Посетили
                queue.append(u) # Нужно посетить соседей
                distances[u] += distances[cur] + 1 # Сохранили расстояние
    
    return distances

# Поиск родителей вершин при обходе в ширину
def bfs_parent(graph, start):
    parent = {} # словарь

    # Изначально родители вершин - неопределены
    for v in graph:
        parent[v]=None

    visited = [] # Посещенные вершины
    visited.append(start)
    queue = deque()
    queue.append(start)

    while queue: # Пока не обошли все вершины
        cur = queue[0]
        queue.popleft()

        for u in graph[cur]: # Проход по всем смежным вершинам с текущей (cur)
            if u not in visited:
                visited.append(u) # Посетили
                queue.append(u) # Нужно посетить её соседей
                parent[u] = cur # Из какой вершины пришли в эту
                
    return parent

''' Вычисление кол. компонент связности - Реализуется с помощью DFS '''

# Восстановление кратчайшего пути по 2 вершинам
def shortest_path(graph, start, end):
    parents = bfs_parent(graph, start) # Родитель для начальной вершины будет None
    path = []
    path.append(end)

    # Формируем кратчайший путь с конца.
    while start not in path:
        parent = parents[end]
        path.append(parent)
        end = parent
    
    return path[::-1] # Вывод сформированного пути от начальной точки

# Наличие вершины на кратчайшем пути
def vertex_on_shortest_path(graph, start, end, x):
    distances_from_start = bfs_distances(graph, start) # Расстояния обхода в ширину из начальной вершины
    distances_from_end = bfs_distances(graph, end)     # Расстояния обхода в ширину из конечной вершины

    # Если сумма наикратчайших расстояний до проверяемой вершины из нач. и кон. точки
    # = наикратчайшему расстоянию из нач. в кон. точку, то
    if distances_from_start[x] + distances_from_end[x] == distances_from_start[end]: 
        return 'Vertex is on the shortest path'
    else:
        return 'Vertex is not on the shortest path'

# Наличие ребра на кратчайшем пути
def edge_on_shortest_path(graph, start, end, edge):
    # edge - две буквы, соответствующие вершинам образующим грань в графе
    distances_from_start = bfs_distances(graph, start) # Расстояния обхода в ширину из начальной вершины
    distances_from_end = bfs_distances(graph, end)     # Расстояния обхода в ширину из конечной вершины

    # print(distances_from_start)
    # print(distances_from_end)

    if distances_from_start[edge[0]] + distances_from_end[edge[1]] + 1 == distances_from_start[end]:
        return 'The edge is on the shortest path'
    else:
        return 'The edge is not on the shortest path'

# Граф в виде списков связностей
graph = {
'A': ['B'],
'B': ['A', 'C', 'D'],
'C': ['E', 'D', 'B'],
'D': ['B', 'C'],
'E': ['C']
}

gr = {
'A': ['B'],
'B': ['A', 'C'],
'C': ['B'],
}

''' DFS алгоритмы '''
# print(DFS(graph, 'A'))
# print(count_connectivity_component(graph)) #  - результат обхода
''' BFS алгоритмы '''
# print(bfs_distances(graph, 'A')) +
# print(bfs(graph, 'D')) +
# print(bfs_parent(graph, 'A')) +
# print(shortest_path(graph,'A','E')) +
# print(vertex_on_shortest_path(graph, 'A', 'E', 'D')) +
print(edge_on_shortest_path(gr, 'A', 'C', 'BC'))


