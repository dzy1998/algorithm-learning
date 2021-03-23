"""
Name : 46.Permutations.py
Author : xyChen
Time : 2021/3/23 13:34
Desc:
"""
import math
import random
from typing import List


class Solution:
    # 一开始的思路是把数组排序,然后倒序,两两交换一次就将此新列表加到res中,但是发现这样的结果并不是全排列
    # 后来的思路是完全随机的取一个数,如果不在l中,就加入l,如果l不在res中,就加入res中,直到res的长度满了
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # nums.sort()
        length = len(nums)
        # n个不同的数,全排列产生n!个序列
        while len(res) < math.factorial(length):
            l = []
            while len(l) < length:
                pos = random.randint(0, length - 1)
                if nums[pos] not in l:
                    l.append(nums[pos])
            if l not in res:
                res.append(l)
        # 此法不通
        # for i in range(length):
        #     for j in range(i + 1, length):
        #         print(i, j)
        #         print(nums)
        #
        #         res.append(nums)
        #         nums[i], nums[j] = nums[j], nums[i]
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
    # print(random.randint(0, 9))