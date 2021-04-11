"""
Name : 121. Best-Time-to-Buy-and-Sell-Stock.py
Author : xyChen
Time : 2021/4/1 14:34
Desc:
"""
from typing import List


class Solution:
    # 一开始看到题目的感觉和 11乘最多水的容易的思路很像，尝试双指针从两端向中间遍历，但是移动的条件得不到
    # 退而求其次，尝试双重循环暴力法，结果超时
    # 动态规划思路来自@北冥有鱼
    # 记录今天之前的最小值，记录今天卖出时的收益，取最大的收益
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        # minPrice记录最低价
        minPrice = prices[0]
        profit = 0
        # profits = [0] * length
        for i in range(length):
            # profits[]记录当天卖出时的收益
            # 更优方案，可以不需列表
            # profits[i] = prices[i] - minPrice
            profit = max(prices[i] - minPrice, profit)
            if prices[i] < minPrice:
                minPrice = prices[i]
        return profit


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(prices = [7,1,5,3,6,4]))