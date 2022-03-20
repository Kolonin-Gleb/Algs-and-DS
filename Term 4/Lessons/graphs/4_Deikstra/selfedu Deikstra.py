# Объяснение: https://youtu.be/MCfjc_UIP1M

# Алгоритм дейкстры 
'''
Позволяет найти наикратчайшее расстояние от заданной вершины до всех остальных вершин в графе.
Он работает только, если ребра графа имеют положительные значения
'''

# 10:45 - начало реализации на python
# 12:20 - объяснение кода

#########################

import math

# Получение списка смежных вершин
def get_adjacent_vertixes(cur_vertex, graph):
    # graph[cur_vertex] - строка из матрицы смежностей
    for vertex_num, weight in enumerate(graph[cur_vertex]):
        if weight > 0:
            yield vertex_num # yeild - возвращает по одной вершине, но вернет в итоге все

# Функция поиска вершины к которой путь - минимальный
def get_num_vertex_min_route(table_last_row, visited_vertexes):
    amin = -1
    m = max(table_last_row)  # максимальное значение из таблицы
    for i, t in enumerate(table_last_row):
        # Поиск вершины с минимальным путем из тех, что ещё не рассмотрены
        if t < m and i not in visited_vertexes:
            m = t
            amin = i

    return amin

##########################################################################################


# Матрица смежностей графа в виде кортежа
# Чтобы граф нельзя было изменить
graph = (
    (0, 3, 1, 3, 0, 0),
    (3, 0, 4, 0, 0, 0),
    (1, 4, 0, 0, 7, 5),
    (3, 0, 0, 0, 0, 2),
    (0, 0, 7, 0, 0, 4),
    (0, 0, 5, 2, 4, 0)
)

# Число вершин в графе
vertexes_count = len(graph)
# Последняя строка таблицы, что хранит расстояния до вершин из начальной вершины (Согласно визуализации алгоритма)
table_last_row = [math.inf]*vertexes_count
# Текущая (стартовая) вершина (нумерация с нуля)
cur_vertex = 0
# Просмотренные вершины. Хранятся в множестве
visited_vertexes = {cur_vertex}
# Нулевой вес для стартовой вершины
table_last_row[cur_vertex] = 0

while cur_vertex != -1: # Пока не просмотрим все вершины
    for adj_vertex_num in get_adjacent_vertixes(cur_vertex, graph): # Перебор всех смежных вершин
        if adj_vertex_num not in visited_vertexes:                  # Если вершина еще не просмотрена
            vertex_route = table_last_row[cur_vertex] + graph[cur_vertex][adj_vertex_num] # Определение пути до вершины bиз тек. вершины
            # Обновление длины пути до вершины только, если найденный вариант короче уже обнаруженного
            if vertex_route < table_last_row[adj_vertex_num]: 
                table_last_row[adj_vertex_num] = vertex_route

    # Выбор вершины, до которой меньше всего идти от нач. вершины для продолжения алгоритма
    cur_vertex = get_num_vertex_min_route(table_last_row, visited_vertexes)

    if cur_vertex >= 0: # Удалось выбрать очередную вершину, которая ещё не рассматривалась
        visited_vertexes.add(cur_vertex) # Добавляем новую вершину на рассмотрение

print(table_last_row)
