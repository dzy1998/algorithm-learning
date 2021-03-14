"""
Name : twoSum.py
Time : 2021/3/14 14:21
Desc: 给定一个数组和目标值，找到数组中和为目标值的两个数，并返回下标
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        number = len(nums)
        # 考虑过先将排序，然后从两边向中间遍历，但是排序后数组中的下标发生改变

        for i in range(number):
            # 由于要求数组中的同一元素不能使用两次，故j从i + 1开始遍历
            for j in range(i + 1, number):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
                else:
                    continue

