class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = float(-inf)
        curr = 0
        for num in nums:
            # Take care of answer < 0 case
            if num > mx:
                mx = num
            if curr < 0:
                curr = 0
            curr += num
            mx = max(mx, curr)
        return mx