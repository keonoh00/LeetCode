# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(-10000)
        front = result
        while head:
            if result.val != head.val:
                result.next = ListNode(head.val)
                result = result.next
            head = head.next
        return front.next

# T.C : O(n)
