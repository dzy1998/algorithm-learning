"""
Name : 344. Reverse String.py
Author : xyChen
Time : 2021/4/21 10:55
Desc:
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(length // 2):
            s[i], s[length - 1 - i] = s[length - 1 - i], s[i]
            # temp = s[i]
            # s[i] = s[length - 1 - i]
            # s[length - 1 - i] = temp


if __name__ == '__main__':
    solution = Solution()
    s = ["H","a","n","n","a","h"]
    solution.reverseString(s)
    print(s)