class Solution:
    def maxArea(self, heights: List[int]) -> int:
        begin = 0
        end = len(heights) - 1
        height1 = heights[begin]
        height2 = heights[end]
        max_water = min(height1, height2) * (end - begin)
        
        while begin != end:
            if height1 < height2:
                begin += 1
                height1 = max(height1, heights[begin])
            else:
                end -= 1
                height2 = max(height2, heights[end])
            max_water = max(max_water, min(height1, height2) * (end - begin))
        
        return max_water