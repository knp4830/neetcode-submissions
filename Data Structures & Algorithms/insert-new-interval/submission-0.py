class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # In this case, the end is less than the start of the next one
            # Thus we can append everything afterwards from adding the new interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # If the start of the new interval is greater than the end of the interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # Overlapping
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res