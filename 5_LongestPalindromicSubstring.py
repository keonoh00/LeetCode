# Given a string s, return the longest palindromic substring in s.

# Brute Force Approach
class Solution:
    def longestPalindrome(self, s: str) -> str:
        diction = dict()
        if len(s) == 1:
            return s
        for i in range(len(s), 0, -1):
            for j in range(len(s)-i+1):
                substring = s[j:j+i]
                if substring == substring[::-1]:
                    return substring

# T.C : O(n^2)


check = Solution()
print(check.longestPalindrome("babad"))
print(check.longestPalindrome("cbbd"))
print(check.longestPalindrome("a"))
print(check.longestPalindrome("ac"))
print(check.longestPalindrome("bb"))

"""
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


Example 5:

Input: s = "bb"
Output: "bb"
"""
