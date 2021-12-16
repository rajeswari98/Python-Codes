class Solution:
    def reverse(self, x: int) -> int:
        rev_x = int(str(abs(x))[::-1])
        
        if x > 0:
            if rev_x <= 2**31 - 1:
                return rev_x
        else:
            if -2**31 - 1 <= -rev_x:
                return -rev_x
        return 0

s= Solution()
x=int(input())
print(s.reverse(x))



'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
'''