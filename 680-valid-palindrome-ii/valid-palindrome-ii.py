class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palin(l, r):
            while l <= r:
                if l == r: return True
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True
        N = len(s)
        l, r = 0, N - 1
        while l <= r:
            if l == r: return True
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return is_palin(l + 1, r) or is_palin(l, r - 1)
        return True
"""
two pointers
abca
 lr
"""