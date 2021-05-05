"""
Name : 78. Subsets.py
Author : xyChen
Time : 2021/4/29 14:41
Desc:
"""
from typing import List


class Solution:
    # 一般这样的题目是采取回溯算法的
    # 但是这题因为给的nums里的元素全不同，所以可以简单一点
    # 思路是遍历nums，每一个x都加入到res里的子集构成新的子集，再加入res
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for x in nums:
            for i in range(len(res)):
                l = res[i].copy()
                l.append(x)
                res.append(l)
            # 这样写有问题，这样遍历不能直接向遍历对象添加新元素，死循环
            # for l in res:
            #     l1 = l.copy()
            #     l1.append(x)
            #     res.append(l1)
        return res


solution = Solution()
print(solution.subsets(nums = [0]))