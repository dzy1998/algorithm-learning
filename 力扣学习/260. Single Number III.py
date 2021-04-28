"""
Name : 260. Single Number III.py
Author : xyChen
Time : 2021/4/20 13:22
Desc:
"""
from typing import List


class Solution:
    # 一开始思路是三次遍历异或操作，但是还没想明白
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if num not in res:
                res.append(num)
            else:
                res.remove(num)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber(nums = [-1,0]))
