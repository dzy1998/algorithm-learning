"""
Name : 1828. Queries on Number of Points Inside a Circle.py
Author : xyChen
Time : 2021/4/23 10:41
Desc:
"""
from typing import List


class Solution:
    # 思路就是对每个点判断是否在圆内，到圆心的距离小于等于半径
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for q in queries:
            cnt = 0
            a, b, r = q[0], q[1], q[2]
            for p in points:
                x, y = p[0], p[1]
                d2 = (a - x) * (a - x) + (b - y) * (b - y)
                if d2 <= r * r:
                    cnt += 1
            ans.append(cnt)
        return ans


solution = Solution()
print(solution.countPoints(points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]))