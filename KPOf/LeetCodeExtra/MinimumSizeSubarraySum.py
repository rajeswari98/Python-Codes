# https://leetcode.com/problems/minimum-size-subarray-sum/
#TimeComplexity is O(N)
def minSubArrayLen(target, nums):
        l = len(nums)
        left = 0
        total = 0
        min_length = l+1
        for right in range(l):
            total += nums[right]
            while total>= target:
                cur_length = right-left +1
                min_length = min(min_length, cur_length)
                total -= nums[left]
                left += 1
        if min_length<=l:
            return min_length
        else:
            return 0

target = 7
nums = [2,3,1,2,4,3]
res=minSubArrayLen(target, nums)
print(res)


# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0