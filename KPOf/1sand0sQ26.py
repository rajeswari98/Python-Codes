#Method 1
def maxSub(l):
    n = len(l)
    ones = 0
    zeros = 0
    res = 0
    for i in range(n):
        if l[i] == 0:
            ones = 0
            zeros += 1
            res = max(res, zeros)
        else:
            ones += 1
            zeros = 0
            res = max(res, ones)        
    return res

l = [0,1,1,1,1,1,0]
res=maxSub(l)
print(res)


#Method 2

# def maxSub(l):
#     n = len(l)
#     count = 0
#     max_value  = -1
#     for i in range(n):
#         if l[i] == 0:
#             if count>max_value:
#                 max_value = count
#             count = 0
#         elif i == n-1 and l[i] == 1:
#             count+=1
            
#             if count>max_value:
#                 max_value = count

#         elif l[i] == 1:
#             count  += 1
#     return max_value

# l = [0,1,1,1,1,1,0]
# res=maxSub(l)
# print(res)