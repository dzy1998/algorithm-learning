"""
Name : Remove-Duplicates-from-Sorted-Array.py
Author : xyChen
Time : 2021/3/23 9:57
Desc: 26. 删除有序数组中的重复项.不使用额外空间
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        i, j = 0, 1
        while j < length:
            # 记得做前面某一题的时候，看大家的讨论中有一种双指针的思路，所以这题马上想到了双指针的思路
            # 双指针指向内容不同时,就这么移下去,相同时的做法一开始没想到,看了@x yao的博客才会
            # 是一个一直比较是否相同的过程
            if nums[i] == nums[j]:
                j += 1
                continue
            nums[i + 1] = nums[j]
            i += 1
            j += 1
        return i + 1


if __name__ == '__main__':
    # nums = [1, 2, 3, 3, 3, 4, 5, 5, 6]
    solution = Solution()
    res = solution.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4])
    print(res)
    # print(nums)
