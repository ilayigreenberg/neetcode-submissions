class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices) - 1
        maxPrf = 0
        while l < r:
            if prices[l + 1] <= prices[l]:
                l += 1
            if prices[r - 1] >= prices[r]:
                r -= 1
            diff = prices[r] - prices[l]
            if diff > maxPrf:
                maxPrf = diff
            r += 1
        return maxPrf
            