num=int(input("Enter the total no.of numbers: "))
l=[]
for _ in range(num-1):
    l.append(int(input()))
for i in range(num):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)

'''
input:

3
8
5
2

output:

[2, 3, 5, 8]
'''