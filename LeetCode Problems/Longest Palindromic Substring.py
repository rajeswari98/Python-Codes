class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        count = 0
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > count:
                    count = right - left + 1
                    result = s[left: right + 1]
                left, right = left -1, right + 1
            
            left , right = i, i+ 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > count:
                    count = right - left + 1
                    result = s[left: right + 1] 
                left, right = left -1, right + 1
        return result

func=Solution()
s=input()
print(func.longestPalindrome(s))

'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''