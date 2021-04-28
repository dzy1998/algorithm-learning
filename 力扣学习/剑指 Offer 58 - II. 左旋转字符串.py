"""
Name : 剑指 Offer 58 - II. 左旋转字符串.py
Author : xyChen
Time : 2021/4/26 14:30
Desc:
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[0:n]


solution = Solution()
print(solution.reverseLeftWords(s = "lrloseumgh", k = 6))
