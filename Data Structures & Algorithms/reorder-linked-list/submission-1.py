# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # h2 is now the second half (have to do .next to get the head of secondhalf)
        h1, h2 = head, slow.next
        slow.next = None # Cuts the linked list in half
        # First half 
        prev = None 

        # Reverse the second half
        while h2:
            nextLink = h2.next
            h2.next = prev
            prev = h2
            h2 = nextLink 
        
        # While there is a second half parse them together
        while prev:
            dummy1 = h1.next # store first half next in a dummy
            dummy2 = prev.next # store second half next in a dummy
            h1.next = prev # make first half next the second half
            prev.next = dummy1 # make second half the first halfs next
            h1 = dummy1 # Make h1 be the dummy now so once it loops it continues
            prev = dummy2 # make h2 be the dummy now so once it loops it continues