"""
Name : 122. Best-Time-to-Buy-and-Sell-Stock-II.py
Author : xyChen
Time : 2021/4/1 15:43
Desc:
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 思路来自@派大星星星星。贪心算法，非常符合人的思维：只要有钱赚就赚
        # 题目的第二示例可能有所误导？
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7,6,4,3,1]))

