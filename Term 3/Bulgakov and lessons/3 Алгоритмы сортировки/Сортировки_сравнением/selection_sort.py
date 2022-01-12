# Сортировка выборками

def selection_sort(arr):

    for i in range(len(arr)): # Спринты по структуре данных
        min = i # 1 эл. принимаем за наименьший

        for j in range(i+1, len(arr)): # Непосредственная сортировка
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i] # Обмен мин. эл. в неотс. части с 1 эл. из из неотс. части
        # Переставляя мин. эл. в начало формируется отсортированная часть массива 
nums = [5, 7, 6, 9, 8, 2, 4, 3, 1]

selection_sort(nums)

print(nums)

