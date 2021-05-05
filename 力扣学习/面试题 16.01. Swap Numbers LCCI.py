"""
Name : 面试题 16.01. Swap Numbers LCCI.py
Author : xyChen
Time : 2021/4/28 15:20
Desc:
"""
from typing import List


class Solution:
    # 倒着返回有点偏题了
    # 加减法的思路来自@CodingGorit
    # 另有异或的思路
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] = numbers[0] + numbers[1]
        numbers[1] = numbers[0] - numbers[1]
        numbers[0] = numbers[0] - numbers[1]
        return numbers
        # return [numbers[1], numbers[0]]


solution = Solution()
print(solution.swapNumbers([1, 2]))
