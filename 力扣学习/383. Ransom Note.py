"""
Name : 383. Ransom Note.py
Author : xyChen
Time : 2021/4/22 15:27
Desc:
"""


class Solution:
    # 思路和之前350集合交集的题目相像
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mList = list(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] in mList:
                mList.remove(ransomNote[i])
            else:
                return False
        return True


solution = Solution()
print(solution.canConstruct(ransomNote="aa", magazine="aab"))
