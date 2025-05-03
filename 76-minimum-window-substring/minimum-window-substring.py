class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = collections.Counter(t)
        window_counter = {}
        matched_chars = 0
        left = 0
        res = ''
        for right in range(len(s)):
            # expand window logic
            if s[right] in t_counter:
                if s[right] not in window_counter:
                    window_counter[s[right]] = 0
                window_counter[s[right]] += 1
                if window_counter[s[right]] == t_counter[s[right]]:
                    matched_chars += 1
            # shrink window logic
            while left <= right and matched_chars == len(t_counter):
                if not res or len(res) >= (right - left + 1):
                    res = s[left:right + 1]
                if s[left] in window_counter:
                    if window_counter[s[left]] == t_counter[s[left]]:
                        matched_chars -= 1
                    window_counter[s[left]] -= 1
                    if window_counter[s[left]] == 0:
                        del window_counter[s[left]]
                left += 1
        return res
"""
hashmap + sliding window
Input: s = "ADOBECODEBANC", t = "ABC"
t_counter = {A: 1, B: 1, C: 1}
res = ADOBEC
window_counter = {A: 1, B: 1, C: 1}
 A D O B E C O D E B A N C
                     L   R
"""