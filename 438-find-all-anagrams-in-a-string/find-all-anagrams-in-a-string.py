class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = collections.Counter(p)
        window = {}
        res = []
        l = 0
        for r in range(len(s)):
            if r - l + 1 > len(p):
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            if s[r] in window:
                window[s[r]] += 1
            else:
                window[s[r]] = 1
            if window == counter:
                res.append(l)
        return res

"""
sliding window fixed
cbaebabacd
0123456789
abc   abc
"""