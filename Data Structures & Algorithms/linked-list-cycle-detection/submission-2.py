# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(n) time and O(1) space
        # Initialize heads
        slow, fast = head, head
        # So long as fast has a value and the next does too
        while fast and fast.next:
            # we increment slow by one and fast by two
            # so if there is a cycle fast will reach slow
            slow = slow.next
            fast = fast.next.next
            # If they are equal we return true
            if slow == fast:
                return True
        
        return False