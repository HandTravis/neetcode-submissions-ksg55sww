class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        mins = [0] * n
        mins[0] = float('inf')
        cur = prices[0]

        for i in range(1, n):
            cur = min(cur, prices[i])
            mins[i] = cur
        
        res = 0

        for m, p in zip(mins, prices):
            res = max(res, p - m)
        
        return res
        