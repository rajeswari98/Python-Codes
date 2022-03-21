def max_sub(l):
    max_sum = 0
    val = 0
    for i in l:
        val = val + i
        val = max(val, 0)
        max_sum = max(max_sum, val)
    return max_sum
arr=[1,-5, 6 , -10 ,9,-4,-7]
print(max_sub(arr))


# def maxSubsetSum(arr):
#     dp = {} # key : max index of subarray, value = sum
#     dp[0] = arr[0]
#     dp[1] = max(arr[0], arr[1])

#     for i, num in enumerate(arr[2:], start=2):
#         # print(i,num)
#         dp[i] = max(dp[i-1], dp[i-2]+num, dp[i-2], num)
#     print(dp)
#     return dp[len(arr)-1]

# arr=[1,-5, 6 , -10 ,9,-4,-7]
# print(maxSubsetSum(arr))

# def subsets(arr):
#     lists = [[]]
#     for i in range(len(arr)+1):
#         for j in range(i):
#             lists.append(arr[j:i])
#     # print(lists)
#     return lists

# def maxSubsetSum(arr):
#     subsetLists = subsets(arr)
#     # print(subsetLists)
#     maxArr=[]
#     temp=-99999999
#     for i in subsetLists:
#         # print(i)
#         # print(sum(i))
#         if sum(i) > temp :
#             # print(temp, sum(i))
#             temp=sum(i)
#             print(i, sum(i), temp)
#     print(temp)
    
# arr=[1,-5, 6 , -10 ,9,-4,-7]
# maxSubsetSum(arr)