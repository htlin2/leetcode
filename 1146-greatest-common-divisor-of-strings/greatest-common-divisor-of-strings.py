class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        N1, N2 = len(str1), len(str2)
        for i in range(min(N1, N2), 0, -1):
            if N1 % i or N2 % i:
                continue
            curr = str1[:i]
            s1 = N1 // i * curr
            s2 = N2 // i * curr
            if s1 == str1 and s2 == str2:
                return curr
        return ''