# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(n) time and space
        seen = set()
        cur = head
        # While there is a next
        while cur:
            # If we see it we return True
            if cur in seen:
                return True
            # Otherwise we just add it and go next
            seen.add(cur)
            cur = cur.next
        # If it doesn't have a cycle we return false
        return False