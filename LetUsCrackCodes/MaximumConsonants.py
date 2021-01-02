string=input().split()
vow='aeiou'
l=[]
count=0
for i in string:
    if i in vow:
        count+=1
        l.append(i)
print(l)