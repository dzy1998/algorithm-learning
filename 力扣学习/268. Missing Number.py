"""
Name : 268. Missing Number.py
Author : xyChen
Time : 2021/4/15 19:29
Desc:
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 思路与之前一题 只出现一次的数字 相像
        # 数组加上0-n，刚好就是其他数字出现两次，缺失的数只出现一次
        # 还有思路 两组数加法求和 然后相减，但是注意溢出
        num = 0
        n = len(nums)
        for i in range(n):
            num ^= i ^ nums[i]
        return num ^ n


if __name__ == '__main__':
    solution = Solution()
    print(solution.missingNumber(nums = [0]))
