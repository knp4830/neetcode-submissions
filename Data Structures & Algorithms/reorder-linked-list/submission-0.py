# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        h2 = slow.next
        slow.next = None
        h1 = head 
        prev = None 
        while h2:
            nextLink = h2.next
            h2.next = prev
            prev = h2
            h2 = nextLink 
        while prev:
            dummy1 = h1.next
            dummy2 = prev.next
            h1.next = prev
            prev.next = dummy1
            h1 = dummy1
            prev = dummy2