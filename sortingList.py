#list sorting without the in-built functions
#ascending order

#using the in-built function
l=[3,2,6,4]
l.sort
print(l)

#list reverse
print(l[::-1])

#Time complexity O(N)
# l=[3,2,6,4]
# new_list =[]
# while l:
#     minimum = l[0]
#     for i in l:
#         if i < minimum:
#             minimum = i
#     new_list.append(minimum)
#     l.remove(minimum)
# print(new_list)



#list reverse using traditional method
# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if l[i]<l[j]:
#             temp=l[j]
#             l[j]=l[i]
#             l[i]=temp
# print(l)


#Time complexity O(N^2)
# l=[3,2,6,4]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             temp=l[i]
#             l[i]=l[j]
#             l[j]=temp
# print(l)
