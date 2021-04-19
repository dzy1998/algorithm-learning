"""
Name : 242. Valid Anagram.py
Author : xyChen
Time : 2021/4/15 10:16
Desc:
"""
class Solution:
    # 判断是否为字母异位词，就是两个字符串只是字符的位置不同
    # 思路为遍历字符串s，对于每一个s字符，考察是否在u列表中，若存在，则移除
    # 若不存在，则考察t字符串当前字符，若不相同，则将该字符加入u列表，继续遍历t字符串，直到找到相同的为止
    def isAnagram(self, s: str, t: str) -> bool:
        u = []
        j = 0
        length1 = len(s)
        length2 = len(t)
        if length1 != length2:
            return False
        for i in range(length1):
            if s[i] in u:
                u.remove(s[i])
                continue
            while j < length2:
                if t[j] != s[i]:
                    u.append(t[j])
                    j += 1
                else:
                    j += 1
                    break
        return len(u) == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram(s = "rat", t = "car"))