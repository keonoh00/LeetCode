class Solution:
    def merge(
        self,
        nums1: list[int],
        m: int,
        nums2: list[int],
        n: int,
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        while len(nums2) > 0:
            if nums1[i] > nums2[0]:
                nums1.insert(i, nums2[0])
                nums1.pop(-1)
                nums2.pop(0)
            elif nums1[i] == 0 and i > m:
                nums1.insert(i, nums2[0])
                nums1.pop(-1)
                nums2.pop(0)
            i += 1
        return nums1


check = Solution()
print(check.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
print(check.merge(nums1=[1], m=1, nums2=[], n=0))
print(check.merge(nums1=[0], m=0, nums2=[1], n=1))
print(check.merge(nums1=[2, 0], m=1, nums2=[1], n=1))
print(
    check.merge(
        nums1=[-1, 0, 0, 3, 3, 3, 0, 0, 0],
        m=6,
        nums2=[1, 2, 2],
        n=3,
    )
)
print(
    check.merge(
        nums1=[-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        m=5,
        nums2=[-1, -1, 0, 0, 1, 2],
        n=6,
    )
)


"""
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the
underlined elements coming from nums1.


Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].


Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1.
The 0 is only there to ensure the merge result can fit in nums1.


Example 4:

Input: nums1 = [2,0], m = 1, nums2 = [1], n = 1
Output: [1, 2]


Example 5:

Input: nums1 = [-1,0,0,3,3,3,0,0,0], m = 6, nums2 = [1,2,2], n = 3
Output: [-1,0,0,1,2,2,3,3,3]


Example 5:

Input: nums1 = [-1,0,0,0,3,0,0,0,0,0,0], m = 5, nums2 = [-1,-1,0,0,1,2], n = 6
Output: [-1,-1,-1,0,0,0,0,0,1,2,3]
"""
