"""
Name : 169. Majority-Element.py
Author : xyChen
Time : 2021/4/9 13:46
Desc:
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 思路一开始很简单，既然题目说明了必有众数，则可以考虑直接排序，然后返回中间值
        # 但是如果直接用api接口，则失去了算法的意义；手写排序算法，时间开销太大
        # 有考虑其他的遍历列表的方法，但无果。该摩尔投票法思路来自@YourBaymax
        # 思路就是major记录一个数，遍历列表，与major相同则cnt + 1，不同则cnt - 1
        # 如果cnt = 0，则重新记录major
        cnt = 0
        for num in nums:
            if cnt == 0:
                major = num
            if num == major:
                cnt += 1
            else:
                cnt -= 1
        return major


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([3,2,3]))
