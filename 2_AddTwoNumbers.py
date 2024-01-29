from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        p1 = ""
        p2 = ""

        while l1:
            p1 += str(l1.val)
            l1 = l1.next

        while l2:
            p2 += str(l2.val)
            l2 = l2.next

        p3 = int(p1[::-1]) + int(p2[::-1])
        p3 = str(p3)
        p = ListNode(int(p3[-1]))
        res = p

        for i in range(len(p3) - 2, -1, -1):
            p.next = ListNode(int(p3[i]))
            p = p.next

        return res


"""
Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
