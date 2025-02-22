class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        w1, w2 = s1.split(' '), s2.split(' ')
        w1_left, w2_left = 0, 0
        while w1_left < len(w1) and w2_left < len(w2) and w1[w1_left] == w2[w2_left]:
            w1_left += 1
            w2_left += 1
        w1_right, w2_right = len(w1) - 1, len(w2) - 1
        while w1_right >= 0 and w2_right >= 0 and w1[w1_right] == w2[w2_right]:
            w1_right -= 1
            w2_right -= 1
        return w2_right < w1_left
"""
two pointers
Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
w1 = [My, name, is, Haley]
          w1_l  w2_r
w2 = [My, Haley]
      w2_r  w2_l

"""