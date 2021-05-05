"""
Name : 1791. Find Center of Star Graph.py
Author : xyChen
Time : 2021/4/28 15:58
Desc:
"""
from typing import List


class Solution:
    # 好蠢
    def findCenter(self, edges: List[List[int]]) -> int:
        e1 = edges[0]
        e2 = edges[1]
        for x in e1:
            if x in e2:
                return x


solution = Solution()
print(solution.findCenter(edges = [[1,2],[5,1],[1,3],[1,4]]))
