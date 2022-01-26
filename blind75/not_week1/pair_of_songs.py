class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # { time:count, 30:1}
        d = {}
        ans = 0
        for t in time:
            if 60 - (t % 60) in d:
                ans += d[60 - (t % 60)]
            else:
                d[t%60] = d.get(t%60, 0) + 1
                print(t, t%60, d[t%60])
                
        return ans