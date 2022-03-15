# s= input()
# step =int(input()) 

s="abcde"
step = 3
length = len(s)

res = [s[i:i+step] for i in range(len(s))]
newRes = []
for i in res:
    if len(i)!=step:
        res.remove(i)
    else:
        newRes.append(i)
print(newRes)