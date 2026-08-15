class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cheapest = 0
        for i in range(len(prices)):
            temp = prices[i] - prices[cheapest]
            if temp > profit:
                profit = temp

            if prices[i] < prices[cheapest]:
                cheapest = i

        return profit
