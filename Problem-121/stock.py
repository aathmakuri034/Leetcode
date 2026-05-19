# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# SOLVED

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buyPrice = prices[0]
        profit = 0

        for i in range(len(prices)):
            if (buyPrice < prices[i]):
                if profit < prices[i] - buyPrice:
                    profit = prices[i] - buyPrice
            else:
                buyPrice = prices[i]
        
        return profit


if __name__ == "__main__":
    solution = Solution()

    caseOne = [7,1,5,3,6,4]
    caseTwo = [7,6,4,3,1]

    print("Test case 1")
    print("Actual Output: " + str(solution.maxProfit(caseOne)))
    print("Expected Output: 5")
    print("="*30)

    print("Test case 2")
    print("Actual Output: " + str(solution.maxProfit(caseTwo)))
    print("Expected Output: 0")
    print("="*30)