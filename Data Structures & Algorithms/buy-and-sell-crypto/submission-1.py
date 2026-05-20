class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0 
        # for i in range(len(prices)-1):
        #     for j in range(i, len(prices)):
        #         if prices[j] - prices[i] > profit: 
        #             profit = prices[j] - prices[i]
        # return profit 

        # DP approach

        max_profit = 0
        min_buy = prices[0]

        for sell in prices:
            max_profit = max(max_profit, sell - min_buy)
            min_buy = min(min_buy, sell)

        return max_profit