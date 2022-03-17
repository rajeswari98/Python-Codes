#Referring Josephs algorithm based 
#Method 1
#Time Complexity is O(n)

def classPresident(num, k):
    if num == 1:
        return 1
    else: 
        return (classPresident(num-1, k)+ k-1) % num+ 1
arr= [1,2,3,4]
k=2
l = len(arr)


IndexValue = classPresident(l, k)
print(arr[IndexValue-1])