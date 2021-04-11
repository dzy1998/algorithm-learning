"""
Name : 215. Kth-Largest-Element-in-an-Array.py
Author : xyChen
Time : 2021/4/10 14:32
Desc:
"""
from typing import List


class Solution:
    # 找到数组中第k大的元素，思路就是先排序，在返回所求值
    # 这个快速排序思路来自《算法图解》，看到的时候非常新奇，比上课时学的简单、清晰一点
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = self.quickSort(nums)
        return nums[k - 1]

    def quickSort(self, nums: List[int]):
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[0]
            less = [i for i in nums[1:] if i <= pivot]
            greater = [i for i in nums[1:] if i > pivot]
            return self.quickSort(greater) + [pivot] + self.quickSort(less)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
