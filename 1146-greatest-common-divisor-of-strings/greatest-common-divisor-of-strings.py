class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        n1, n2 = len(str1), len(str2)
        for i in range(n2 + 1, 0, -1):
            if n1 % i or n2 % i:
                continue
            s2 = str2[:i]
            base2 = n2 // i
            base1 = n1 // i
            if s2 * base2 == str2 and s2 * base1 == str1:
                return s2
        return ''
                