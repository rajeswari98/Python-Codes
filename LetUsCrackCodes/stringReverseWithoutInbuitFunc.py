s = input()
k=''
for i in range(len(s)-1, 0, -1):
    k = k + s[i]

print(k)


#inbuit FUnctions
# method 1
# s=input()
# print(s[::-1])


#method 2
# s = input()
# k=[]
# for i in s:
#     k.insert(0,i)

# print(''.join(k))


# method 3
# s = input()
# k = list(reversed(s))
# print(''.join(k))