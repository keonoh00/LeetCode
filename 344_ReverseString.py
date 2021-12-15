# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Simple Solution
class Solution:
    def reverseString(self, s: list[str]) -> None:
        s[:] = s[::-1]


check = Solution()
print(check.reverseString(s=["h", "e", "l", "l", "o"]))
print(check.reverseString(s=["H", "a", "n", "n", "a", "h"]))

"""
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]


Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
