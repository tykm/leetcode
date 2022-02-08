class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Edge case: only 1 meeting
        if len(intervals) == 1:
            return 1
        
        # We only care when any meeting begins and any meeting ends
        # The begin/end of a meeting are not important to keep linked.
        # We separate the starts and end times and then sort them in ascending order
        begin = []
        end = []
        for itvl in intervals:
            begin.append(itvl[0])
            end.append(itvl[1])
        begin.sort()
        end.sort()
        print(begin)
        print(end)
        
        # Now that we have the sorted beginning and end, we can
        # iterate over the beginning times and compare against the end times
        # to check if any meetings have ended
        room_count = 0
        e = 0
        for b in range(len(begin)):
            # If there is an ended meeting, then we don't have to create a new room
            if begin[b] >= end[e]:
                e += 1
            # If there is not an ended meeting, then we have to create a new room
            else:
                room_count += 1
        return room_count