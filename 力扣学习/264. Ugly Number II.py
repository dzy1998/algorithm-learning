"""
Name : 264. Ugly Number II.py
Author : xyChen
Time : 2021/4/20 13:50
Desc:
"""


class Solution:
    # 这样的思路不行，超出时间限制
    def nthUglyNumber(self, n: int) -> int:
        num = 1
        while n != 0:
            if self.isUgly(num):
                n -= 1
            num += 1
        return num - 1

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
    print(solution.nthUglyNumber(401))
