# Граф ориентированный, т.к. обмены происходят в одну сторону
# вершины - валюты
# ребра - курсы обмена

# print(currencies_exchange['Rub']) # Получение значения по ключу (ещё 1 словарь)
# print(currencies_exchange['Rub']['Dollar']) # цена конвертации в соседнюю валюту

from cmath import inf
from collections import deque

# С данным графом обмен туда обратно не выгоден.
currencies_exchange = {
    'Rub': {'Dollar':0.0096, 'Euro':0.0087, 'GPB':0.0072},
    'Dollar':{'Rub':100.9, 'Euro':0.9, 'GPB':0.75},
    'Euro':{'Rub':110.5, 'Dollar':1.1, 'GPB':0.83},
    'GPB':{'Rub':135, 'Dollar':0.7, 'Euro':0.83}
}

# С данным графом меняя валюту можно получить больше, чем было из-за ('Dollar':2.1)
currencies_exchange_anomaly = {
    'Rub': {'Dollar':0.0096, 'Euro':0.0087, 'GPB':0.0072},
    'Dollar':{'Rub':100.9, 'Euro':0.9, 'GPB':0.75},
    'Euro':{'Rub':110.5, 'Dollar':2.1, 'GPB':0.83},
    'GPB':{'Rub':135, 'Dollar':0.7, 'Euro':0.83}
}

'''
Этот код выдаёт максимальные суммы денег, которые можно получить 
конвертацией исходной валюты во все остальные валюты.
'''
def deikstra (start_vertex, money, G):
    distances = {} # расстояние от начальной вершины
    distances[start_vertex] = money # Переводим 1 условную единицу (Сумма входной валюты)

    queue = deque() # Стек = очередь с 2х сторон
    queue.append(start_vertex)

    while queue:
        cur_vertex = queue.popleft()

        for neighbor in G[cur_vertex]: # Получение смежных с данной вершин

            # Если расстояние до смежной вершины не определено
            if (neighbor not in distances):
                distances[neighbor] = distances[cur_vertex] * G[cur_vertex][neighbor] # Конвертация в другую валюту
                queue.append(neighbor) # Полученную валюту также нужно попробовать конвертировать

            # ИЛИ если расстояние до смежной вершины найдено больше (более выгодная конвертация)
            elif (distances[cur_vertex] * G[cur_vertex][neighbor] > distances[neighbor]):
                distances[neighbor] = distances[cur_vertex] * G[cur_vertex][neighbor]
                queue.append(neighbor)
    return distances # Расстояния - результаты перевода денег

currency = 'Rub'
money = 1
desired_currency = 'GPB'
best_transaction_result = 0

# Можно ли получить больше денег, чем имеется? # currencies_exchange_anomaly - будет аномалия
max_results = deikstra(currency, money, currencies_exchange)
for key in max_results:
    if max_results[key] == inf:
        print("Аномалия! Конвертируя деньги можно получить больше, чем имеется!")
        exit()

# Результат самой выгодной конвертации в заданную валюту
print(f"Из {money} {currency} можно получить максимум {max_results[desired_currency]} {desired_currency}")
print("Для этого нужно сделать следующие конвертации")


