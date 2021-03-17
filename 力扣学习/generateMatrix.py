"""
Name : generateMatrix.py
Author : xyChen
Time : 2021/3/16 13:39
Desc: 螺旋矩阵，n * n
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # i = 0
        # j = 0
        num = 1
        # list = [0 for x in range(0, n)]
        # lists = [list for x in range(0, n)]出错，可能时lists[0]发生变化时，lists[1]、2、3同时发生变化，因为是指向同一块内容？
        lists = [[0 for x in range(0, n)] for x in range(0, n)]

        # 方法来自@不能说的秘密
        for i in range(n // 2 + 1):
            # i, j并不是指矩阵索引
            for j in range(i, n - i):
                lists[i][j] = num
                num += 1
            for j in range(i + 1, n - i):
                lists[j][n - i - 1] = num
                num += 1
                # 下边赋值
            for j in range(n - i - 2, i, -1):
                lists[n - i - 1][j] = num
                num += 1
                # 左边赋值
            for j in range(n - i - 1, i, -1):
                lists[j][i] = num
                num += 1
        # 下面这种方法不可行，在于移动的优先级混乱，逆时针的优先级应为右 > 下 > 左 > 上 > 右，不可能
        # while num <= n * n:
        #     lists[i][j] = num
        #     num += 1
        #     if j < n - 1 and lists[i][j + 1] == 0:
        #         j += 1
        #         continue
        #     if i < n - 1 and lists[i + 1][j] == 0:
        #         i += 1
        #         continue
        #     if j > 0 and lists[i][j - 1] == 0:
        #         j -= 1
        #         continue
        #     if i > 0 and lists[i - 1][j] == 0:
        #         i -= 1
        # print(i, j)
        # lists[i][j] = n

        # 此法不通
        # for num in range(1, n * n + 1):
        #     for j in range(j, n - i - 1):
        #         lists[i][j] = num
        #         num += 1
        #         if lists[i][j + 1] != 0:
        #             break
        #     for i in range(i, j - 1):
        #         lists[i][j] = num
        #         num += 1
        #         if lists[i + 1][j] != 0:
        #             break
        #     for j in range(j, n - i - 1, -1):
        #         lists[i][j] = num
        #         num += 1
        #         if lists[i][j - 1] != 0:
        #             break
        #     for i in range(j, i, -1):
        #         lists[i][j] = num
        #         num += 1
        #         if lists[i - 1][j] != 0:
        #             break

        return lists


if __name__ == '__main__':
    soletion = Solution()
    print(soletion.generateMatrix(1))
