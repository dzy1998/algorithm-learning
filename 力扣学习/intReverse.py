"""
Name : intReverse.py
Time : 2021/3/14 15:32
Desc: 给定一个有符号数，将数字部分反转并返回
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 特殊情况，0就直接返回0
        if x == 0:
            return 0
        sum = 0
        # 获得数的符号
        flag = int(x < 0)
        number = abs(x)
        # 反转思路是不断取个位数字再乘10相加，这样考虑了末位为0的情况；另可以考虑转化为字符串
        while number != 0:
            k = number % 10
            sum = sum * 10 + k
            # python整除符号//, /则会自动转换类型，结果产生inf
            number = number // 10
        # 对于32位限制的考虑
        if sum < -pow(2, 31) or sum > pow(2, 31) - 1:
            return 0
        if flag == 0:
            return sum
        return 0 - sum
