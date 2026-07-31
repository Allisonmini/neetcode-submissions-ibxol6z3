class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l_buy = 0
        r_sell = l_buy + 1
        
        while r_sell < len(prices):
            if prices[l_buy] > prices[r_sell]:
                l_buy = r_sell

            profit = prices[r_sell] - prices[l_buy]
            res = max(res, profit)
            r_sell += 1

        return res
        