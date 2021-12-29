import os
import heapq # Реализация очереди с приоритетом как минимальной кучи
from math import sqrt
# Задача - найти 3 точки максимально близкие к центру

os.system('cls')

def distanceToCenter(p, accuracy):
    # Теорема Пифагора. Нахожждение гипотенузы (расстояние до цнетра)
    len = sqrt(p[1]**2 + p[2]**2)
    return round(len, 2)

# Массив точек (каждый вложенный массив - точка, где 0 индекс - расстояние до центра, 1 - x, 2 - y)

# Точки (0 - непосчитанное растояние до центра)
p1 = [-1, 1, 1]
p2 = [-1, 3, 3]
p3 = [-1, 5, 5]
p4 = [-1, 10, 10]

# Вычисление расстояний до центра
p1[0] = distanceToCenter(p1, 2)
p2[0] = distanceToCenter(p2, 2)
p3[0] = distanceToCenter(p3, 2)
p4[0] = distanceToCenter(p4, 2)

heap = [ p1, p2, p3, p4 ]

heapq.heapify(heap)
print("Сформированная минимальная куча:")
print(heap)

pointsNearestToCenter = []

pointsNearestToCenter.extend(heapq.nsmallest(3, heap))

print(pointsNearestToCenter)

# Координаты точек наиближайших к центру
for i in pointsNearestToCenter:
    print("Координаты:")
    print("x = " + str(i[1]) + " y = " + str(i[2]))
    
