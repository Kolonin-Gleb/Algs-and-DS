# Количество маршрутов в графе

'''
# # Получение ключа по значению в словаре
# def get_key(d, value):
#     for k, v in d.items():
#         if v == value:
#             return k
#
# # Печать всех смежных вершин
# def print_adjacent_vert(arr, v, index):
#     for row in range(len(v)):
#         for connection in range(len(v)):
#             if arr[row][connection] == 1: # Вершины - смежные
#                 print(str(get_key(index, row)) + " -> " + str(get_key(index, connection)))
'''

# Граф в виде матрицы смежностей:
# исходящая стрелка - значение в строке
# входящее стрелка  - значение в столбце
v = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
index = {v[i]: i for i in range(len(v))} # Словарь для нумерации вершин числами
arr = [
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
]

# Данная функция находит кол. способов добраться из нач. вершины в каждую!
# Но если я захочу найти кол. способов добраться из заданной вершины в заданную, то она мне не поможет.
def graph_path():
    path = [1] # База. В начальную вершину 1 маршрут.

    for i in range(1, len(v)):
        res = 0 # Число способов добраться до каждой вершины
        for j in range(0, len(v)):
            if arr[j][i] == 1: # Идём по столбцу, начиная с 0 строки 1 столбца. # 0 столбец пропускается, т.к. для 1 вершины А уже задана база
                res += path[j] # Прибавляем кол. способов добраться до той вершины из которой можно добраться в текущую
        path.append(res)
    return path

print(graph_path())

# print_adjacent_vert(arr, v, index)

# Кол. способов добраться из A в G

# start_vertex = 'A'
# end_vertex = 'G'

# for row in range(len(v)):
#     for connection in range(len(v)):
#         if arr[row][connection] == 1: # Вершины - смежные
#             print(str(get_key(index, row)) + " -> " + str(get_key(index, connection)))


#TODO:
'''
По итогу я разобрался как работает алгоритм выше.
Мои закомментированные наброски кода могут усовершенствовать алгоритм.
Оставлю это до лучших времён.
'''

'''
TODO: Что можно улучшить?
0) Мне интересно оформить решение задачи в виде отдельной функции, в которую:
- Подаётся граф в виде v, index, arr
- Подаётся нач. вершина
- Подаётся кон. вершина
-- Возращает число маршрутов из нач. в кон.

1) Решить эту задачу с исп. рекурсии, а не сохранения маршрутов до каждой вершины в пути к финишу

2) Мне интересно написать код для восстановления ответа
- Какие именно маршруты ведут из нач. в кон. вершины

3) Решить эту же задачу на неациклическом, не направленном графе.
'''
