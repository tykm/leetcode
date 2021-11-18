# Kinda works. Doesn't work for case [0, 0]

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        left = 0
        right = len(height) - 1
        mx = 0
        
        while left != right:
            #print(left, right, height[left], height[right])
            area = (right - left - 1) * max(height[left], height[right])
            mx = max(mx, area)
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return mx