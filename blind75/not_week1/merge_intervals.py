class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        # Helper function for key for sorting by beginning of interval
        def begin(elem):
            return elem[0]
        intervals.sort(key=begin)
        
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_begin = ans[-1][0]
            prev_end = ans[-1][1]
            curr_begin = intervals[i][0]
            curr_end = intervals[i][1]
            if (curr_begin >= prev_begin and curr_begin <= prev_end) or (curr_end >= prev_begin and curr_end <= prev_end):
                ans[-1] = [min(prev_begin, curr_begin), max(prev_end, curr_end)]
            else:
                ans.append(intervals[i])
        
        return ans