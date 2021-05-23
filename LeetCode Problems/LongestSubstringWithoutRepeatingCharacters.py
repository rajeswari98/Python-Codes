s = "abcabcbb"
if not s:
    print(0)
d = {}
m = 0
j = 0
for i in range(len(s)):
    if s[i] in d and j <= d[s[i]]:
        j = d[s[i]]+1
    else:
        m = max(m, i-j+1)
    d[s[i]] = i
print(m)

'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Sol:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s =="":
            return 0
        di= {}
        j=0
        m=0
        for i,num in enumerate(s):
            if s[i] in di and j<=di[s[i]]:
                j = di[s[i]]+1
            else:
                m= max(m, i-j+1)
            di[s[i]] = i
        return m
'''
