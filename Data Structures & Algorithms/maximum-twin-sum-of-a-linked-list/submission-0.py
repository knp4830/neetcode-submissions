# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find the middle half to partition
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second = slow.next 
        prev = slow.next = None 
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        maxSum = 0
        first = head
        # Find max twin sum
        while first and prev:
            maxSum = max(maxSum, first.val + prev.val)
            first = first.next
            prev = prev.next

        return maxSum