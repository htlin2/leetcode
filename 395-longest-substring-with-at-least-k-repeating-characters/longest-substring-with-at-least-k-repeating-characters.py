class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def get_longest(i):
            res = 0
            window = collections.defaultdict(int)
            l = 0
            for r in range(len(s)):
                window[s[r]] += 1
                while len(window) > i:
                    window[s[l]] -= 1
                    if window[s[l]] == 0:
                        del window[s[l]]
                    l += 1
                if min(window.values()) >= k:
                    res = max(res, r - l + 1)
            return res

        res = 0
        for i in range(1, len(set(s)) + 1):
            longest = get_longest(i)
            res = max(res, longest)
        return res
"""
backtracking
+/- substring

sliding window + binary search

"""