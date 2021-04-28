"""
Name : 1769. Minimum Number of Operations to Move All Balls to Each Box.py
Author : xyChen
Time : 2021/4/23 16:00
Desc:
"""
from typing import List


class Solution:
    # 暴力法，双重循环找距离
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        length = len(boxes)
        for i in range(length):
            d = 0
            for j in range(length):
                if boxes[j] == '1':
                    d += abs(i - j)
            res.append(d)
        return res


solution = Solution()
print(solution.minOperations(boxes = "001011"))