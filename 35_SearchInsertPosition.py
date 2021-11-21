class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Binary Search
        infront = 0
        while len(nums) > 1:
            print(nums)
            mid = len(nums)//2
            first = nums[:mid]
            last = nums[mid:]
            if target == first[-1]:
                return infront + len(first) - 1
            elif target == last[0]:
                return infront + len(first)
            elif target > first[-1]:
                nums = last
                infront += len(first)
            elif target < last[0]:
                nums = first
        if nums[0] < target:
            infront += 1
        return infront
# T.C: O(log(n))


output = Solution()
print(output.searchInsert(nums=[1, 3, 5, 6], target=5))
print(output.searchInsert(nums=[1, 3, 5, 6], target=2))
print(output.searchInsert(nums=[1, 3, 5, 6], target=7))
print(output.searchInsert(nums=[1, 3, 5, 6], target=0))
print(output.searchInsert(nums=[1], target=0))

'''
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2


Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1


Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4


Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0


Example 5:
Input: nums = [1], target = 0
Output: 0

'''
