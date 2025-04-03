class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        s1_s = s1.split(' ')
        s2_s = s2.split(' ')
        if len(s1) < len(s2): return self.areSentencesSimilar(s2, s1)
        s1 = s1_s
        s2 = s2_s
        n1, n2 = len(s1), len(s2)
        s1_l, s1_r = 0, n1 - 1
        s2_l, s2_r = 0, n2 - 1
        while s2_l <= s2_r and s1[s1_l] == s2[s2_l]:
            s1_l += 1
            s2_l += 1
        while 0 <= s2_r and s1[s1_r] == s2[s2_r]:
            s1_r -= 1
            s2_r -= 1
        if s2_r < s2_l:
            return True
        return False
"""
two pointers
Input: sentence1 = "My name is Haley", sentence2 = "My Haley"

s1 = My, name, is, Haley
     l               r
s2 = My, Haley
     l    r


Input: sentence1 = "Eating right now", sentence2 = "Eating"
s1 = Eating, right, now
      l              r
s2 = Eating
       lr

s1 = Lucccky

s2 = Luky

"""