"""
Name : 231. Power-of-Two.py
Author : xyChen
Time : 2021/4/14 20:11
Desc:
"""
class Solution:
    # 一开始是普通思路
    # 后来无意看到了相似题目中有191题，就想到了位运算
    # 数是2的幂特点为1在最左边，且只有一个1
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n:
            x = n % 2
            n >>= 1
            if x == 1:
                break
        return n == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfTwo(16))