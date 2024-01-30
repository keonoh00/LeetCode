# flake8: noqa
# 1. Two Sum

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


# Solution 1: Brute Force
# Time complexity: O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for first in range(len(nums)):
            for second in range(first + 1, len(nums)):
                if nums[first] + nums[second] == target:
                    return [first, second]

        return []


# Solution 2: Two-pass Hash Table
# Time complexity: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a hash table
        hash_table = {}
        # Add the elements to the hash table
        for i in range(len(nums)):
            hash_table[nums[i]] = i

        # Find the two numbers
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table and hash_table[complement] != i:
                return [i, hash_table[complement]]

        return []


# Solution 3: One-pass Hash Table
# Time complexity: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype List[int]
        """
        # Create a hash table
        hash_table = {}

        # Find the two numbers
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table:
                return [hash_table[complement], i]

            hash_table[nums[i]] = i

        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(solution.twoSum([3, 2, 4], 6))  # [1, 2]
    print(solution.twoSum([3, 3], 6))  # [0, 1]
