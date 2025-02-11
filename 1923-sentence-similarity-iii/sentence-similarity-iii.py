class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        if len(s2) > len(s1):
            return self.areSentencesSimilar(s2, s1)
        w1, w2 = s1.split(' '), s2.split(' ')
        w1_l, w1_r, w2_l, w2_r = 0, len(w1) - 1, 0, len(w2) - 1
        while w1_l < len(w1) and w2_l < len(w2) and w1[w1_l] == w2[w2_l]:
            w1_l += 1
            w2_l += 1
        while w1_r >= 0 and w2_r >= 0 and w1[w1_r] == w2[w2_r]:
            w1_r -= 1
            w2_r -= 1
        return w1_l > w2_r
"""
two pointers
handle both sides
handle front or back
"""