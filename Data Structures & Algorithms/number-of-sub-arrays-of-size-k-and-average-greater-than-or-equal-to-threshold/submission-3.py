class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        res = 0
        total = 0

        for R in range(len(arr)):
            total += arr[R]
            if R >= k:
                total -= arr[R - k]
            if R >= k - 1 and total >= threshold:
                res += 1
        
        return res 