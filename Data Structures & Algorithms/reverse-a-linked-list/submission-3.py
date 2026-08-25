# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Save node to placeholder, set node next to the previous node. Return its head
        # We use a while loop to go until there is no more next
        
        prev = None
        cur = head
        while cur:
            nextLink = cur.next
            cur.next = prev
            prev = cur
            cur = nextLink
        return prev