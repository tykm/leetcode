class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        left = 0
        right = len(height) - 1
        mx = 0
        
        while left != right:
            area = (right - left) * min(height[left], height[right])
            mx = max(mx, area)
            #print(left, right, height[left], height[right], area, mx)
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return mx