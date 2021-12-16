class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        str1, str2 = min(strs), max(strs)
        i=0
        while i < len(str1):
            if str1[i] != str2[i]:
                str1 = str1[:i]
            i=i+1
        return str1
        
c=Solution()
strs = list(map(str,input().split()))
print(c.longestCommonPrefix(strs))

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters
'''