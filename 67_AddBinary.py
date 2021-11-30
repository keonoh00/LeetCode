class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        a = a[::-1]
        b = b[::-1]
        if len(a) > len(b):
            b += "0" * (len(a)-len(b))
        else:
            a += "0" * (len(b)-len(a))
        carry = 0
        for i in range(len(a)):
            current_sum = int(a[i]) + int(b[i]) + carry
            if current_sum == 3:
                current_sum = 1
                carry = 1
            elif current_sum == 2:
                current_sum = 0
                carry = 1
            else:
                carry = 0
            result += str(current_sum)
            print(
                f"i:{i},   a:{a[i]},   b:{b[i]},   current_sum:{current_sum},  carry:{carry},   result:{result}")
        if carry != 0:
            result += str(1)
        return result[::-1]
# T.C : O(max(m, n))


check = Solution()
print(check.addBinary(a="0", b="0"))

"""
Example 1:

Input: a = "11", b = "1"
Output: "100"


Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
