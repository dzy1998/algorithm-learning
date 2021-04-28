"""
Name : 771. Jewels and Stones.py
Author : xyChen
Time : 2021/4/26 14:45
Desc:
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for i in range(len(stones)):
            if stones[i] in jewels:
                cnt += 1
        return cnt


solution = Solution()
print(solution.numJewelsInStones(jewels = "z", stones = "ZZ"))