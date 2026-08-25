# Create a list node class, good use of abstraction and encapsulating the data all together
class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        # Dummy node
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        # we use .next because we ignore the dummy node
        cur = self.head.next
        i = 0
        # Can use this syntax because it automatically means while our current index is not null
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1 # Index out of bounds

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node # This sets the dummy head pointer to the new node
        if not new_node.next:
            # if the list was empty before inserting
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head
        while i < index and cur:
            # Move cur to node before target node
            i += 1
            cur = cur.next

        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        cur = self.head.next
        res = []

        while cur:
            res.append(cur.val)
            cur = cur.next

        return res
