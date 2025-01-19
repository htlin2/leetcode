class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for i in range(1, len(set(s)) + 1):
            window = collections.defaultdict(int)
            left = 0
            for right, char in enumerate(s):
                window[char] += 1
                while len(window) > i:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                    left += 1
                is_valid = all([True if v >= k else False for v in window.values()])
                if is_valid:
                    res = max(res, right - left + 1)
        return res

"""
brute force

"""