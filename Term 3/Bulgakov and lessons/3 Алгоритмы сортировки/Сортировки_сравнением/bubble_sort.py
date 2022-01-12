# # Сортировка пузырьком

def bubble_sort(arr):
    def swap(i, j): # Вложенная функция
        arr[i], arr[j] = arr[j], arr[i]

    count_elements = len(arr)
    mixed = True
    
    sprint_number = -1 # С каждым новым проходом по массиву 1 элемент будет ставиться точно на своё место
    while mixed:
        mixed = False
        sprint_number += 1
        for i in range(1, count_elements - sprint_number):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                mixed = True

nums = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]

bubble_sort(nums)

print(nums)


