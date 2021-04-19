"""
Name : 279. Perfect Squares.py
Author : xyChen
Time : 2021/4/15 19:45
Desc:
"""


class Solution:
    # 思路来自@caibirdme，用到了数学定理，任何一个正整数都可以表示为4以内数的完全平方
    # 所以答案只有1，2，3，4
    # 如果n刚好是完全平方，则返回1
    # 情况为2，则进行枚举
    # 情况为4，则n满足等式n = (4 ^ a) * (8 * a + 7)
    # 其他情况，返回3
    def numSquares(self, n: int) -> int:
        if int(pow(n, 0.5)) == pow(n, 0.5):
            return 1
        for a in range(int(pow(n, 0.5)) + 1):
            for b in range(int(pow(n, 0.5)) + 1):
                if a * a + b * b == n:
                    return 2
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        return 3

        # 这思路不行，在12测试用例中，为9，1，1，1，实际最少应该是4，4，4
        # cnt = 0
        #
        # while n != 0:
        #     k = int(pow(n, 0.5))
        #     cnt += 1
        #     n -= k * k
        # return cnt


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSquares(7))
