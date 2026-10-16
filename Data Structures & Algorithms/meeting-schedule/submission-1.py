"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key = lambda x:x.start)
        first_interval = intervals[0]

        start = first_interval.start
        end = first_interval.end

        for i in range(1, len(intervals)):
            if intervals[i].start < end:
                return False
            else:
                start = intervals[i].start
                end = intervals[i].end

        return True 