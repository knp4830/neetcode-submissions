# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs:List[Pair], l: int, r: int) -> List[Pair]:
        if r - l + 1 <= 1:
            return pairs
        # Get Middle index
        m = (l + r) // 2

        # Sort left
        self.mergeSortHelper(pairs, l, m)

        # Sort right
        self.mergeSortHelper(pairs, m + 1, r)

        # call merge itself
        self.merge(pairs, l, m, r)

        return pairs

    def merge(self, arr: List[pair], l: int, m: int, r: int) -> None:

        L = pairs[l:m+1]
        R = pairs[m+1:r+1]

        i = 0 # left
        j = 0 # right
        k = l # index for array

        # Merge two sorted halfs into original
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # one of the halfs remain
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


