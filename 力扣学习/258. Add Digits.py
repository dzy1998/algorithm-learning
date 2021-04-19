"""
Name : 258. Add Digits.py
Author : xyChen
Time : 2021/4/15 10:44
Desc:
"""
class Solution:
    # 思路为普通思路，循环，各位相加
    # 另有思路找规律
    def addDigits(self, num: int) -> int:
        while True:
            sum = 0
            while num != 0:
                sum += num % 10
                num //= 10
            num = sum
            if sum < 10:
                break
        return sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.addDigits(10))