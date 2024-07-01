class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        res = ''
        for i in range(0, len(s)):
            # get odd
            odd = getPalindrome(i, i)
            # get even
            even = getPalindrome(i, i + 1)
            if len(res) < len(odd):
                res = odd
            if len(res) < len(even):
                res = even
        return res


"""
sliding window + hashmap
babad
bab


brute force
ans = bab
time: n * (n + n) > n^2
space: n
"""