'''
sub = "0001110101"
l = 3
'''

sub = "1000011"
l = 5
'''
a = []
for i in range(len(sub)):
    p = 0
    if l > p:
        a.append(int(sub[i]))
        p = p+1
print(a)

k = len(a)//l
finalRem = len(a) - l
# print(k)
res = []
sum = 0
for j in range(1, len(a)):
    if k > j:
        sum = sum+a[j]
        print(k, j, sum, a[j])
    else:
        res.append(sum)
        k = k+l
        sum = 0
        sum = sum+a[j]
t = []
x = -1
print(finalRem)

while finalRem:
    t.append(a[x])
    x = x-1
    finalRem = finalRem-1
tot = 0
for b in t:
    tot = tot+b
arrRes = max(res)
print(res, max(arrRes, tot))
'''
k = input()
s = input()
news = ''
l = len(k)+len(s)
c = 0
for i in range(l):
    if i % 2 == 0:
        news = news+k[c]
        c = c+1
    else:
        news = news+s[c]
        c = c+1
print(news)
