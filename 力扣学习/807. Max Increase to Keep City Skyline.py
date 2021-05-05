"""
Name : 807. Max Increase to Keep City Skyline.py
Author : xyChen
Time : 2021/4/28 15:02
Desc:
"""
from typing import List


class Solution:
    # 题目讲述很复杂，思路比较简单
    # 找到二维数组每行、每列的最大值
    # 可以的增量就是行、列最大值的较小者
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        width = len(grid)
        il = []
        jl = []
        for j in range(width):
            maxHight = max(grid[j])
            jl.append(maxHight)
        for i in range(length):
            # 列表生成器
            maxHight = max(x[i] for x in grid)
            # for j in range(width):
            #     if grid[j][i] > maxHight:
            #         maxHight = grid[j][i]
            il.append(maxHight)

        d = 0
        for i in range(length):
            for j in range(width):
                d += min(jl[j], il[i]) - grid[j][i]
        return d


solution = Solution()
print(solution.maxIncreaseKeepingSkyline(grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))

