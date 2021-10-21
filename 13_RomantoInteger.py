class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        roman_order = list(roman_dict.keys())
        converted = [roman_dict[char] for char in s]
        indexed = [roman_order.index(char) for char in s]
        for i in range(len(indexed)-1):
            if indexed[i] < indexed[i+1]:
                converted[i] = converted[i] * -1
        return sum(converted)


check = Solution()
print(check.romanToInt("MCMXCIV"))
"""
Example 1:

Input: s = "III"
Output: 3


Example 2:

Input: s = "IV"
Output: 4


Example 3:

Input: s = "IX"
Output: 9


Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.


Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
