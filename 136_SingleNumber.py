# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        temp = 0
        for i in range(len(nums)):
            # Use of Bitwise XOR Operator
            temp ^= nums[i]
        return temp


check = Solution()
print(check.singleNumber(nums=[2, 2, 1]))
print(check.singleNumber(nums=[4, 1, 2, 1, 2]))
print(check.singleNumber(nums=[1]))
print(check.singleNumber(nums=[1, 3, 1, -1, 3]))

"""
Example 1:

Input: nums = [2,2,1]
Output: 1


Example 2:

Input: nums = [4,1,2,1,2]
Output: 4


Example 3:

Input: nums = [1]
Output: 1

Example 4:

Input: nums = [1,3,1,-1,3]
Output: -1

"""
