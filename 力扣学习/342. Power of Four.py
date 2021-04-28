"""
Name : 342. Power of Four.py
Author : xyChen
Time : 2021/4/21 10:50
Desc:
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 0:
            if n % 4 == 0:
                n >>= 2
            else:
                break
        return n == 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfFour(8))