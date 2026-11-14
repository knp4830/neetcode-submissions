class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums: # Key = Integer, Value = # Of Occurences
            hashmap[num] += 1

        minHeap = []
        for occ in hashmap.keys():
            heapq.heappush(minHeap, (hashmap[occ], occ))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res

        