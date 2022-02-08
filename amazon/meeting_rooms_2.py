class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Start by sorting the intervals list according by start time
        # O(n*log(n))
        def sort_by_start(interval):
            return interval[0]
        intervals.sort(key=sort_by_start)
        
        # Define variables
        rooms = 0
        ongoing_meetings = 0
        start_count = {}
        low = float(inf)
        high = float(-inf)
        
        #[[0, 30], [5, 10], [15, 20]]
        for interval in intervals:
            begin = interval[0]
            end = interval[1]
            start_count[begin] = start_count.get(begin, 0) + 1
            # Check if any meetings are over