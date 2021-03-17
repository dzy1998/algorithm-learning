"""
Name : Spiral-Matrix.py
Author : xyChen
Time : 2021/3/16 19:30
Desc: 给一个矩阵，按照顺时针遍历
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        
        # 思路参照59题的思路，只是由方阵变为了m * n
        # 本来是没有if判断的，但是提交之后有错，应该是末尾的时候有重复遍历，但是还想不到哪个循环条件有问题，或者这种方法不行。
        # 只好添加if判断，避免重复，丑陋的方法！
        # min(m, n)可能比max(m, n)节约一点时间？
        for i in range(min(m, n) // 2 + 1):
            for j in range(i, n - i):
                if len(res) < m * n:
                    res.append(matrix[i][j])
            for j in range(i + 1, m - i):
                if len(res) < m * n:
                    res.append(matrix[j][n - i - 1])
            for j in range(n - i - 2, i, -1):
                if len(res) < m * n:
                    res.append(matrix[m - i - 1][j])
            for j in range(m - i - 1, i, -1):
                if len(res) < m * n:
                    res.append(matrix[j][i])
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.spiralOrder(matrix = [[6,9,7]])
    print(res)
