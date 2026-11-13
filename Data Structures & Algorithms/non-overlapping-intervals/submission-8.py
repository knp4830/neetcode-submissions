class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Amazon Review
        intervals.sort(key = lambda x: x[0])
        cur = intervals[0][1]
        res = 0

        for start, end in intervals[1:]:
            if start < cur:
                res += 1
                cur = min(cur, end)
            else:
                cur = end

        return res


