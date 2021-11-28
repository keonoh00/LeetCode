class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for x in range(len(s)-1, 0, -1):
            if s[x] != " " and s[x-1] == " ":
                count += 1
                return count
            elif s[x] != " ":
                count += 1
            else:
                pass
        if s[0] != " ":
            count += 1
        return count
