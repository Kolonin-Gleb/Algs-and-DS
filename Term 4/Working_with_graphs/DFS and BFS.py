# Дополнительная практика
# https://pimiento.github.io/python_graphs.html
# 
'''
Будет использоваться ненаправленный связный граф V=6 E=6.
Существует две популярные методики представления графов: матрица смежности (эффективна с плотными графами)
и список связей (эффективно с разряженными графами).

Плотный граф - граф, имеющий число ребер близкое к максимально возможному с его числом вершин.

Разряженный граф - граф, имеющий малое число ребер.

Будем использовать второй способ.
'''

# Граф в виде списков связностей
graph = {
'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A', 'F'],
'D': ['B'],
'E': ['B', 'F'],
'F': ['C', 'E']
}

# Поиск в глубину
def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited

# print(dfs(graph, 'A'))



# Поиск в ширину
from queue import deque
def bfs(graph, start):
    visited, queue = [], deque([start])
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.append(vertex)
            queue.extendleft(set(graph[vertex]) - set(visited))
    return visited

print(bfs(graph, 'A'))
