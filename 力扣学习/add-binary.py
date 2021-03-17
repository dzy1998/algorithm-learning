"""
Name : add-binary.py
Author : xyChen
Time : 2021/3/17 14:18
Desc: 67.二进制加法。和也用二进制表示
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:      
        # 思路就是人的二进制加法思路，实现方法很普通，时间、空间都很差
        
        la = len(a)
        lb = len(b)
        i = 1
        c = 0
        res = []
        while i <= min(la, lb):
            x = (int(a[la - i]) + int(b[lb - i]) + c) % 2
            # print(x)
            c = (int(a[la - i]) + int(b[lb - i]) + c) // 2
            # print(c)
            res.append(x)
            # print(res)
            i += 1
        # print(i)
        if i == la + 1:
            while i <= lb:
                x = (int(b[lb - i]) + c) % 2
                c = (int(b[lb - i]) + c) // 2
                res.append(x)
                i += 1
        else:
            while i <= la:
                x = (int(a[la - i]) + c) % 2
                c = (int(a[la - i]) + c) // 2
                res.append(x)
                i += 1
        if c == 1:
            res.append(c)
        res.reverse()
        ans = ''
        for item in res:
            ans += str(item)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary(a = "1010", b = "1011"))
