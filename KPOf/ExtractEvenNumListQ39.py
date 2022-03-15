l = [1,2,3,4,5,6,7,8,9,10]

#Method 1
for i in range(0,len(l)):
    if l[i]%2==0: print(l[i])

#Method 2
print([l[i] for i in range(0,len(l)) if l[i]%2==0])

#Method 3
print(list(filter(lambda x: (x%2==0), l )))