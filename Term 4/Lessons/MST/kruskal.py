# Построение остовного дерева - алгоритм Краскала - простой
# Стал использоваться, после изобратения структуры данных DSU

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

# Формирование списка смежных вершин
def get_edges_list(graph):
    edges = []

    for vertex in graph:
        # Проход по смежным вершинам
        for neighbor in graph[vertex]: 

            # Если такого (обратного) ребра ещё нет, то добавляем
            if [graph[vertex][neighbor], neighbor, vertex] not in edges:
                edges.append([graph[vertex][neighbor], vertex, neighbor])

    return edges

# Функция формирования словаря вершин и их компонент связности
# Такой словарь нужен для поиска циклов в графе и формирования mst
def get_vertexes_dict(graph):
    vertexes_components = {}

    component_num = 0

    for vertex in graph:
        vertexes_components[vertex] = component_num
        component_num += 1
   
    return vertexes_components

# Вернуть список ребер, который даст минимальное дерево
def kraskal (start_vertex, G):
    mst = [] # Сформированное минимальное дерево

    edges = sorted(get_edges_list(graph)) # Сортировка вершин графа по весу
    vertexes_components = get_vertexes_dict(graph)

    # Перебираем отсортированные ребра
    for edge in edges:
        # print(edge) # [4, 'v3', 'v5']

        if vertexes_components[edge[1]] != vertexes_components[edge[2]]: # Если вершины формирующие ребро имеют разные компоненты связности

            # Определяем номер наименьшей компоненты связности
            comp_with_min_value = min(vertexes_components[edge[1]], vertexes_components[edge[2]])
            # Определяем номер наибольшей компоненты связности
            comp_with_max_value = max(vertexes_components[edge[1]], vertexes_components[edge[2]])

            # Находим все вершины с номером компоненты связности = компоненте связности с большим номером
            # в vertexes_components
            for vert in vertexes_components.keys():
                if vertexes_components[vert] == comp_with_max_value:
                    vertexes_components[vert] = comp_with_min_value # Меняем их на комп. связности с меньшим номером

            # 4 Добавляем ребро в дерево
            mst.append(edge)

            # Для просмотра процесса формирования дерева:
            # print("Полученное дерево" + str(mst))
            # print("Компоненты связности вершин графа" + str(vertexes_components))
            # print()

    return mst

print("Число ребер в полученном дереве = " + str(len(kraskal('v0', graph))))
print("Полученное дерево: " + str(kraskal('v0', graph)))

# Должно быть 7 ребер (v - 1)
# Верный ответ будет:
# [[4, 'v3', 'v5'], 
#  [7, 'v0', 'v2'], 
#  [7, 'v1', 'v7'],
#  [9, 'v0', 'v7'],
#  [10, 'v6', 'v7'],
#  [11, 'v3', 'v4'],
#  [22, 'v4', 'v7']
# ]