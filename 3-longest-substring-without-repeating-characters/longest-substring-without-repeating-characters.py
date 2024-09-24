class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while left < len(s) and s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            res = max(res, len(window))
        return res