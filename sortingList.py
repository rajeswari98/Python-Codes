#list sorting without the in-built functions
#ascending order
l=[3,2,6,4]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)

#using the in-built function
l.sort
print(l)

#list reverse
print(l[::-1])

#list reverse using traditional method
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i]<l[j]:
            temp=l[j]
            l[j]=l[i]
            l[i]=temp
print(l)


