# Граф ориентированный, т.к. обмены происходят в одну сторону
# 
# вершины - валюты
# ребра - курсы обмена
# 

'''
Мой план по решению этой КТ:
'''

from collections import deque

# С данным графом обмен туда обратно не выгоден.
currencies_exchange = {
    'Rub': {'Dollar':0.0096, 'Euro':0.0087, 'GPB':0.0072},
    'Dollar':{'Rub':100.9, 'Euro':0.9, 'GPB':0.75},
    'Euro':{'Rub':110.5, 'Dollar':1.1, 'GPB':0.83},
    'GPB':{'Rub':135, 'Dollar':0.7, 'Euro':0.83}
}

def deikstra (start_vertex, G):
    distances = {} # расстояние от начальной вершины
    distances[start_vertex] = 0

    queue = deque()
    queue.append(start_vertex)

    while queue:
        cur_vertex = queue.popleft()

        for neighbor in G[cur_vertex]:
            if (neighbor not in distances
                or distances[cur_vertex] + G[cur_vertex][neighbor] < distances[neighbor]):
                distances[neighbor] = distances[cur_vertex] + G[cur_vertex][neighbor]
                queue.append(neighbor)
    return distances

# Я получу строку таблицы, которая будет соответствовать результату конвертации заданной валюты во все остальные валюты.
print(deikstra('Rub', currencies_exchange))

your_currency = 'Rub'
desired_currency = 'GPB'

print()





