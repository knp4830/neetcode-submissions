class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Get the distance for every point in the list
        # Put it into a minheap with the original points
        # pop k elements and those distances are the shortest and return the key

        # Get your distance of points
        heap = []
        # Get the distance from middle of both points
        for x, y in points:
            # Append to the heap the distance and the points
            heap.append((x*x + y*y, [x, y])) 
        # Make a minheap of the distance and points
        # It keeps track of the distance as the value for minimum
        heapq.heapify(heap)

        
        return [heapq.heappop(heap)[1] for _ in range(k)]