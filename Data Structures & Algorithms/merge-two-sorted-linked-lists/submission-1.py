# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode(0) #creates current and dummy pointing to a dummy node

        while list1 and list2: #iterate through both lists until one reaches None
            if list1.val < list2.val: #If the value of list1 is less than list2 that means we append the value of list1 to our new list
                current.next = list1 #currents next is now starting at list1 value
                list1 = list1.next #now we move forward. List1 is now moved up one, current is now where list1 just was
            else:
                current.next = list2 #if list2 is less than list1 value. We append its value to current.
                list2 = list2.next #now list2 is moved forward, and current is at where list2 was
            current = current.next

        if list1 or list2: #if one or the other has not yet reached None
            current.next = list1 if list1 else list2 #append the rest of the one that has not reached none to currents next.

        return dummy.next #this was never iterated forward, so we can just return the head which is next