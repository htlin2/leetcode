class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        if len(s2) > len(s1):
            return self.areSentencesSimilar(s2, s1)
        s1 = s1.split(' ')
        s2 = s2.split(' ')
        n1, n2 = len(s1), len(s2)
        s1_left, s1_right = 0, n1 - 1
        s2_left, s2_right = 0, n2 - 1
        while s1_left < n1 and s2_left < n2 and s1[s1_left] == s2[s2_left]:
            s1_left += 1
            s2_left += 1
        while 0 <= s1_right and 0 <= s2_right and s1[s1_right] == s2[s2_right]:
            s1_right -= 1
            s2_right -= 1
        return s2_right < s2_left
"""
two pointers
"""