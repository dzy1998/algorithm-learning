"""
Name : 202. Happy-Number.py
Author : xyChen
Time : 2021/4/10 10:00
Desc:
"""


class Solution:
    # 相当于暴力法，设定了循环上限20次
    # 实际上如果一个数不快乐，在计算过程中n会出现循环的数
    def isHappy(self, n: int) -> bool:
        loopCnt = 0
        while n != 1:
            res = []
            while n != 0:
                digit = n % 10
                res.append(digit)
                n //= 10
            while len(res) > 0:
                n += pow(res.pop(), 2)
            loopCnt += 1
            if loopCnt > 20:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(100))
