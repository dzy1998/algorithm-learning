"""
Name : container-with-most-water.py
Author : xyChen
Time : 2021/3/17 16:02
Desc: 11.乘最多水的容器
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 一开始的做的是双重循环，结果是超时。也设想两边指针向中间移动，但是移动的条件错了
        area_max = 0
        a = 0
        b = len(height) - 1
        while a < b:
            area_max = max(area_max, min(height[a], height[b]) * (b - a))
            # 这个移动条件思路来自@ChengMing。自己考虑的是比较的是a和a+1、b和b-1
            # 应该是a,b之间比较，小的那一遍向中间靠拢
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1

        # for i in range(length):
        #     for j in range(i + 1, length):
        #         area = min(height[i], height[j]) * (j - i)
        #         if area > area_max:
        #             area_max = area
        
        return area_max


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea(height=[1, 2, 1]))
