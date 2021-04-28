"""
Name : 1512. Number of Good Pairs.py
Author : xyChen
Time : 2021/4/26 14:52
Desc:
"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        length = len(nums)
        if length < 2:
            return 0
        nums = self.quickSort(nums)
        print(nums)
        for i in range(length - 1):
            j = i + 1
            while nums[i] == nums[j]:
                j += 1
                if j == length:
                    break
            cnt += j - i - 1
        return cnt

    def quickSort(self, nums):
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[0]
            less = [x for x in nums[1:] if x <= pivot]
            greater = [x for x in nums[1:] if x > pivot]
            return self.quickSort(less) + [pivot] + self.quickSort(greater)


solution = Solution()
print(solution.numIdenticalPairs(nums = [1,2,3]))