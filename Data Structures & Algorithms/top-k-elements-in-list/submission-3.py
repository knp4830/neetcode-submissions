class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize Hashmap
        count = {}
        # Array thats same size as input array, index is frequency and value is list of values that occur that particular number of times
        freq = [[] for i in range(len(nums) + 1)]

        # go through each number and add the count, the get(n, 0) adds the number if its not there
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # go through each value that we counted, count.items() returns every key value pair
        # c is the count or the index
        # we append n meaning this value n occurs c number of times
        for n, c in count.items():
            freq[c].append(n)

        # result output
        res = []
        # we iterate in descending order cause we want most occurences
        for i in range(len(freq) - 1, 0, -1):
        # go through every value in frequency cause every value inserted in i is another sublist
        # it could be empty or have some values
            for n in freq[i]:
                res.append(n)
                # when we get the same number as our target we know we are done
                if len(res) == k:
                    return res 
