class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            heapq.heappush(minHeap, [(x * x) + (y * y), [x,y]])
        
        return [heapq.heappop(minHeap)[1] for _ in range(k)]