class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        res = 0
        left = 0
        window = set()
        for right in range(N):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            res = max(res, len(window))
        return res
"""
sliding window variable
Input: s = "abcabcbb"
Output: 3 -> abc
window = cab
 a b c a b c b b
     l   r
"""