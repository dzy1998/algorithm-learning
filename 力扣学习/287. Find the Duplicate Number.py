"""
Name : 287. Find the Duplicate Number.py
Author : xyChen
Time : 2021/4/16 15:30
Desc:
"""
from typing import List


class Solution:
    # 一开始以为和之前找重复数、缺失数的思路相同，采用异或的位运算
    # 后来没什么好的思路，就只是快速排序，然后比较相邻位置是否相同
    def findDuplicate(self, nums: List[int]) -> int:
        nums = self.quickSort(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

    def quickSort(self, nums: List[int]):
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[0]
            less = [i for i in nums[1:] if i <= pivot]
            greater = [i for i in nums[1:] if i > pivot]
            return self.quickSort(less) + [pivot] + self.quickSort(greater)

        # 思路错误，不一定其他数都存在且唯一，重复次数可能大于2
        # res = 0
        # n = len(nums) - 1
        # for num in nums:
        #     res ^= num
        # for i in range(1, n + 1):
        #     res ^= i
        # return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findDuplicate(nums = [2,2,2,2,2]))
