def BitnoicPoint(array):
    l = 0
    r = len(array)-1
    while l <= r:
        mid = (l+r) // 2
        print(array[mid-1],array[mid+1],array[mid])
        if array[mid-1] < array[mid] and array[mid] > array[mid+1]:
            return array[mid]
        elif array[mid-1] > array[mid]:
            r = mid - 1
        elif array[mid + 1] > array[mid]:
            l = mid + 1
    return -1
array = [1,3,8,12,4,2]
result = BitnoicPoint(array)
print(result) 

