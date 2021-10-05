class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index, value in enumerate(nums):
            restList = nums[index+1:]
            for index_2, value_2 in enumerate(restList):
                if value+value_2 == target:
                    return [index, index_2+index+1]