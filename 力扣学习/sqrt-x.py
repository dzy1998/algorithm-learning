"""
Name : sqrt-x.py
Author : xyChen
Time : 2021/3/17 13:37
Desc: 69. x的平方根, 返回的是整型
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # if x == 0:
        #     return 0
        # elif x == 1:
        #     return 1
        # else:
        # 思路就是二分查找符合条件的值，由于一定有平方根，所有有些地方没考虑，比如循环条件应是a,b
        # 应该用除法，因为相乘可能会溢出
        # 还有其他方法，牛顿法？
        
        a = 0
        b = x
        while True:
            mid = (a + b) // 2
            # print(a, b, mid)
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid < x:
                a = mid + 1
            else:
                b = mid - 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(10001))
