"""
Name : pow-x-n.py
Author : xyChen
Time : 2021/3/17 10:02
Desc: 50.实现幂运算
"""


# 看到题目的时候，一下子就想到了递归，写起来漂亮，但是耗时、耗空间
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 指数为负的情况，直接转化为正，这思路是我没想到的
        if n < 0:
            return 1 / self.myPow(x, -n)
        res = 1
        # 方法来自@刘扬俊，快速幂方法，思路是通过底数平方，降低指数。
        # 还有提升空间，如加入移位运算等
        while n > 0:
            if n % 2 == 0:
                n /= 2
                x *= x
            else:
                res *= x
                n = (n - 1) / 2
                x *= x
        return res

        # 此法不通。一开始的递归思路是x * pow(x, n),直接就爆了空间
        # 修改后是pow(x, n / 2) * pow(x, n / 2),在同一测试用例中，超时
        # 思路也是降低指数，和上述通过的方法相比，还是差的远了
        # if n == -1:
        #     return 1 / x
        # elif n == 0:
        #     return 1
        # elif n == 1:
        #     return x
        # else:
        #     if n % 2 == 0:
        #         return self.myPow(x, n // 2) * self.myPow(x, n // 2)
        #     else:
        #         return self.myPow(x, n // 2) * self.myPow(x, n // 2 + 1)
        # if n < 0:
        #     return 1 / x * self.myPow(x, n + 1)
        # elif n == 0:
        #     return 1
        # else:
        #     return x * self.myPow(x, n - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(x = 2.00000, n = -2))
    # print(-5 // 2)
