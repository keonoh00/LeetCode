class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        for i in range(len(haystack)):
            needle_candidate = haystack[i:i+len(needle)]
            if needle_candidate == needle:
                return i
        return -1
