class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        count = 0 
        
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
                end = min(intervals[i][1], end)
            
            else:
                start = intervals[i][0]
                end = intervals[i][1]
        

        
        return count