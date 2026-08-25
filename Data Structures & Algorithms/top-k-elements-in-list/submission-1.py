class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = Counter(nums) #counts the frequencies
        top_k = count_map.most_common(k) #takes the top-k pairs (item, freq)
        # this returns a tuple (key, value) = (number, frequency)
        # ex: top_k = [(1,3), (2,2)]
        top_k_keys = [k for k, v in top_k] #extracts only the keys
        # loop through each (k,v) pair (key-value pair) in the list top_k
        # takes only the first item (k) from each tuple
        # -> [1,2,3]
        #longer version would be
        #top_k_keys = []
        #for k, v in top_k:
        #    top_k_keys.append(k)
        return top_k_keys
