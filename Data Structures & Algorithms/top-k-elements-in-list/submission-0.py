class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = Counter(nums)
        top_k = count_map.most_common(k)
        top_k_keys = [k for k, v in top_k]
        return top_k_keys
