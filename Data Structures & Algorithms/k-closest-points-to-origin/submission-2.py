class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] # Initialize our min heap
        res = []
        for x, y in points: # go through all points
            heapq.heappush(minHeap, [(x * x) + (y * y), x, y]) # we want the points to be appended as well

        for i in range(k):
            cur = heapq.heappop(minHeap)
            res.append([cur[1], cur[2]])
        return res
