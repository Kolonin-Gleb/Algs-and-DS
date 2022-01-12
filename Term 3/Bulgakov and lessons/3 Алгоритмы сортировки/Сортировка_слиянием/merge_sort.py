def merge_sort(arr, first, last): # Декомпозирует с.д.
    mid = len(first + last) / 2
    
    merge_sort(arr, first, mid)
    merge_sort(arr, mid+1, last)
    merge(arr, first, mid, last)


def merge(arr, first, mid, last): # Собирает с.д.
    
    return None # Возращаем новый массив, что мы сформировали

    

nums = [0, 4, 3, 2, 7, 8, 9, 6, 5, 1]

merge_sort(nums)

print(nums)

