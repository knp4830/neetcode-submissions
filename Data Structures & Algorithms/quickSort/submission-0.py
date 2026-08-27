# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs, l, r):
        # if the length is just 1 its already sorted by itself
        if r - l + 1 <= 1:
            return
        

        pivot = pairs[r] # right most element
        left = l # this is where we should place the next element that is less than the pivot

        for i in range(l, r):
            # partition
            if pairs[i].key < pivot.key:
                pairs[left], pairs[i] = pairs[i] , pairs[left]
                left += 1
        pairs[r] = pairs[left]
        pairs[left] = pivot

        self.quickSortHelper(pairs, l, left - 1) # left
        self.quickSortHelper(pairs, left + 1, r) # right