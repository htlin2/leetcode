class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = float('inf'), 0
        for p in prices:
            max_profit = max(max_profit, p - min_price)
            min_price = min(min_price, p)
        return max_profit

"""
1) brute force
two for loops, first for buy, 2nd for sell
Time: O(n^2)
Space: O(1)

2) keep track of min price?
[7,1,5,3,6,4]
  -1
Time: O(n)
Space: O(1)
"""