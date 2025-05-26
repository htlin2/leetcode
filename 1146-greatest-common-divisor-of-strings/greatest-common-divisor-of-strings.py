class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        if n1 < n2:
            return self.gcdOfStrings(str2, str1)
        for i in range(n2, 0, -1):
            w2 = str2[:i]
            w1 = str1[:i]
            if n2 % len(w2) != 0 or n1 % len(w1) != 0:
                continue
            if w1 != w2:
                continue
            base2 = n2 // len(w2)
            base1 = n1 // len(w1)
            if base2 * w2 == str2 and base1 * w1 == str1:
                return w2
        return ''
