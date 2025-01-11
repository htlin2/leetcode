class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_uniq_chars = len(set(s))
        res = 0
        for uniq_chars in range(1, max_uniq_chars + 1):
            left = 0
            window = collections.defaultdict(int)
            for right in range(len(s)):
                window[s[right]] += 1
                while len(window) > uniq_chars:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                    left += 1
                is_valid = all([True if v >= k else False for v in window.values()])
                if is_valid:
                    res = max(res, sum(window.values()))
        return res