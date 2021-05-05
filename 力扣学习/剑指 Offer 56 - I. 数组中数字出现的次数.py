"""
Name : 剑指 Offer 56 - I. 数组中数字出现的次数.py
Author : xyChen
Time : 2021/4/29 15:51
Desc:
"""
from typing import List


class Solution:
    # 思路来自@Ant
    # 以前昨天只有一个元素是只有一个的
    # 这里有两个，有一个分组的思想
    # 要想到第一次全部异或后，相当于两个数的异或，而这个结果的二进制表示中的1表示这两个数在这一位上是不一样
    # 分组的依据就是这个，这位上为1的一组，为0的一组
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = 0
        index = 0
        for x in nums:
            res ^= x
        while res % 2 == 0:
            res >>= 1
            index += 1
        r1, r2 = 0, 0
        for x in nums:
            if (x >> index) & 1 == 0:
                r1 ^= x
            else:
                r2 ^= x
        return [r1, r2]


solution = Solution()
print(solution.singleNumbers(nums = [1,2,10,4,1,4,3,3]))

