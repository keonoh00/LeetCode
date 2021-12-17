# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

def fact(n):
    # Can Import Factorial from math library but self defined fuction used
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = list()
        n_factorial = fact(rowIndex)
        for i in range(rowIndex+1):
            binom_coef = n_factorial / (fact(i)*fact(rowIndex-i))
            result.append(int(binom_coef))
        return result


check = Solution()
print(check.getRow(rowIndex=3))
print(check.getRow(rowIndex=0))
print(check.getRow(rowIndex=1))

"""
Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]


Example 2:

Input: rowIndex = 0
Output: [1]


Example 3:

Input: rowIndex = 1
Output: [1,1]
"""
