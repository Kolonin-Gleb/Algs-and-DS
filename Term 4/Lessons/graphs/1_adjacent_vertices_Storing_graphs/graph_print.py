# Различная реализация и вывод неориентированного графа в python

# 1 Способ 
# Неорентированный граф в виде множества вершин и множества кортежей ребер
# Получение смежных вершин для каждой вершины
'''
v = {'A', 'B', 'C', 'D'}
e = {('A', 'B'), ('B', 'C'), ('C', 'D')}
# print(v) - множества хранятся в случайном порядке

# # Вывод смежных вершин для каждой вершины
for vertex1 in v:
    adjacent_vertices = [] # Список смежных вершин для текущей вершины
    for vertex2 in v:
        for edge in e:
            if edge == (vertex1, vertex2) or edge == (vertex2, vertex1):
                adjacent_vertices.append(vertex2)
    print(str(vertex1) + ' : ' + str(adjacent_vertices))
# #
'''

# 2 Способ 
# Неорентированный граф в виде множества вершин и матрицы смежностей
# Получение смежных вершин для каждой вершины
'''
v = ['A', 'B', 'C', 'D', 'E']
Adjacency_matrix = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
]

# Содержит пары вершина и индекс её строки/столбца в матрице
indexes = {v[i]: i for i in range(len(v))}

for vertex in v:
    # Список смежных вершин для текущей вершины
    adjacent_vertices = []
    # Чтение матрицы смежности по строкам
    row = Adjacency_matrix[indexes[vertex]]
    for connection_index in range(len(row)):
        if row[connection_index]: # Если присутствует связь
            adjacent_vertices.append(v[connection_index]) # Добавление смежной вершины
    print(vertex, " : ", adjacent_vertices)
'''

# 3 Способ
# Неорентированный граф в виде множества вершин и множества кортежей ребер
# Получение матрицы смежностей графа


# Считываем список ребер и списки смежности в матрицу смежностей
# Ввод: vertexes_count - кол-во вершин edges_count - кол-во ребер
# Вывод: edges_count - строк кода в виде "A B"

print("\n\nВвод графа")
vertexes_count = int(input("Введите кол-во вершин в графе: "))
edges_count = int(input("Введите кол-во ребер в графе: "))


vertexes = [] # массив вершин
index = {} # пустой словарь под индексы

arr = [[0] * vertexes_count for _ in range(vertexes_count)]
print(arr)
G = {}

for _ in range(vertexes_count): # Обработка всех вершин
    v1, v2 = input().split()

    for u1, u2 in (v1, v2), (v2, v1): # список
        if u1 not in G:
            G[u1]= {u2}
        else:
            G[u1].add(u2)

    for v in v1, v2:
        if v not in index:
            vertexes.appent(v)
            index[v] = len(vertexes) - 1
        v1_i = index[v1]
        v2_i = index[v2]
        arr[v1_i][v2_i] = 1
        arr[v2_i][v1_i] = 1

print(vertexes)
print(arr)
print(G)

