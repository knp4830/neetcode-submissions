class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks) # Sort by turning it into a heap
        count = 0
        while len(sticks) > 1: 
            a = heapq.heappop(sticks) # first minimum
            b = heapq.heappop(sticks) # second minimum
            heapq.heappush(sticks, (a + b)) # push back on the total
            count += (a + b)

        return count

