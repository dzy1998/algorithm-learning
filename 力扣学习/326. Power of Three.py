"""
Name : 326. Power of Three.py
Author : xyChen
Time : 2021/4/21 10:38
Desc:
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 0:
            if n % 3 == 0:
                n //= 3
            else:
                break
        return n == 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfThree(45))