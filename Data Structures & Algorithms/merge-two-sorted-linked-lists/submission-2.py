# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode(0)  # Create a dummy node and a pointer to build the new list

        while list1 and list2:  # Iterate until at least one list is exhausted
            if list1.val < list2.val:
                current.next = list1  # Append the smaller node (list1) to current's next
                list1 = list1.next    # Move list1 forward
            else:
                current.next = list2  # Append the smaller node (list2) to current's next
                list2 = list2.next    # Move list2 forward
            current = current.next    # Advance current to the last node added

        # Attach the remainder of the non-empty list (if any)
        current.next = list1 if list1 else list2

        return dummy.next  # Return the merged list starting after dummy
