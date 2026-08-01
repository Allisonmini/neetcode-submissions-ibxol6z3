class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l+1
        res = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            profit = prices[r] - prices[l]
            res = max(res, profit)
            r += 1
        return res

# Time = O(n), Space = O(1)



'''
[10,1,5,6,7,1]
[l, r,       ]

'''
        