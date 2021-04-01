"""
Name : 73. Set-Matrix-Zeroes.py
Author : xyChen
Time : 2021/3/30 14:25
Desc:
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 两个集合记录0数据所在的行和列
        i_set = set()
        j_set = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    i_set.add(i)
                    j_set.add(j)
        while len(i_set) > 0:
            i = i_set.pop()
            for j in range(n):
                matrix[i][j] = 0
        while len(j_set) > 0:
            j = j_set.pop()
            for i in range(m):
                matrix[i][j] = 0


if __name__ == '__main__':
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution = Solution()
    solution.setZeroes(matrix)
    print(matrix)