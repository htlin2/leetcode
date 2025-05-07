class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        uniq_chars = set(s)
        res = 0
        for i in range(1, len(uniq_chars) + 1):
            window = collections.defaultdict(int)
            left = 0
            for right in range(len(s)):
                window[s[right]] += 1
                if min(window.values()) >= k:
                    res = max(res, right - left + 1)
                while left <= right and len(window) > i:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                    left += 1
        return res
"""
sliding window
"""