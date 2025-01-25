class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        for i in range(min(n1, n2), 0, -1):
            if n1 % i or n2 % i:
                continue
            m1, m2 = n1 // i, n2 // i
            if m1 * str1[:i] == str1 and m2 * str1[:i] == str2:
                return str1[:i]
        return ''
"""
greedy + math
"""