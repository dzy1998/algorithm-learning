"""
Name : 347. Top K Frequent Elements.py
Author : xyChen
Time : 2021/4/21 13:45
Desc:
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        res = []
        for i in range(len(nums)):
            if nums[i] in myDict:
                myDict[nums[i]] += 1
            else:
                myDict[nums[i]] = 1
        # 思路就是对输入进行建立字典，以键值的形式存储数和次数，按值进行排序
        # 直接使用sorted函数不够好
        mylist = sorted(myDict.items(), key=lambda item:item[1], reverse=True)
        for i in range(k):
            res.append(mylist[i][0])
        return res


solution = Solution()
# solution.topKFrequent(nums = [1,2,1,2,2,3], k = 2)
print(solution.topKFrequent(nums = [1,1,1,2,2,3], k = 2))



