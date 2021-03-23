"""
Name : Median-of-Two-Sorted-Arrays.py
Author : xyChen
Time : 2021/3/18 11:19
Desc: 4.寻找两个正序数组的中位数
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedList = nums1 + nums2
        mergedList.sort()
        length = len(mergedList)
        i = length // 2
        if length % 2 == 0:
            return (mergedList[i - 1] + mergedList[i]) / 2
        else:
            return mergedList[i]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1 = [2], nums2 = []))