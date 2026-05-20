class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        remove = 0
        last_end = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] >= last_end:
                last_end = interval[1]
            else:
                remove += 1
                last_end = min(interval[1], last_end)
            
        return remove