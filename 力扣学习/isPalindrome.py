"""
Name : isPalindrome.py
Author : xyChen
Time : 2021/3/15 16:05
Desc: 给定一个整数，判断是否符合回文。思路将其转换为字符串，从两端遍历，判断是否相等，不相等即不是回文
"""


class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        s1 = str(x)
        length = len(s1)
        for i in range(0, length):
            # 注意(0, length-1)才是字符串的索引范围
            if s1[i] == s1[length - 1 - i]:
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    flag = solution.isPalindrome(10)
    print(flag)
