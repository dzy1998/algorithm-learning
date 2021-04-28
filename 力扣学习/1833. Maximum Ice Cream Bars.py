"""
Name : 1833. Maximum Ice Cream Bars.py
Author : xyChen
Time : 2021/4/23 14:53
Desc:
"""
from typing import List


class Solution:
    # 快速排序的方法超时
    # 尝试参考背包问题采用动态规划，失败
    # 简单的思路就是采用内置函数来排序
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i in range(len(costs)):
            coins -= costs[i]
            if coins < 0:
                return i
        return len((costs))
        # dp1 = [0] * (coins + 1)
        # dp2 = [0] * (coins + 1)
        # for i in range (len(costs)):
        #     for j in range(1, len(dp2)):
        #         res = j - costs[i]
        #         if res >= 0:
        #             dp2[j] = max(dp1[j], dp1[res] + 1)
        #     dp1 = dp2
        # return max(dp2)

        # costs = self.quickSort(costs)
        # for i in range(len(costs)):
        #     coins -= costs[i]
        #     if coins < 0:
        #         return i
        # return len(costs)

    def quickSort(self, nums: List[int]):
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[0]
            less = [i for i in nums[1:] if i <= pivot]
            greater = [i for i in nums[1:] if i > pivot]
            return self.quickSort(less) + [pivot] + self.quickSort(greater)


solution = Solution()
print(solution.maxIceCream(costs = [1,3,2,4,1], coins = 7))
