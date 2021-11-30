class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        # Indices for low and high price days
        low = float('inf')
        high = float('-inf')
        print(low, high)
        
        for price in prices:
            if price < low:
                low = price
            elif price > high:
                high = price
        if low == float('inf') or high == float('-inf'):
            return 0
        return high - low