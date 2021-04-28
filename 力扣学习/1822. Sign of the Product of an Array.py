"""
Name : 1822. Sign of the Product of an Array.py
Author : xyChen
Time : 2021/4/23 10:31
Desc:
"""
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for x in nums:
            res *= self.signFunc(x)
            if res == 0:
                return 0
        return res

    def signFunc(self, num: int):
        if num > 0:
            return 1
        elif num == 0:
            return 0
        else:
            return -1