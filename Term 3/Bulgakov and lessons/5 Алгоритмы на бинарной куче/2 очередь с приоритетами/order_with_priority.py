import os
import heapq # Реализация очереди с приоритетом как минимальной кучи


os.system('cls')

# Массив, пока не куча
heap = [5, 8, 1, 23, 123, 31, 65, 56, 48]

# Формирование минимальной кучи (также очередь с приоритетом)
heapq.heapify(heap)
print("Минимальная куча:")
print(heap)
# При выводе:
# 1 - вершина кучи
# 8 и 5 - дети 1
# 23 и 123 - дети 8
# 31 и 65 - дети 5
# 56 и 48 - дети 23

heap.append(70)
print("Перестала быть кучей:")
print(heap)

print("Восстановление минимальной кучи:")
heapq.heapify(heap)
print(heap)

print("Удаление вершины кучи и автоматическое восстановление:")
heapq.heappop(heap)
print(heap)

print("Добавление элемента в кучу и автоматическое восстановление кучи:")
heapq.heappush(heap, -1)
print(heap)

arr = []
# Сделать из мин. кучи массив по возрастанию
def heapToArr(heap, arr):
    for i in range(len(heap)):
        arr.append(heapq.heappop(heap))

heapToArr(heap, arr)


print("Куча")
print(heap)

print("Массив из кучи")
print(arr)

