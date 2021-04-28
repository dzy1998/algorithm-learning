"""
Name : 263. Ugly Number.py
Author : xyChen
Time : 2021/4/20 13:34
Desc:
"""
class Solution:
    # 思路是能被2，3，5整除就一直除，如果结果不是1，就不是丑数
    # 注意负数不是丑数
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n //= 2
                continue
            if n % 3 == 0:
                n //= 3
                continue
            if n % 5 == 0:
                n //= 5
                continue
            return False
        if n == 1:
            return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isUgly(n = 55))