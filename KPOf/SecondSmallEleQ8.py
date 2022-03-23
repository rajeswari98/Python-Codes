# second smallest element in the array


l = [3,7,12,1,1,2]
def findSmallest(l):
    small_num=l[0]
    for i in l:
        if small_num>i:
            small_num = i
    return small_num

small = findSmallest(l)

second = l[0]
for i in range(0,len(l)):
    if l[i]!=small and second>l[i]:
        second=l[i]
print(second)


#Method 2 brute force O(N^2)
# arr = [3,7,12,1,2]
# for i in range(len(arr)):
#     for j in range(i , len(arr)):
#         if arr[i]>arr[j]:
#             temp =arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
# print(arr[1])

#Method 3
# arr = [3,7,12,1,2]
# arr.sort()
# print(arr[1])