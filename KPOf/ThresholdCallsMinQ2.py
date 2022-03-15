numCalls = [2,2,2,2,5,5,5,8]
alertThreshold = 4
preMin = 3

def NumOfAlerts(numCalls, alertThreshold, preMin):
        
    check = preMin
    l =[]
    for i in range(0,len(numCalls)+1):
        if len(numCalls[i:check]) == preMin:
            l.append(numCalls[i:check])
            check += 1

    # print(l, check)
    alert = 0
    for j in range(0, len(l)):
        if sum(l[j])/ preMin > alertThreshold:
            alert += 1
    return alert


RES = NumOfAlerts(numCalls, alertThreshold, preMin)
print(RES)

