import math # Для реализации графа с исп. таблицы с бесконечными значениями

# Объяснение: https://youtu.be/MCfjc_UIP1M
# Алгоритма Дейкстры




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

# С данным графом обмен туда обратно не выгоден.
currencies_exchange = {
    'Rub': {'Dollar':0.0096, 'Euro':0.0087, 'GPB':0.0072},
    'Dollar':{'Rub':100.9, 'Euro':0.9, 'GPB':0.75},
    'Euro':{'Rub':110.5, 'Dollar':1.1, 'GPB':0.83},
    'GPB':{'Rub':135, 'Dollar':0.7, 'Euro':0.83}
}