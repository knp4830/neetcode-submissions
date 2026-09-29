class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        res = count = 0
        sign = 0

        for R in range(n - 1):
            if arr[R] > arr[R + 1]:
                count = count + 1 if sign == -1 else 1
                sign = 1
            elif arr[R] < arr[R + 1]:
                count = count + 1 if sign == 1 else 1
                sign = -1
            else:
                count = 0
                sign = 0

            res = max(res, count)

        return res + 1