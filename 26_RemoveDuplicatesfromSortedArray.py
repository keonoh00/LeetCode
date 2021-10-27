class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        checked = []
        i = 0
        while len(nums) > i:
            if nums[i] in checked:
                nums.pop(i)
                nums.append("_")
            elif nums[i] == "_":
                i += 1
            else:
                checked.append(nums[i])
                i += 1
        return len(checked)


check = Solution()
print(check.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
