# second smallest element in the array

#Method 1
arr = [3,7,12,1,2]
for i in range(len(arr)):
    for j in range(i , len(arr)):
        if arr[i]>arr[j]:
            temp =arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr[1])

#Method 2
# arr = [3,7,12,1,2]
# arr.sort()
# print(arr[1])