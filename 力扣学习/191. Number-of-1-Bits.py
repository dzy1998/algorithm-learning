"""
Name : 191. Number-of-1-Bits.py
Author : xyChen
Time : 2021/4/10 9:43
Desc:
"""


class Solution:
    # 将二进制串右移，考察最低位是否为1
    # 注意运算符 >>=
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n % 2
            n >>= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight(0b00000000000000000000000000001011))
