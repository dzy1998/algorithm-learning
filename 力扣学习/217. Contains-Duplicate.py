"""
Name : 217. Contains-Duplicate.py
Author : xyChen
Time : 2021/4/10 15:05
Desc:
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 利用集合的自动去重性质，将原列表转为集合，比较两者的长度，若是有重复，则长度会比列表短
        return len(set(nums)) < len(nums)

        # 普通思路，排序之后，比较相邻的元素是否相同，超时
        nums = self.quickSort(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


    def quickSort(self, nums):
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[0]
            less = [i for i in nums[1:] if i <= pivot]
            greater = [i for i in nums[1:] if i > pivot]
            return self.quickSort(less) + [pivot] + self.quickSort(greater)


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))
