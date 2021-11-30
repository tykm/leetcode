class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store previous existed items in dictionary
        # {num:index, ...}
        visited = {}
        
        for i in range(len(nums)):
            num = nums[i]
            if target - num in visited:
                return [i, visited[target - num]]
            visited[num] = i