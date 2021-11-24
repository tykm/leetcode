'''
This implementation uses an integer to store the max jump index. No more hashmap and O(n) time and O(1) space. Needs work on the while loop conditions.
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        curr = 0
        jumpable = 0    # Pointer to store max jumpable index
        
        # While we are allowed to jump forward:
        while jumpable >= curr and curr < len(nums) or jumpable == 0:
            curr_jump = nums[curr]
            
            # Check if current + nums[current] > jumpable: set jumpable
            jumpable = max(jumpable, curr + curr_jump)
            print(curr, curr_jump, jumpable)
            curr += 1
        
        if jumpable < len(nums) - 1:
            return False
        return True