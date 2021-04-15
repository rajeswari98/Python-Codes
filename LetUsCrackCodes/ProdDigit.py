# Write the product of all the digits in the given number

num = int(input())
temp = 1
k = 1
while(num != 0):
    k = num % 10
    temp = temp*k
    num = num//10
print(temp)

'''
a = input()
res = 1
for i in a:
    res = res*(int(i))
print(res)
'''
