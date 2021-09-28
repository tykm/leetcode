class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hist = {0:1}
        ans = 0
        sm = 0
        
        # iterate once and keep track of sum
        for i in range(len(nums)):
            sm += nums[i]
            if sm - k in hist:
                ans += hist[sm-k]
            if sm in hist:
                hist[sm] += 1
            else:
                hist[sm] = 1
                
        
        
        return ans