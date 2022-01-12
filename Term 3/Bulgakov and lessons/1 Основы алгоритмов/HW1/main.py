def getMaxElem(arr): 
    currentMax = arr[0]
    for elem in arr:
        if elem > currentMax:
            currentMax = elem
    
    return currentMax

arr = [1, 3, 4, 5, 89, 12, 64]

print(getMaxElem(arr))

   
