'''
I think correct but runtime is too slow for Leetcode to grade. 77/166 test cases passed.
Could improve by instead of using a hashmap, keep a pointer for max jump position. From that jump position, work backwards if there is no path. This way, we can skip certain indices.
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        jumpable = {0}   # { index:True for indices in List }
        
        # Touch each number once
        for index in range(len(nums)):
            
            # Check if current index is jumpable
            if index not in jumpable:
                return False
                
            # Log jumpable locations in set
            for i in range(nums[index]):
                jumpable.add(index + i + 1)
        
        return True