"""
Name : 204. Count-Primes.py
Author : xyChen
Time : 2021/4/12 18:48
Desc:
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        cnt = 0
        numList = [1] * n
        for i in range(2, n):
            if numList[i] == 1:
                cnt += 1
                for j in range(i + i, n, i):
                    numList[j] = 0
        return cnt

    # 算法来自厄拉多塞筛法，下面是自己实现的，但是仍旧超时
    # 上面的做法来自@Sailkiki
    # 为什么上面的双循环反而不会超时
    # 可能n增大的时候，上面的内循环的步长越来越大，循环次数逐渐减少
    # 下面在n增大的时候，列表内的元素增加，比较次数增加

    def myCountPrimes(self, n: int) -> int:
        primeList = []
        for i in range(2, n):
            if not self.cmp(i, primeList):
                primeList.append(i)
        return len(primeList)

    # 比较n是否为某数的倍数
    def cmp(self, n, primeList):
        flag = False
        for num in primeList:
            if n % num == 0:
                flag = True
                break
        return flag


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrimes(1500000))
