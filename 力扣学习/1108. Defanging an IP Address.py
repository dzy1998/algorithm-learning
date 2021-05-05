"""
Name : 1108. Defanging an IP Address.py
Author : xyChen
Time : 2021/4/28 14:54
Desc:
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        l = address.split('.')
        addr = '[.]'.join(l)
        return addr


solution = Solution()
print(solution.defangIPaddr(address = "255.100.50.0"))