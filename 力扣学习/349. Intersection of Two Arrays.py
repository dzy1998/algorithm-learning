"""
Name : 349. Intersection of Two Arrays.py
Author : xyChen
Time : 2021/4/21 14:45
Desc:
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mySet1 = set(nums1)
        mySet2 = set(nums2)
        res = []
        for item in mySet1:
            if item in mySet2:
                res.append(item)
        return res


solution = Solution()
print(solution.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
