class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = defaultdict(int)
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if hmap[temp]:
                return[hmap[temp], i + 1]
            hmap[numbers[i]] = i + 1
        return []