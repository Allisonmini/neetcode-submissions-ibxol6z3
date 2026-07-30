class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        maxP = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            pro = prices[r] - prices[l]
            maxP = max(maxP, pro)
            r += 1
        return maxP
