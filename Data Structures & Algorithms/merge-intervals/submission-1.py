class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Review for Amazon
        intervals.sort(key = lambda x: x[0])    # We sort by start (ties are decided by end)
        res = [intervals[0]]        # Start with first interval

        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        
        return res