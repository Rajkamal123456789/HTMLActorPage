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

# def equblirum(array):
#     total_sum = 0
#     left_sum = 0

#     for i in array:
#         total_sum += i

#     for i in array:
#         total_sum -= i
#         if total_sum == left_sum:
#             return i
#         left_sum += i
#     return "Given array there is no equalbrium number is present."
# # array = [3,4,9,6,1]
# # array = [1,2,3,4,6,10]
# # array = [0,1,1]
# result = equblirum(array)
# print(result)

# def subset(array1,array2):
#     i = 0
#     j = 0
#     while i < len(array1) and j < len(array2):
#         if array1[i] == array2[j]:
#             i += 1
#             j += 1
#         elif array1[i] < array2[j]:
#             i += 1
#         else:
#             return False
#     return True

# array1 = [1,2,3,4,5]
# array2 = [2,4,5]
# result = subset(array1,array2)
# print(result)

# def unique(array):
#     out = 0
#     for i in array:
#         out = out ^ i
#     return out
# array = [4,2,5,2,4]
# result = unique(array)
# print("Result:",result)

def missign_number(array):
    n = len(array)
    print(type(n),n)
    to_add = n*(n+1)//2
    from_add = 0
    for i in array:
        from_add += i
    return to_add - from_add
array = [0,1,3,4]
result = missign_number(array)
print("Result:",result)

