class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        val_in_nums = nums.count(val)
        for i in range(val_in_nums):
            nums.remove(val)
            nums.append("_")
        return len(nums)-val_in_nums
