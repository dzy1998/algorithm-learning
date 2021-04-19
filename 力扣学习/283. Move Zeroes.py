"""
Name : 283. Move Zeroes.py
Author : xyChen
Time : 2021/4/16 14:57
Desc:
"""
from typing import List


class Solution:
    # 思路就是设计双指针，如果j指向的位置不为0，则将这个数移动到i，i指针后移
    # 然后将i位置之后都置0
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        length = len(nums)
        for j in range(length):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for j in range(i, length):
            nums[j] = 0


if __name__ == '__main__':
    solution = Solution()
    nums = [0,1,0,3,12]
    solution.moveZeroes(nums)
    print(nums)