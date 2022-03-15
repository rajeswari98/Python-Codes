arr= [4,2,8,1]

#Method 1
print(min(arr), max(arr))

#Method 2(Without using  in-built functions)
temp=0
small = arr[0]
for i in arr:
    if i>temp:
        temp=i 
    if small>i:
        small=i
print("Max number is:",temp)
print("Min number is:",small)

#Method 3
arr.sort()
print("Max Number", arr[-1])
print("Min Number", arr[0])
