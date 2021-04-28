"""
Name : 350. Intersection of Two Arrays II.py
Author : xyChen
Time : 2021/4/21 15:15
Desc:
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        cnt = 0
        for item in nums1:
            cnt += 1
            if item in nums2:
                res.append(item)
                nums2.remove(item)
        return res


solution = Solution()
print(solution.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))