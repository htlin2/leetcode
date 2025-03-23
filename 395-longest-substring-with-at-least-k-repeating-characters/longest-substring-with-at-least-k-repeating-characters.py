class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_uniq_chars = len(set(s))
        counter = collections.Counter(s)
        res = 0
        for i in range(1, max_uniq_chars + 1):
            window = collections.defaultdict(int)
            left = 0
            for right in range(len(s)):
                window[s[right]] += 1
                while len(window) > i:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                    left += 1
                is_valid = min(window.values()) >= k
                if is_valid:
                    res = max(res, sum(window.values()))
        return res