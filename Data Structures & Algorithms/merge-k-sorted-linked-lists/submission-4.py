# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    # This is for the heap to compare nodes
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Heap solution
        # Base Case
        if len(lists) == 0:
            return None
        
        # Set up
        res = ListNode(0)
        cur = res
        minHeap = []

        # Seeding the heap
        for lst in lists:
            if lst is not None:
                heapq.heappush(minHeap, NodeWrapper(lst))
        
        # Runs until every node has been placed 
        while minHeap:
            # Remove and returns wrapper with smallest value in O(log k)
            node_wrapper = heapq.heappop(minHeap)
            cur.next = node_wrapper.node
            cur = cur.next

            # Attach node to the result and advance the tail
            if node_wrapper.node.next:
                heapq.heappush(minHeap, NodeWrapper(node_wrapper.node.next))

        return res.next

            