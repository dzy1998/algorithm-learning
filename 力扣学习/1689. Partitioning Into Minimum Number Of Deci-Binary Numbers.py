"""
Name : 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers.py
Author : xyChen
Time : 2021/4/23 14:38
Desc:
"""


class Solution:
    # 这题思路来自@刷leetcode真无聊
    # 一开始我试图在字符串前几位找规律
    # 不成功之后就去看了一下大家的思路，顿时豁然开朗，有点脑筋急转弯的意思
    # 只需要找字符串中的最大值就行了，这一位需要全1，其他地方可以用0或1补
    def minPartitions(self, n: str) -> int:
        return int(max(n))


solution = Solution()
print(solution.minPartitions(n="27346209830709182346"))
