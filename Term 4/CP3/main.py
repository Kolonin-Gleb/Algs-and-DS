# Топологическая сортировка

# Граф представляющий последовательность изучения курсов

# Граф в виде списков связностей
graph = {
'A': ['B'],
'B': ['C'],
'C': ['H'],
'D': ['C'],
'E': ['D', 'G'],
'F': ['E'],
'G': ['C'],
'H': [],
}

# Поиск в глубину
# def dfs(graph, start):
#     visited, stack = [], [start] # visited - серых
# черные - для них закончили рекурсию
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.append(vertex)
#             stack.extend(set(graph[vertex]) - set(visited))
#     return visited

# print(dfs(graph, 'A'))

'''
Сделать добавление вершин, для которых закончилась рекурсия в конец списка.
При выводе ответа выводим список в обратном порядке.
'''

# В моём случае белые вершины - это все вершины графа, с которыми не работала функция.
# Серые вершины - в списке visited
# Чёрные вершины - те, для которых закончилась рекурсия


def topological_sort(graph, start):
    visited, stack = [], [start] # visited - серых
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited

# print(topological_sort(graph, 'A'))

black_vertices = topological_sort(graph, 'A')

print("Возможная последовательность изучения курсов:")
print(black_vertices[::-1])


# Определить одну из возможных последовательностей изучения курсов
# Необходимо сформировать список - последовательность посещенных вершин
# Можно сделать с удалением

