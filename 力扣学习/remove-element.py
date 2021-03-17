"""
Name : remove-element.py
Author : xyChen
Time : 2021/3/17 15:31
Desc: 27.移除元素。原地删除数组中指定值，返回新长度
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 思路是想把指定值元素赋值为int的最大值，然后在排序之后即可将其截断
        # 后来采用了数组中的最大值代替int的最大值。
        length = len(nums)
        # 需要考虑数组为空的情况，直接返回0
        if length == 0:
            return 0
        Max = max(nums)
        cnt = 0
        # 用item来遍历的时候，可以计数，但是不能赋值，item = Max没有用？
        for i in range(length):
            if nums[i] == val:
                # item = Max
                nums[i] = Max
                cnt += 1
        nums.sort()
        return length - cnt


if __name__ == '__main__':
    # a = [1, 2, 3, 4]
    solution = Solution()
    print(solution.removeElement(nums = [3,2,2,3], val = 4))