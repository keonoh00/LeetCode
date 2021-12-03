# Binary Search Approach
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        i = 0
        j = x
        while i <= j:
            half = (i+j)//2
            if half*half <= x < (half+1)*(+1):
                return half
            elif half*half > x:
                j = half
            else:
                i = half


# Conventional Approach
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x < 1:
#             return 0
#         i = 0
#         power2 = 1
#         while power2 < x:
#             next = (i+1) * (i+1)
#             if x < next:
#                 return i
#             power2 = next
#             i += 1
#         return i

check = Solution()
print(check.mySqrt(7))

"""
Example 1:

Input: x = 4
Output: 2


Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""
