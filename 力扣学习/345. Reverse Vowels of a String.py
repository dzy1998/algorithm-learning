"""
Name : 345. Reverse Vowels of a String.py
Author : xyChen
Time : 2021/4/21 13:27
Desc:
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelsList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        sl = list(s)
        i = 0
        j = len(sl) - 1
        while i < j:
            while sl[i] not in vowelsList and i < j:
                i += 1
            while sl[j] not in vowelsList and i < j:
                j -= 1

            sl[i], sl[j] = sl[j], sl[i]
            i += 1
            j -= 1
        return ''.join(sl)


solution = Solution()
print(solution.reverseVowels("iU"))