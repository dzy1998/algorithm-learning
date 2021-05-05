"""
Name : 剑指 Offer 56 - II. 数组中数字出现的次数 II.py
Author : xyChen
Time : 2021/4/29 16:11
Desc:
"""
from typing import List


class Solution:
    # 思路就是求和，然后减去3倍每一个没减过的数，最后的差就是所求数的-2倍
    def singleNumber(self, nums: List[int]) -> int:
        ans = sum(nums)
        l = []
        for x in nums:
            if x not in l:
                ans -= 3 * x
                l.append(x)
        return (-ans) // 2


solution = Solution()
print(solution.singleNumber(nums = [9,1,7,9,7,9,7]))