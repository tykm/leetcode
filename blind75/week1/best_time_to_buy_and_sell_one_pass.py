class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        # Indices for low and high price days
        low = float('inf')
        mx = 0
        
        for price in prices:
            if price < low:
                low = price
            if price - low > mx:
                mx = price - low
        
        return mx