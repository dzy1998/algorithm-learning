"""
Name : 136. Single-Number.py
Author : xyChen
Time : 2021/4/9 14:23
Desc:
"""
from typing import List


class Solution:
    # 找出数组中只出现一次的数，其他均出现两次
    # 思路来自@深红，异或运算，相同的数异或结果为0，0和任何数异或为该数
    # 异或满足交换律
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans ^= x
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([2,2,1]))

