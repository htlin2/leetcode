class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, skip = float('-inf'), float('-inf'), 0
        for p in prices:
            temp = sell
            sell = buy + p
            buy = max(buy, skip - p)
            skip = max(temp, skip)
        return max(sell, skip)