# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        result = [""]
        correspondingLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        for i in digits:
            letters = correspondingLetter[i]
            result *= len(letters)
            count = 0
            index = 0
            for j in range(len(result)):
                if count == len(result)//len(letters):
                    count = 0
                    index += 1
                result[j] += letters[index]
                count += 1
        return result


check = Solution()
print(check.letterCombinations(digits="23"))
print(check.letterCombinations(digits=""))
print(check.letterCombinations(digits="2"))


"""
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


Example 2:

Input: digits = "23"
Output: []


Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""
