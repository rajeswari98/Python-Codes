'''
nums = [3, 3]
target = 6
k = []
for i in range(len(nums)-1):
    j = i+1
    if nums[i]+nums[j] == target:
        j = i+1
        print("[{},{}]".format(i, j))
'''
# Solution:


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = []
        for i in range(len(nums)-1):
            j = i+1
            if nums[i]+nums[j] == target:
                j = i+1
                # print("[{},{}]".format(i,j))
                return i, j


'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
Accepted
4,108,847
Submissions
8,790,804
Seen this question in a real interview before?

Yes

No
A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions for just for completeness. It is from these brute force solutions that you can come up with optimizations.
So, if we fix one of the numbers, say
x
, we have to scan the entire array to find the next number
y
which is
value - x
where value is the input parameter. Can we change our array somehow so that this search becomes faster?
The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?
'''
