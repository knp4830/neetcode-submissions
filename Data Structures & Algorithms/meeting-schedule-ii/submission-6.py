"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Base case
        if not intervals:
            return 0
        intervals.sort(key = lambda i: i.start)

        ends = []
        for interval in intervals:
            if ends and interval.start >= ends[0]:
                heapq.heappop(ends) # earliest room is free: reuse it
            heapq.heappush(ends, interval.end)
        return len(ends)
