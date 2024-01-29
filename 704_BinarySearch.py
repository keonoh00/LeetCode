# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        count = 0
        if len(nums) == 1:
            return nums[0]
        while len(nums) > 1:
            halfIndex = len(nums)//2
            first = nums[:halfIndex]
            last = nums[halfIndex:]
            if first[-1] == target:
                return count + len(first) - 1
            elif last[0] == target:
                return count + len(first)
            elif target < first[-1]:
                nums = first
            elif target > first[-1]:
                nums = last
                count += len(nums)
            else:
                pass
        return -1


check = Solution()
print(check.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(check.search(nums=[-1, 0, 3, 5, 9, 12], target=2))

"""
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4


Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
