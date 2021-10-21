class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        pair = {
            "(": ")",
            "{": "}",
            "[": "]",
            ")": "Prevent Key Error",
            "}": "Prevent Key Error",
            "]": "Prevent Key Error",
        }

        i = 0
        while len(s)-1 > i:
            if pair[s[i]] == s[i+1]:
                s = s[:i] + s[i+2:]
                i = 0
            else:
                i += 1

        if len(s) > 0:
            return False
        return True


sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))

"""
Example 1:

Input: s = "()"
Output: true


Example 2:

Input: s = "()[]{}"
Output: true


Example 3:

Input: s = "(]"
Output: false


Example 4:

Input: s = "([)]"
Output: false


Example 5:

Input: s = "{[]}"
Output: true
"""
