# Различная реализация и вывод неориентированного графа в python
# Разными способами

# 1 Способ Глеб

# v = {'A', 'B', 'C', 'D'} # Множество вершин
# e = {('A', 'B'), ('B', 'C'), ('C', 'D')} # Множество ребер

# print(v)

# # Вывод смежных вершин для каждой вершины
# for vertex1 in v:
#     edges_for_vertex = []
#     for vertex2 in v:
#         for edge in e:
#             if edge == (vertex1, vertex2) or edge == (vertex2, vertex1):
#                 edges_for_vertex.append(vertex2)
#     print(str(vertex1) + ' : ' + str(edges_for_vertex))
# #

# 1 Способ Игорь

# from pprint import pprint
# def main():
#     v = ['A', 'B', 'C', 'D', 'E']
#     r = [('A', 'B'), ('A', 'E'), ('C', 'B'), ('D', 'B'), ('E', 'C'), ('D', 'E')]

#     result = {i: [] for i in v}
#     for edge in r:
#         for tot in edge:
#             for tot2 in edge:
#                 if tot != tot2 and tot2 not in result[tot]:
#                     result[tot] += [tot2]
#     pprint(result)

# main()

# 2 Способ Игорь

# def main():
#     v = ['A', 'B', 'C', 'D', 'E']
#     index = {v[i]: i for i in range(len(v))}
#     arr = [
#         [0, 1, 0, 0, 1],
#         [1, 0, 1, 1, 0],
#         [0, 1, 0, 0, 1],
#         [0, 1, 0, 0, 1],
#         [1, 0, 1, 1, 0],
#     ]
#     for tot in v:
#         tots = []
#         row = arr[index[tot]]
#         for s_index in range(len(row)):
#             if row[s_index]:
#                 tots.append(v[s_index])
#         print(tot, ":", tots)


# main()

# 1 Способ Софии

# v = {'A', 'B', 'C', 'D'}
# e = {('A', 'B'), ('B', 'C'), ('C', 'D')}


# def find_edj(ver):
#     ver_ar = []
#     for i in e:
#         if (i[0] == ver or i[1] == ver):
#             ver_id = i.index(ver)
#             ver_ar.append(i[1-ver_id])
            
#     print(f'{ver}: {ver_ar}')
# for ver in v:
#     find_edj(ver)



# TODO: Реализуй 3 способ. Разбирись, как делать 2 способ


# # v = {'A', 'B', 'C', 'D'} # Множество вершин
# e = {('A', 'B'), ('B', 'C'), ('C', 'D')} # Множество ребер



'''
Обход в глубину на следующем уроке 

На следующем уроке рекурсия обхода в глубину
'''

