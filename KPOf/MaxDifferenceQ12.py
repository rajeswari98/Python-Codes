def maxDifference(l):
    diffList = []
    for i in range(0,len(l)):
        for j in range(i+1, len(l)):
            diffList.append(l[j]-l[i])
    return max(diffList)
l = [1,2,6,4]
maxDifference(l)


# def maxDifference(l):
#     res = l[1] - l[0]
#     for i in range(0,len(l)):
#         for j in range(i+1, len(l)):
#             if l[j]-l[i] > res:
#                 res = l[j]- l[i]
#     return res
# l = [1,2,6,4]
# print(maxDifference(l))