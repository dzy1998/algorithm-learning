"""
Name : Count-and-Say.py
Author : xyChen
Time : 2021/3/23 10:41
Desc: 38.外观数列
"""

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 第一项是数字 1
# 描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
# 描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
# 描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
# 描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"

class Solution:
    # 题目没有时间要求,适合于递归解法
    def countAndSay(self, n: int) -> str:
        # 给出前几项的返回值,作为递归出口
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        elif n == 3:
            return '21'
        # 递归开始
        s = self.countAndSay(n - 1)
        res = ''
        i = s[0]
        count = 0
        # 本来是采用while循环,但是i和i+1项比较中,在最后一项的时候会溢出
        # 换了一种思路,取i作为临时字符,比较item与i是否相等
        for item in s:
            if item == i:
                count += 1
            else:
                res += str(count) + i
                i = item
                count = 1
        # 循环最后一项加到外观数列中
        res += str(count) + i
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(5))