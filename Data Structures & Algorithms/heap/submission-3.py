class MinHeap:
    
    def __init__(self):
        # Initialize heap with dummy value at the index 0
        self.heap = [0]

    def push(self, val: int) -> None:
        # Pushes value onto the heap
        self.heap.append(val)
        self.percolate_up(len(self.heap) - 1)

    def pop(self) -> int:
        # Pops the smallest value
        if len(self.heap) <= 1:
            return -1
        # If only one value
        if len(self.heap) == 2:
            return self.heap.pop()
        
        # Move the last element to the root and percolate down
        root = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolate_down(1)
        return root

    def top(self) -> int:
        # If empty otherwise return the first index
        if len(self.heap) <= 1:
            return - 1
        return self.heap[1]
        

    def heapify(self, nums: List[int]) -> None:
        # Transform a list into a heap in-place (concatonates the two arrays)
        self.heap = [0] + nums
        # We only need to bubble down with half of the heap and we're going in reverse order
        for i in reversed(range(1, len(self.heap) // 2 + 1)):
            self.percolate_down(i)

        
    def percolate_up(self, index: int) -> None:
            parent = index // 2 # Parent is always index // 2
            # Checks if its not the root and if its less than the parent
            while index > 1 and self.heap[parent] > self.heap[index]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
                parent = index // 2

    def percolate_down(self, index: int) -> None:
        # Left child
        child = 2 * index
        while child < len(self.heap):
            # if there is a right child and its smaller than the left
            if child + 1 < len(self.heap) and self.heap[child] > self.heap[child + 1]:
                # right child is smaller
                child += 1
            # if the child is greater than the index
            if self.heap[child] >= self.heap[index]:
                return
            # Swap index and child
            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            index = child 
            child = 2 * index # left child 

