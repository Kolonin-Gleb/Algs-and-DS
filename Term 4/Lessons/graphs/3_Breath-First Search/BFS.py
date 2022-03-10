# Поиск в ширину
from collections import deque
from multiprocessing import parent_process

# Граф в виде списков связностей
graph = {
'A': ['B'],
'B': ['A', 'C', 'D'],
'C': ['E', 'D', 'B'],
'D': ['B', 'C'],
'E': ['C']
}

graph_distances = {
'A': None,
'B': None,
'C': None,
'D': None,
'E': None
}

# Для каждой точки откуда мы в неё пришли
parents = {
'A': '',
'B': '',
'C': '',
'D': '',
'E': ''
}

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
# print(bfs(graph, 'D'))


def bfs_distances(graph, vertex_start):
    queue = deque() # Дек - очередь с двух сторон
    queue.append(vertex_start)
    graph_distances[vertex_start] = 0

    while queue: # Пока все вершины не обойдём
        vertex = queue.popleft()

        # Обход смежных вершин
        for u in graph[vertex]: # Идём по ключам текущей вершины
            if graph_distances[u] == None:
                graph_distances[u] = graph_distances[vertex] + 1
                queue.append(u)

    return graph_distances
# print(bfs_distances(graph, 'A'))

# Поиск родителя вершины
def bfs_parent(graph, vertex_start):
    queue = deque() # Дек - очередь с двух сторон
    queue.append(vertex_start)
    parents[vertex_start] = None

    while queue: # Пока все вершины не обойдём
        vertex = queue.popleft()

        # Обход смежных вершин
        for u in graph[vertex]: # Идём по ключам текущей вершины
            if parents[u] == '': # Если не известен родитель
                parents[u] = vertex # Сохраняем родителя для этой вершины
                queue.append(u)

    return parents
# print(bfs_parent(graph, 'A'))


# Восстановление кратчайшего пути по 2 вершинам
# Минимальный маршрут между 2мя вершинами
'''
Нужен будет словарь, хранящий предыдущие вершины
Нужно вызывать функцию bfs_parent
'''
def bfs_route(graph, vertex_start, vertex_finish):
    queue = deque() # Дек - очередь с двух сторон
    queue.append(vertex_start)
    parents[vertex_start] = None # У начальной вершины нет родителя

    while queue: # Пока все вершины не обойдём
        vertex = queue.popleft()

        # Обход смежных вершин (u)
        for u in graph[vertex]: # Идём по ключам текущей вершины
            if parents[u] == '': # Если у текущей смежной вершины не определен родитель
                parents[u] = vertex
                queue.append(u)

    return graph_distances
print(bfs_route(graph, 'A', 'D'))

'''
Задачи, что нужно также решить:
1) Подсчёт кол. компонент связностей
2) Восстановление кратчайшего пути по 2 вершинам - приступил
3) Нахождение всех ребер на кратчайшем пути
4) Задачи в телеграмм Флуд на фото
'''
#



# Эффективная реализация очереди - 2х связный список
# enqueue - вход в очередь
# dequeue - выход из очереди
