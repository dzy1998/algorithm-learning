"""
Name : 1480. Running Sum of 1d Array.py
Author : xyChen
Time : 2021/4/26 14:21
Desc:
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        s = 0
        for x in nums:
            s += x
            res.append(s)
        return res


solution = Solution()
print(solution.runningSum(nums=[1, 2, 3, 4]))
