# # # Сортировка пузырьком

# def bubble_sort(arr):
#     def swap(i, j): # Вложенная функция
#         arr[i], arr[j] = arr[j], arr[i]

#     count_elements = len(arr)
#     mixed = True
    
#     sprint_number = -1 # С каждым новым проходом по массиву 1 элемент будет ставиться точно на своё место
#     while mixed:
#         mixed = False
#         sprint_number += 1
#         for i in range(1, count_elements - sprint_number):
#             if arr[i - 1] > arr[i]:
#                 swap(i - 1, i)
#                 mixed = True

# nums = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# bubble_sort(nums)

# print(nums)

def shaker_sort(array): 
    length = len(array) 
    swapped = True
    start_index = 0
    end_index = length - 1
    
    while (swapped == True): 
        
        swapped = False
          
        # проход слева направо
        for i in range(start_index, end_index): 
            if (array[i] > array[i + 1]) : 
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i] 
                swapped = True
  
        # если не было обменов прерываем цикл
        if (not(swapped)): 
            break

        swapped = False

        end_index = end_index - 1
  
        #проход справа налево
        for i in range(end_index - 1, start_index - 1, -1): 
            if (array[i] > array[i + 1]): 
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i] 
                swapped = True
 
        start_index = start_index + 1

print("Шейкерная сортировка")
arr = []
length = int(input("Введите длину массива: ")) 
for i in range(0, length): 
    element = int(input("arr[" + str(i + 1) + "] = "))   
    arr.append(element)
shaker_sort(arr) 
print("Отсортированный массив: ") 
print(arr)

