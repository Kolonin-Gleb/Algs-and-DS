import os

def heapify(array, n, i):
    root  = i
    left  = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and array[root] < array[left]:
        root = left
    if right < n and array[root] < array[right]:
        root = right

    if root != i:
        array[i], array[root] = array[root], array[i]
        heapify(array, n, root)

def heapSort(array):
    n = len(array)

    # построение пирамиды
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)

    # сама сортировка
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i] # отрываем корень и меняем местами с последним элементом
        heapify(array, i, 0)
    return array



os.system('cls')
arr = [5, 8, 1, 23, 123, 31, 65, 56, 48]
print(heapSort(arr))

