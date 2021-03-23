"""
Name : 35. Search-Insert-Position.py
Author : xyChen
Time : 2021/3/23 19:15
Desc: 35.搜索插入位置
"""
from typing import List


class Solution:
    # 一开始的思路是二分查找找到位置，没看到题目说的数组中没有相同的元素，考虑相同的元素应该返回第一个，就没考虑了
    # 就循环遍历找位置，一开始分的三种情况，大于、等于和小于；后来看到@嘘，我在孵蛋呐 的解答，就改成一个大于等于的条件了
    # 实际两种情况相差不大，甚至原先的运行时间还少一些
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = 0
        length = len(nums)
        for i in range(length):
            if nums[i] >= target:
                return i
            # elif nums[i] == target:
            #     pos = i
            #     break
            # else:
            #     break
        return length


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1,3,5,6], 2))
