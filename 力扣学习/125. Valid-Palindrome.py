"""
Name : 125. Valid-Palindrome.py
Author : xyChen
Time : 2021/4/2 10:14
Desc:
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        i = 0
        j = length - 1
        while i <= j:
            print(s[i], s[j])
            # 只考虑字母、数字是否符合回文
            # 注意python中的取反是 not
            if not s[i].isalnum() and not s[i].isalpha():
                i += 1
                continue
            if not s[j].isalnum() and not s[j].isalpha():
                j -= 1
                continue
            # 不考虑字母的大小写
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
    # print("z".isalpha())
