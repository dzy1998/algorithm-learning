"""
Name : 48. Rotate-Image.py
Author : xyChen
Time : 2021/3/30 13:44
Desc:
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 旋转思路是一圈一圈往中间,r表示圈数,若为奇数维,最中间的数不需旋转
        r = n // 2
        for i in range(r):
            for j in range(i, n - i - 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp


if __name__ == '__main__':
    solution = Solution()
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution.rotate(matrix)
    print(matrix)
