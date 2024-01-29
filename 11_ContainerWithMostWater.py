class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0
        while len(height) > 1:
            if height[0] > height[-1]:
                check = height[-1] * (len(height)-1)
                height = height[:-1]
            else:
                check = height[0] * (len(height)-1)
                height = height[1:]
            if check > maxArea:
                maxArea = check
        return maxArea


check = Solution()
print(check.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(check.maxArea(height=[1, 1]))

"""
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Example 2:

Input: height = [1,1]
Output: 1
"""
