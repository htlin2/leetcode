class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        s1, s2 = s1.split(' '), s2.split(' ')
        s1_l, s1_r = 0, len(s1) - 1
        s2_l, s2_r = 0, len(s2) - 1
        while s1_l <= s1_r and s2_l <= s2_r and s1[s1_l] == s2[s2_l]:
            s1_l += 1
            s2_l += 1
        while s1_l <= s1_r and s2_l <= s2_r and s1[s1_r] == s2[s2_r]:
            s1_r -= 1
            s2_r -= 1
        return s1_r < s1_l or s2_r < s2_l
"""
queue or stack?
"""