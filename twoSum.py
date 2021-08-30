class Solution():
     def twoSum(self, nums, target):
          # First addend
          for i in range(len(nums)):
               for j in range(len(nums) - 1):
                    if nums[i] + nums[j + i + 1] == target:
                         return [i, j + 1]

3 2 4
6