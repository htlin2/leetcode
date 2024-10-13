class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        N = len(s)
        left = 0
        res = 0
        for right in range(N):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            res = max(res, len(window))
        return res
"""
sliding window
Input: s = "abcabcbb"
Output: 3
window = abc
 a b c a b c b b
   l   r
"""