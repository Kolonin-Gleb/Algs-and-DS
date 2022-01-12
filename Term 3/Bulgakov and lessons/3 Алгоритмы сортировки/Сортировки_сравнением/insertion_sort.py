# Сортировка вставками

def insertion_sort(arr):
        
    for i in range(len(arr)): # Спринты по структуре данных
        current = arr[i]
        position = i
        
        while position > 0 and arr[position - 1] > current:
            # Меняем местами число, продвигая по списку
            arr[position] = arr[position - 1]
            position -= 1
        # Остановимся и сделаем последний обмен
        arr[position] = current

    return arr

nums = [1, 4, 2, 3, 7, 5, 6, 8, 9, 0]

insertion_sort(nums)

print(nums)

