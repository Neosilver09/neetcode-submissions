class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minPrice = prices[0]

        for i,price in enumerate(prices):
            if price < minPrice:
                minPrice = price

            if price-minPrice> maxProfit:
                maxProfit = price - minPrice
    

        
        return maxProfit

            
