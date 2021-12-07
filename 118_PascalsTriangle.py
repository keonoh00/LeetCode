# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        row = 3
        first_row = [1]
        second_row = [1, 1]
        result = [first_row, second_row]
        if numRows == 1:
            return [first_row]
        elif numRows == 2:
            return result
        while row <= numRows:
            current_row = result[row-2]
            next_row = [1, 1]
            for i in range(len(current_row)-1):
                add = current_row[i] + current_row[i+1]
                next_row.insert(1, add)
            result.append(next_row)
            row += 1
        return result


check = Solution()
print(check.generate(5))
print(check.generate(1))


"""
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


Example 2:

Input: numRows = 1
Output: [[1]]
"""
