class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
      minimum = min([len(word) for word in strs])
      i = 0
      while minimum != 0 and i <= minimum:
        i += 1
        check = strs[0][:i]
        for word in strs:
          if word[:i] != check:
            return word[:i-1]
      return strs[0][:i]

example = Solution()
print(example.longestCommonPrefix(["flower","flow","flight"]))
print(example.longestCommonPrefix(["dog","racecar","car"]))

"""
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"


Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings
"""
