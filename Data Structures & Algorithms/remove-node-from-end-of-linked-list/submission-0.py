# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node at 0 and next to be head
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # move the head n distances ahead
        while n > 0 and right:
            right = right.next
            n -= 1
        # Keep shifting both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next
        # Delete the node by pointing next to the one after
        left.next = left.next.next

        return dummy.next