class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        sm = 0
        for i in range(len(nums)):
            sm = 0
            for j in range(i, len(nums)):
                sm += nums[j]
                if sm > k:
                    break
                elif sm == k:
                    ans += 1
        return ans