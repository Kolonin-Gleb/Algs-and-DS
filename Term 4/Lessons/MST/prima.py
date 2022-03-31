# Построение остовного дерева - алгоритм Прима - простой

import math

graph = {
    'v0': {'v2': 7, 'v5':26, 'v6':20, 'v7':9, 'v1': 10},
    'v1': {'v0': 10, 'v7': 7},
    'v2': {'v0': 7},
    'v3': {'v4': 11, 'v5': 4},
    'v4': {'v6': 30, 'v7': 22, 'v3': 11, 'v5': 15},
    'v5': {'v0': 26, 'v3': 4, 'v4': 15},
    'v6': {'v0': 20, 'v4': 30, 'v7': 10},
    'v7': {'v0': 9, 'v1': 7, 'v4': 22, 'v6': 10}
}

# Вернуть список ребер, который даст минимальное дерево
def prima (start_vertex, G):

    # Вершины сформированного дерева.
    formed_tree = [] 
    formed_tree.append(start_vertex)

    # Вершина, к которой будет производиться присоединение
    connector_vertex = start_vertex
    # Присоединяемая ближайшая вершина
    nearest_vertex = ''
    # Расстояние до ближайшей вершины
    nearest_vertex_distance = math.inf

    not_tree = []  # Вершины, что ещё не стали частью дерева
    # Добавляем все вершины, что ещё не стали частью дерева
    for v in G:
        not_tree.append(v)
    not_tree.pop(0)

    while len(not_tree) != 0: # Пока все вершины не стали частью дерева

        # Перебор всех вершин, что уже являются деревом
        for cur_vertex in formed_tree:

            # Поиск наиближайшей вершины к любой вершине дерева

            # Поиск ближайшей вершины к cur_vertex, что ещё не в дереве
            for neighbor in G[cur_vertex]: # Получение смежных с cur_vertex вершин

                # Если смежная вершина не в дереве
                if (neighbor not in formed_tree):
                    # Если эта вершина ближе, тех, что были рассматрены
                    if nearest_vertex_distance > graph[cur_vertex][neighbor]:
                        # Определена новая ближайшая вершина
                        nearest_vertex = neighbor
                        # Откуда идти к ближайшей вершине
                        connector_vertex = cur_vertex 
                        # Сколько идти к ближайшей вершине
                        nearest_vertex_distance = graph[cur_vertex][neighbor]

        # Добавление наиближайшей вершины к любой вершине дерева в дерево
        formed_tree.append(nearest_vertex)
        not_tree.pop(not_tree.index(nearest_vertex))

        # Имеющееся дерево
        print(formed_tree)  
        # Вывод ребра дерева
        print(connector_vertex + nearest_vertex)

        # Подготовка к новому поиску

        # Вершина, к которой будет производиться присоединение
        connector_vertex = start_vertex
        # Присоединяемая ближайшая вершина
        nearest_vertex = ''
        # Расстояние до ближайшей вершины
        nearest_vertex_distance = math.inf

# Должно быть 7 ребер (v - 1)
prima('v0', graph)

