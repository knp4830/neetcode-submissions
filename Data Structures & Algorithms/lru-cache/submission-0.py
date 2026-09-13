class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # Capacity needs to be stored to know if we ever go over it
        self.cap = capacity
        self.cache = {} # map key to nodes

        # Left = LRU, right = Most Recent
        self.left, self.right = Node(0, 0), Node(0, 0) # Dummy nodes
        self.left.next, self.right.prev = self.right, self.left

    # Helper function applied to linked list
    # remove from the list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # TODO: update most recent
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from the hashmap (cache)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

