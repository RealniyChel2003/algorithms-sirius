def binarySearch(arr, x, left = 0, right = None):
    if right == None: 
        right = len(arr)
    if right <= left: # данный промежуток пустой
        return -1
    # теперь промежуток не пустой
    mid = (left + right) // 2
    if arr[mid] == x: # центральный элемент — он искомый
        return mid
    elif x < arr[mid]: # искомый элемент меньше центрального
                       # значит следует искать в левой половине
        return binarySearch(arr, x, left, mid)
    else: # иначе следует искать в правой половине
        return binarySearch(arr, x, mid + 1, right)


arr = [1, 2, 5, 10, 17]
x = 0
index = binarySearch(arr, x)
print(index)