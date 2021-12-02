class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memory = dict()
        current_chars = str()
        if len(s) < 2:
            return len(s)
        for i in range(len(s)):
            if s[i] not in current_chars:
                current_chars += s[i]
            else:
                memory[current_chars] = len(current_chars)
                current_chars = current_chars[current_chars.index(
                    s[i])+1:] + s[i]
        memory[current_chars] = len(current_chars)
        return max(memory.values())

# T.C : O(n)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set(s)
        if len(unique) == len(s):
            return len(s)
        max_length = len(unique)
        for l in range(max_length, 0, -1):
            for i in range(len(s)-l+1):
                substring = s[i:i+l]
                if len(substring) == len(set(substring)):
                    return len(substring)
        return 0

# T.C : O(m*n)


check = Solution()
print(check.lengthOfLongestSubstring("abcabcbb"))
print(check.lengthOfLongestSubstring("bbbbb"))
print(check.lengthOfLongestSubstring("pwwkew"))
print(check.lengthOfLongestSubstring(""))
print(check.lengthOfLongestSubstring(" "))
print(check.lengthOfLongestSubstring("au"))
print(check.lengthOfLongestSubstring("aab"))
print(check.lengthOfLongestSubstring("dvdf"))
print(check.lengthOfLongestSubstring("aabaab!bb"))


"""
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


Example 5:

Input: s = " "
Output: 1
"""
