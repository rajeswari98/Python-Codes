def checkElement(arr):
    n = len(arr)
    visited = set()
    i=0
    while True:
        if i in visited:
            print(len(visited)+1)
            break
        visited.add(i)
        i=(arr[i]+i) % n

arr=  [2,4,3,0,1,1]
checkElement(arr)