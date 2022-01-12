class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = float(-inf)
        curr = 0
        for num in nums:
            curr += num
            mx = max(mx, curr)
            if curr < 0:
                curr = 0
        return mx