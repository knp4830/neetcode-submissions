# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, cur = groupNext, groupPrev.next   # prev starts at groupNext
            while cur != groupNext:                 # Reverse just this group
                cur.next, prev, cur = prev, cur, cur.next
            
            tmp = groupPrev.next                    # old head = new tail
            groupPrev.next = kth                    # connect previous part to new head
            groupPrev = tmp                         # new tail is teh new group's groupPrev

        return dummy.next

    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur