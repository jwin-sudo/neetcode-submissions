class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort(key=lambda x: x[0])

        output = []

        start = intervals[0][0]
        end = intervals[0][1]
        

        for i in range(1, len(intervals), 1):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                output.append([start, end])

                start = intervals[i][0]
                end = intervals[i][1]

        output.append([start, end])

        return output 