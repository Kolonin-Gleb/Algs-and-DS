# Объяснить этот код, чтобы получить 10 баллов.



# Объяснение сортировки
# https://youtu.be/spoelATn2UI

# Пример реализации
# https://russianblogs.com/article/103441404/

# Топологическая сортировка позволяет представить запутанный граф в более понятном виде.
# C её помощью также можно понять, явл. ли граф Ациклическим

# Термины:
# Ациклический граф - граф имеющий циклы
# исток - вершина, имеющая только выходящие ребра
# сток - вершина, имеющая только входящие ребра

def TopologicalSort(graph):
    # Создание словаря степеней каждой вершины графа.
    # Вершина - ключ, значения их степеней по умолчанию = 0
    vertexes_degrees = dict( (vertex, 0) for vertex in graph )
    # print(vertexes_degrees) # Словарь

    # Вычисление степени каждого узла путём подсчёта кол. смежных с ней вершин
    for vertex in graph:
        for adjacent_vertex in graph[vertex]:
            # print(adjacent_vertex)
            vertexes_degrees[adjacent_vertex] += 1 # Увеличение значения по ключу в словаре


    # Создание очереди-списка и добавление в неё вершин со степенью 0
    queue = [vertex for vertex in graph if vertexes_degrees[vertex] == 0] # генератор
    topologically_sorted_graph = []

    # Пока в очереди есть вершины
    while queue:
        # Удаление вершин из головы очереди
        vertex = queue.pop()
        # Сохранение полученных вершин
        topologically_sorted_graph.append(vertex)

        # Удалить указатели, относящиеся к удаленным вершинам, 
        # Уменьшение степеней всех вершин, смежными с которыми была удаленная вершина на 1
        for adjacent_vertex in graph[vertex]:
            vertexes_degrees[adjacent_vertex] -= 1

        # Если степень вершины = 0, то она добавляется обратно в очередь
            if vertexes_degrees[adjacent_vertex] == 0:
                queue.append(adjacent_vertex)

    topologically_sorted_graph.reverse() # Порядок, в котором нужно проходить курсы

    return topologically_sorted_graph

Acyclic_graph = {
'a': ['b'],
'b': ['c'],
'c': ['h'],
'd': ['c'],
'e': ['d', 'g'],
'f': ['e'],
'g': ['c'],
'h': [],
}

Сyclic_graph = {
'a': ['b', 'c', 'd', 'e'],
'b': [],
'c': ['b', 'e'],
'd': ['c'],
'e': ['b', 'd']
}

Unlinked_graph = {
    '1': ['2', '3'],
    '2': [],
    '3': [],
    '4': []
}

print(TopologicalSort(Acyclic_graph)) # ['h', 'c', 'b', 'a', 'd', 'g', 'e', 'f'] - correct

print(TopologicalSort(Сyclic_graph)) # ['a'] - Удалось убрать только 1 вершину

print(TopologicalSort(Unlinked_graph)) # ['2', '3', '1', '4'] - correct
