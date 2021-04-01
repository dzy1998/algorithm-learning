"""
Name : 118. Pascal's-Triangle.py
Author : xyChen
Time : 2021/4/1 10:20
Desc:
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return [[]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        # 思路就是正常思路，只是注意内循环的循环条件
        for rol in range(2, numRows):
            l = [1]
            for col in range(1, rol):
                num = res[rol - 1][col - 1] + res[rol - 1][col]
                l.append(num)
            l.append(1)
            res.append(l)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(5))
