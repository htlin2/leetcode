class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_match(s_counter, t_counter):
            if len(s_counter.keys()) != len(t_counter.keys()):
                return False
            for key in s_counter.keys():
                if s_counter[key] < t_counter[key]:
                    return False
            return True
        if len(s) < len(t):
            return ''
        res = ''
        t_counter = collections.Counter(t)
        s_counter = {}
        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in t_counter:
                s_counter[char] = s_counter.get(char, 0) + 1
            while is_match(s_counter, t_counter):
                if not res or right - left + 1 < len(res):
                    res = s[left: right+1]
                s_char = s[left]
                if s_char in s_counter:
                    s_counter[s_char] -= 1
                    if s_counter[s_char] == 0:
                        del s_counter[s_char]
                left += 1
        return res
"""
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
t_counter = {A: 1, B: 1, C: 1}
s_counter = {A: 1, B: 2, C: 1}
s = "ADOBECODEBANC"
      L       R
window = ADOBEC
"""