"""
Name : 20. Valid-Parentheses.py
Author : xyChen
Time : 2021/3/23 18:47
Desc: 20.有效的括号
"""


class Solution:
    # 思路就是简单的栈操作，利用list的append和pop实现栈的进栈、出栈
    # 匹配规则就是遇到左括号则进栈，遇到右括号则出栈，比较出栈的左括号和当前的右括号是否匹配，不匹配则False
    def isValid(self, s: str) -> bool:
        stack = []
        length = len(s)
        i = 0
        while i < length:
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            else:
                # 前两次提交出错了，需要考虑，当栈为空时遇到右括号的情况
                if len(stack) == 0:
                    return False
                ch = stack.pop()
                if s[i] == ')':
                    if ch != '(':
                        return False
                elif s[i] == ']':
                    if ch != '[':
                        return False
                else:
                    if ch != '{':
                        return False
            i += 1
        if len(stack) > 0:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid(s="(]"))
