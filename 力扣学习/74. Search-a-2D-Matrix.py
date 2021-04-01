"""
Name : 74. Search-a-2D-Matrix.py
Author : xyChen
Time : 2021/3/30 13:16
Desc:
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        k = 0
        m = len(matrix)
        n = len(matrix[0])
        for k in range(m):
            if matrix[k][0] <= target <= matrix[k][n - 1]:
                break

        i = 0
        j = n - 1
        # 注意n = 1时
        while i <= j:
            mid = (i + j) // 2
            if matrix[k][mid] == target:
                return True
            elif matrix[k][mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))