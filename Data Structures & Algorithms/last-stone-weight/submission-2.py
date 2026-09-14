class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Shorter lines
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            L1, L2 = heapq.heappop(stones), heapq.heappop(stones)
            if L2 > L1:
                heapq.heappush(stones, L1 - L2)

        stones.append(0)
        return abs(stones[0])