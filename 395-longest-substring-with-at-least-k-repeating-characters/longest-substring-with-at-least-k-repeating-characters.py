class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        def is_valid(mid):
            nonlocal res
            window = collections.defaultdict(int)
            left = 0
            for right in range(len(s)):
                window[s[right]] += 1
                while len(window) > mid:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                    left += 1
                if min(window.values()) >= k:
                    total = sum(window.values())
                    res = max(res, total)
        for i in range(1, len(set(s)) + 1):
            is_valid(i)
        return res
"""
binary search + sliding window
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

 a b a b b c
 l         r
window = {a: 2, b: 3, c: 1}
uniq_char = 3 # abc
binary search range 1 ~ 3
mid = 2

"""