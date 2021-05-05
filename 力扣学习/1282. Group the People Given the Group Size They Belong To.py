"""
Name : 1282. Group the People Given the Group Size They Belong To.py
Author : xyChen
Time : 2021/4/28 16:07
Desc:
"""
from typing import List


class Solution:
    # 比想象的复杂，看的一些其他解答，用的哈希表
    # 一开始遇到的困难是一边遍历时那些没能 配对的 就被跳过了
    # 类似于哈希表，字典来存储列表，如果列表的长度和键相同就插入结果列表
    # 需要进行清空操作，但是不能dict[groupSizes[i]].clear()操作，为什么？

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        dict = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in dict:
                dict[groupSizes[i]] = []
            dict[groupSizes[i]].append(i)
            if len(dict[groupSizes[i]]) == groupSizes[i]:
                res.append(dict[groupSizes[i]])
                dict[groupSizes[i]] = []
        return res


solution = Solution()
print(solution.groupThePeople(groupSizes = [2,1,3,3,3,2]))

