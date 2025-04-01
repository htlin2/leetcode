class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
        def is_valid(window, counter):
            if len(window) != len(counter): return False
            for key in window.keys():
                if window[key] < counter[key]: return False
            return True
        counter = collections.Counter(t)
        window = collections.defaultdict(int)
        left = 0
        res = ''
        for right in range(len(s)):
            if s[right] in counter:
                window[s[right]] += 1
            while is_valid(window, counter):
                if not res or len(res) >= (right - left + 1):
                    res = s[left:right + 1]
                if s[left] in window:
                    window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
        return res
"""
sliding window variable
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
window = {A: 1, B: 1, C: 1}
ADOBECODEBANC
L    R
"""