def mergeL1Greater(s1, s2):
    l=[]
    smallLength = len(s2)
    for i in range(smallLength):
            l.append(s1[i])
            l.append(s2[i])
    for j in range(smallLength, len(s1)):
        l.append(s1[j])
    return l

def mergeL2Greater(s1, s2):
    l=[]
    smallLength = len(s1)
    for i in range(smallLength):
            l.append(s1[i])
            l.append(s2[i])
    for j in range(smallLength, len(s2)):
        l.append(s2[j])
    return l

def mergeStrings(str1, str2):
    l1= len(str1)
    l2 = len(str2)
    if l1 == l2:
        l=[]
        for i in range(len(str1)):
            l.append(str1[i])
            l.append(str2[i])
        return l
    elif l1>l2:
        res = mergeL1Greater(str1, str2)
        return res
    else:
        res = mergeL2Greater(str1, str2)
        return res
        
    

str1= "abc"
str2= "stuvwx"
finalRes = mergeStrings(str1, str2)
print(*finalRes, sep='')
#satbucvwx