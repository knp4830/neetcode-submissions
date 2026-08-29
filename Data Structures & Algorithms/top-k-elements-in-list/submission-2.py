class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Implement an integer hashmap
        freq_map = defaultdict(int)
        
        # don't need index because we are simply appending value and adding to it
        for num in nums:
            freq_map[num] += 1

        ordered = sorted(freq_map, key=freq_map.get, reverse=True)
        return ordered[:k]