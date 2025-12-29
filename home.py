# def BitnoicPoint(array):
#     l = 0
#     r = len(array)-1
#     while l <= r:
#         mid = (l+r) // 2
#         print(array[mid-1],array[mid+1],array[mid])
#         if array[mid-1] < array[mid] and array[mid] > array[mid+1]:
#             return array[mid]
#         elif array[mid-1] > array[mid]:
#             r = mid - 1
#         elif array[mid + 1] > array[mid]:
#             l = mid + 1
#     return -1
# array = [1,3,8,12,4,2]
# result = BitnoicPoint(array)
# print(result) 

def equblirum(array):
    total_sum = 0
    left_sum = 0

    for i in array:
        total_sum += i

    for i in array:
        total_sum -= i
        if total_sum == left_sum:
            return i
        left_sum += i
    return "Given array there is no equalbrium number is present."
# array = [3,4,9,6,1]
# array = [1,2,3,4,6,10]
array = [0,1,1]
result = equblirum(array)
print(result)

